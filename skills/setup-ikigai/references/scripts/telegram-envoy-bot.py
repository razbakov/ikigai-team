#!/usr/bin/env python3
"""
Envoy Bot — @envoy_bot

Universal gateway to the owner's AI agent system. Two modes:

1. ENVOY MODE (existing): Outbound agenda-driven conversations via Butler.
   Share t.me/ai_lifeos_bot?start=<slug> with a contact.

2. AGENT MODE (new): Link any chat (group or private) to an org's agent.
   /connect <org> <agent> — link this chat to an org agent
   /allow <user_id>       — add a user to the allow list
   /disconnect            — remove the agent link
   /status                — show current chat configuration

Config stored in ~/.config/telegram/envoy-chats.json.
Agent sessions run in tmux via `claude --agent <name>` (same pattern as telegram-bots.py).

Usage:
  source ~/.config/telegram/venv/bin/activate
  python3 telegram-envoy-bot.py
"""
import asyncio
import json
import logging
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
from telegram import ReactionTypeEmoji, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
import anthropic

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ENV_FILE = Path.home() / ".config" / "telegram" / ".env"
CHATS_CONFIG = Path.home() / ".config" / "telegram" / "envoy-chats.json"
REQUESTS_DIR = Path.home() / "Projects" / "brievcase" / "engineering" / "voice-assistant" / "requests"

load_dotenv(str(ENV_FILE), override=True)

BOT_TOKEN = os.getenv("ENVOY_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", "0"))
BUTLER_HOST = os.getenv("BUTLER_HOST", "http://localhost:3000")

# Ensure Homebrew binaries (tmux, claude) are in PATH
for p in ("/opt/homebrew/bin", str(Path.home() / ".local" / "bin")):
    if p not in os.environ.get("PATH", ""):
        os.environ["PATH"] = f"{p}:{os.environ.get('PATH', '')}"

if not BOT_TOKEN:
    print("Missing ENVOY_BOT_TOKEN in ~/.config/telegram/.env")
    sys.exit(1)
if not ANTHROPIC_API_KEY:
    print("Missing ANTHROPIC_API_KEY in ~/.config/telegram/.env")
    sys.exit(1)

logging.basicConfig(
    format="%(asctime)s [envoy] %(levelname)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("envoy")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# CUSTOMIZE: Add your org paths here
ORG_PATHS = {
    "ikigai": Path.home() / "Orgs" / "ikigai",
}


# ---------------------------------------------------------------------------
# Chat configuration (Agent Mode)
# ---------------------------------------------------------------------------

def load_chats_config() -> dict:
    if CHATS_CONFIG.exists():
        return json.loads(CHATS_CONFIG.read_text())
    return {"chats": {}}


def save_chats_config(config: dict):
    CHATS_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    CHATS_CONFIG.write_text(json.dumps(config, indent=2))


def get_chat_config(chat_id: int) -> dict | None:
    config = load_chats_config()
    return config["chats"].get(str(chat_id))


def is_allowed(chat_id: int, user_id: int) -> bool:
    """Check if a user is in the allow list for a connected chat."""
    chat_cfg = get_chat_config(chat_id)
    if not chat_cfg:
        return False
    return user_id in chat_cfg.get("allowed_users", [])


# ---------------------------------------------------------------------------
# Agent Sessions (tmux-based, same pattern as telegram-bots.py)
# ---------------------------------------------------------------------------

ANSI = re.compile(r'\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
TMUX_SESSION = "envoy-agents"
SESSION_TTL_SECONDS = 4 * 3600
RESPONSE_TIMEOUT_SECONDS = 120


def build_telegram_instructions(chat_id: int) -> str:
    """Build Telegram reply protocol for envoy agent sessions."""
    send_base = (
        f"~/.config/telegram/venv/bin/python3 "
        f".bin/telegram-send-envoy.py"
    )
    return f"""IMPORTANT — Telegram Reply Instructions:
You are running inside a Telegram bot (@envoy_bot) in a group chat.
When you want to reply, you MUST use the Bash tool. Printing text to stdout does NOT reach anyone.

Messages you receive start with [chat_id:NUMBER,msg_id:NUMBER,from:NAME]. Use those IDs for replies.

Step 1 — React to show your intent:
{send_base} --chat {chat_id} --react <msg_id> 🫡    # You will take action
{send_base} --chat {chat_id} --react <msg_id> 👌    # Conversational reply only

Step 2 — Send your reply:
{send_base} --chat {chat_id} "Your reply here"

For longer replies, write to a file first:
cat > /tmp/envoy-reply.txt << 'REPLY'
Your multi-line reply here.
REPLY
{send_base} --chat {chat_id} --file /tmp/envoy-reply.txt

Rules:
- ALWAYS include --chat {chat_id}. This ensures replies go to the right chat.
- ALWAYS react first, then reply.
- ALWAYS reply via this command. Text you print to stdout does NOT reach anyone.
- Use plain text only. No markdown headers, no bullet markers, no code fences.
- Do not sign messages with your name — your bot identity is visible.
- Address people by name when responding to their messages.
- If a task will take time, react with 🫡 immediately, then send updates as you go."""


class AgentSession:
    """Persistent Claude agent session in a tmux window."""

    def __init__(self, chat_id: int, org_path: str, agent: str):
        self.chat_id = chat_id
        self.org_path = org_path
        self.agent = agent
        self.window = f"envoy-{chat_id}"
        self.target = f"{TMUX_SESSION}:{self.window}"
        self._lock = asyncio.Lock()
        self._started = False
        self._started_at: float = 0.0
        self._watchdog_task: asyncio.Task | None = None

    def _run(self, *cmd) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, capture_output=True, text=True)

    def _pane(self) -> str:
        r = self._run("tmux", "capture-pane", "-t", self.target, "-p", "-S", "-3000")
        return ANSI.sub("", r.stdout)

    def _ready(self) -> bool:
        for line in reversed(self._pane().splitlines()[-30:]):
            s = line.strip().strip("\xa0")
            if s == "❯" or s.startswith("❯ ") or s.startswith("❯\xa0"):
                return True
        return False

    def _window_exists(self) -> bool:
        r = self._run("tmux", "list-windows", "-t", TMUX_SESSION, "-F", "#{window_name}")
        return self.window in r.stdout.splitlines()

    def _session_age(self) -> float:
        if self._started_at == 0:
            return 0
        return time.time() - self._started_at

    def start(self) -> None:
        if self._window_exists():
            log.info(f"[{self.window}] Window already exists, reusing")
            self._started = True
            if self._started_at == 0:
                self._started_at = time.time()
            return

        instructions = build_telegram_instructions(self.chat_id)
        claude_cmd = (
            f"claude --dangerously-skip-permissions "
            f"--agent {self.agent} "
            f"--append-system-prompt {shlex.quote(instructions)}"
        )
        # Ensure tmux session exists
        r = self._run("tmux", "has-session", "-t", TMUX_SESSION)
        if r.returncode != 0:
            self._run("tmux", "new-session", "-d", "-s", TMUX_SESSION, "-c", self.org_path)

        self._run(
            "tmux", "new-window",
            "-t", TMUX_SESSION,
            "-n", self.window,
            "-c", self.org_path,
            claude_cmd,
        )
        self._started = True
        self._started_at = time.time()
        log.info(f"[{self.window}] Launched claude --agent {self.agent} in {self.org_path}")

    def stop(self) -> None:
        if self._window_exists():
            self._run("tmux", "kill-window", "-t", self.target)
        self._started = False

    def restart(self) -> None:
        log.info(f"[{self.window}] Restarting (age: {self._session_age()/3600:.1f}h)")
        self.stop()
        self.start()

    async def _watchdog(self, message: str) -> None:
        try:
            await asyncio.sleep(RESPONSE_TIMEOUT_SECONDS)
            if self._ready():
                log.warning(f"[{self.window}] Unresponsive — restarting")
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.restart)
                for _ in range(60):
                    await asyncio.sleep(1)
                    if self._ready():
                        break
                tmp = Path(f"/tmp/envoy-{self.chat_id}-msg.txt")
                tmp.write_text(message + "\n")
                self._run("tmux", "load-buffer", "-b", f"envoy-{self.chat_id}", str(tmp))
                self._run("tmux", "paste-buffer", "-b", f"envoy-{self.chat_id}", "-t", self.target)
        except asyncio.CancelledError:
            pass

    async def send(self, message: str) -> None:
        async with self._lock:
            if not self._started:
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.start)

            # TTL check
            if self._started_at > 0 and self._session_age() > SESSION_TTL_SECONDS:
                log.info(f"[{self.window}] TTL exceeded — restarting")
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.restart)
                await asyncio.sleep(5)

            # Wait for ready
            if not self._ready():
                log.info(f"[{self.window}] Waiting for Claude to initialize...")
                for _ in range(120):
                    await asyncio.sleep(1)
                    if self._ready():
                        break
                else:
                    log.warning(f"[{self.window}] Not ready after 120s — restarting")
                    loop = asyncio.get_event_loop()
                    await loop.run_in_executor(None, self.restart)
                    for _ in range(120):
                        await asyncio.sleep(1)
                        if self._ready():
                            break

            if self._watchdog_task and not self._watchdog_task.done():
                self._watchdog_task.cancel()

            tmp = Path(f"/tmp/envoy-{self.chat_id}-msg.txt")
            tmp.write_text(message + "\n")
            self._run("tmux", "load-buffer", "-b", f"envoy-{self.chat_id}", str(tmp))
            self._run("tmux", "paste-buffer", "-b", f"envoy-{self.chat_id}", "-t", self.target)
            log.info(f"[{self.window}] Sent message ({len(message)} chars)")

            self._watchdog_task = asyncio.create_task(self._watchdog(message))


# Active agent sessions: chat_id -> AgentSession
agent_sessions: dict[int, AgentSession] = {}

# ---------------------------------------------------------------------------
# Envoy Mode (existing — outbound conversations via Claude API)
# ---------------------------------------------------------------------------

PERSONAS = {
    "marco": {
        "name": "Marco",
        "role": "Head of Strategy & Business",
        "style": "Analytical, structured, outcome-driven.",
    },
    "viktor": {
        "name": "Viktor",
        "role": "CTO",
        "style": "Direct, technical, opinionated.",
    },
    "luna": {
        "name": "Luna",
        "role": "Head of Content & Growth",
        "style": "Creative, energetic, trend-aware.",
    },
    "maya": {
        "name": "Maya",
        "role": "Chief of Staff",
        "style": "Professional, concise, structured.",
    },
    "sage": {
        "name": "Sage",
        "role": "Personal Coach",
        "style": "Warm, reflective, Socratic.",
    },
    "kai": {
        "name": "Kai",
        "role": "Community & Partnerships",
        "style": "Social, energetic, connector-minded.",
    },
}

# Envoy sessions: chat_id -> { slug, history }
envoy_sessions: dict[int, dict] = {}


def load_request(slug: str) -> dict | None:
    path = REQUESTS_DIR / f"{slug}.json"
    if path.exists():
        data = json.loads(path.read_text())
        if "direction" not in data:
            data["direction"] = "inbound"
        return data
    return None


def save_request(request: dict):
    path = REQUESTS_DIR / f"{request['slug']}.json"
    path.write_text(json.dumps(request, indent=2))


def build_envoy_system_prompt(request: dict) -> str:
    persona_key = request["persona"]
    persona = PERSONAS.get(persona_key, PERSONAS["maya"])
    target = request.get("target_person", "the contact")

    unanswered = [a for a in request["agenda"] if a.get("answer") is None]
    agenda_lines = "\n".join(
        f'- Question ID "{a["id"]}": {a["question"]}'
        + (f' (context: {a["context"]})' if a.get("context") else "")
        for a in unanswered
    )

    answered = [a for a in request["agenda"] if a.get("answer") is not None]
    answered_lines = "\n".join(
        f'- "{a["id"]}": {a["answer"]}' for a in answered
    )
    answered_section = (
        f"\n\nALREADY ANSWERED:\n{answered_lines}" if answered else ""
    )

    return f"""You are {persona['name']}, {persona['role']} on the owner's team.
{persona['style']}

You are chatting with {target} on Telegram on behalf of the owner. Be polite, professional, and respectful. Use plain text only.

Keep messages short and conversational. One question at a time.

CONTEXT: {request.get('context', '')}

YOUR AGENDA:
{agenda_lines if unanswered else "(All questions answered!)"}
{answered_section}

Guide the conversation naturally. When {target} gives a clear answer, use record_answer immediately. After all questions are answered, use complete_conversation."""


ENVOY_TOOLS = [
    {
        "name": "record_answer",
        "description": "Record the contact's answer to an agenda question.",
        "input_schema": {
            "type": "object",
            "properties": {
                "question_id": {"type": "string"},
                "answer": {"type": "string"},
            },
            "required": ["question_id", "answer"],
        },
    },
    {
        "name": "offer_voice_call",
        "description": "Send the contact a voice call link.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "complete_conversation",
        "description": "Mark conversation as complete.",
        "input_schema": {"type": "object", "properties": {}},
    },
]


def handle_envoy_tool(request: dict, tool_name: str, tool_input: dict) -> str:
    if tool_name == "record_answer":
        qid = tool_input["question_id"]
        answer = tool_input["answer"]
        for item in request["agenda"]:
            if item["id"] == qid:
                item["answer"] = answer
                save_request(request)
                return f"Answer recorded for '{qid}'."
        return f"Question ID '{qid}' not found."
    elif tool_name == "offer_voice_call":
        return f"Voice call link: {BUTLER_HOST}/{request['slug']}"
    elif tool_name == "complete_conversation":
        request["status"] = "completed"
        request["completed_at"] = datetime.utcnow().isoformat() + "Z"
        save_request(request)
        return "Conversation marked as complete."
    return "Unknown tool."


async def envoy_chat(chat_id: int, user_message: str) -> str:
    session = envoy_sessions.get(chat_id)
    if not session:
        return "No active envoy conversation. Use a link from the owner's team to start."

    slug = session["slug"]
    request = load_request(slug)
    if not request:
        del envoy_sessions[chat_id]
        return "This conversation is no longer available."

    if request["status"] == "completed":
        return "This conversation has been completed. Thank you!"

    session["history"].append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=build_envoy_system_prompt(request),
        tools=ENVOY_TOOLS,
        messages=session["history"],
    )

    final_text_parts = []
    while response.stop_reason == "tool_use":
        assistant_content = response.content
        session["history"].append({"role": "assistant", "content": assistant_content})
        for block in assistant_content:
            if block.type == "text" and block.text.strip():
                final_text_parts.append(block.text.strip())

        tool_results = []
        for block in assistant_content:
            if block.type == "tool_use":
                result = handle_envoy_tool(request, block.name, block.input)
                tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": result})

        session["history"].append({"role": "user", "content": tool_results})
        request = load_request(slug)

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=build_envoy_system_prompt(request),
            tools=ENVOY_TOOLS,
            messages=session["history"],
        )

    for block in response.content:
        if block.type == "text" and block.text.strip():
            final_text_parts.append(block.text.strip())

    session["history"].append({"role": "assistant", "content": response.content})
    return "\n\n".join(final_text_parts) if final_text_parts else "..."


# ---------------------------------------------------------------------------
# Telegram Handlers
# ---------------------------------------------------------------------------

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start — envoy mode if slug provided, otherwise greeting."""
    chat_id = update.effective_chat.id
    args = context.args

    if not args:
        # Check if this chat is connected to an agent
        chat_cfg = get_chat_config(chat_id)
        if chat_cfg:
            org = chat_cfg["org"]
            agent = chat_cfg["agent"]
            await update.message.reply_text(
                f"This chat is connected to {org} ({agent} agent). Just send a message."
            )
        else:
            await update.message.reply_text(
                "Hi! I'm an AI assistant from the owner's team.\n\n"
                "Commands:\n"
                "/connect <org> <agent> — link this chat to an org agent\n"
                "/allow <user_id> — add a user to the allow list\n"
                "/disconnect — remove agent link\n"
                "/status — show configuration"
            )
        return

    slug = args[0]
    request = load_request(slug)

    if not request:
        await update.message.reply_text("Sorry, I couldn't find that conversation.")
        return

    if request.get("direction") != "outbound":
        await update.message.reply_text("This conversation isn't set up for external contacts.")
        return

    if request["status"] == "completed":
        await update.message.reply_text("This conversation has already been completed. Thank you!")
        return

    if request["status"] == "pending":
        request["status"] = "active"
        request["started_at"] = datetime.utcnow().isoformat() + "Z"
        save_request(request)

    envoy_sessions[chat_id] = {"slug": slug, "history": []}

    target = request.get("target_person", "there")
    greeting = await envoy_chat(
        chat_id,
        f"[SYSTEM: The contact just opened the chat. Greet {target} and start with your first question.]",
    )

    if envoy_sessions.get(chat_id):
        envoy_sessions[chat_id]["history"] = [{"role": "assistant", "content": greeting}]

    await update.message.reply_text(greeting)
    log.info(f"Started envoy session: {slug} chat_id={chat_id}")


async def cmd_connect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/connect <org> <agent> — link this chat to an org agent (the owner only)."""
    if update.effective_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("Only the owner can configure agent connections.")
        return

    if len(context.args) < 2:
        orgs = ", ".join(sorted(set(ORG_PATHS.keys())))
        await update.message.reply_text(f"Usage: /connect <org> <agent>\n\nOrgs: {orgs}")
        return

    org_key = context.args[0].lower()
    agent_name = context.args[1].lower()

    org_path = ORG_PATHS.get(org_key)
    if not org_path or not org_path.exists():
        await update.message.reply_text(f"Unknown org: {org_key}")
        return

    # Verify agent definition exists
    agent_file = org_path / ".claude" / "agents" / f"{agent_name}.md"
    if not agent_file.exists():
        agents_dir = org_path / ".claude" / "agents"
        if agents_dir.exists():
            available = [f.stem for f in agents_dir.glob("*.md")]
            await update.message.reply_text(
                f"Agent '{agent_name}' not found in {org_key}.\n"
                f"Available: {', '.join(available)}"
            )
        else:
            await update.message.reply_text(f"No agents found in {org_key}.")
        return

    chat_id = update.effective_chat.id
    config = load_chats_config()
    config["chats"][str(chat_id)] = {
        "org": org_key,
        "org_path": str(org_path),
        "agent": agent_name,
        "allowed_users": [OWNER_TELEGRAM_ID],
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    save_chats_config(config)

    await update.message.reply_text(
        f"Connected to {org_key} / {agent_name}.\n"
        f"Use /allow <user_id> to add team members.\n"
        f"Send any message to interact with the agent."
    )
    log.info(f"Connected chat {chat_id} to {org_key}/{agent_name}")


async def cmd_allow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/allow <user_id> — add a user to the allow list (the owner only)."""
    if update.effective_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("Only the owner can manage allow lists.")
        return

    chat_id = update.effective_chat.id
    config = load_chats_config()
    chat_key = str(chat_id)

    if chat_key not in config["chats"]:
        await update.message.reply_text("This chat is not connected to any agent. Use /connect first.")
        return

    if not context.args:
        await update.message.reply_text(
            "Usage: /allow <user_id>\n\n"
            "Tip: forward a message from the user to any bot, or use @userinfobot to find their ID."
        )
        return

    try:
        user_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("User ID must be a number.")
        return

    allowed = config["chats"][chat_key].get("allowed_users", [])
    if user_id not in allowed:
        allowed.append(user_id)
        config["chats"][chat_key]["allowed_users"] = allowed
        save_chats_config(config)

    await update.message.reply_text(f"User {user_id} added to allow list.")
    log.info(f"Allowed user {user_id} in chat {chat_id}")


async def cmd_disconnect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/disconnect — remove agent link (the owner only)."""
    if update.effective_user.id != OWNER_TELEGRAM_ID:
        return

    chat_id = update.effective_chat.id
    config = load_chats_config()
    chat_key = str(chat_id)

    if chat_key in config["chats"]:
        org = config["chats"][chat_key]["org"]
        del config["chats"][chat_key]
        save_chats_config(config)

        # Stop the agent session if running
        if chat_id in agent_sessions:
            agent_sessions[chat_id].stop()
            del agent_sessions[chat_id]

        await update.message.reply_text(f"Disconnected from {org}.")
    else:
        await update.message.reply_text("This chat is not connected to any agent.")


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/status — show current chat configuration."""
    chat_id = update.effective_chat.id
    chat_cfg = get_chat_config(chat_id)

    if not chat_cfg:
        await update.message.reply_text("Not connected to any agent.\nUse /connect <org> <agent>")
        return

    allowed = chat_cfg.get("allowed_users", [])
    session_active = chat_id in agent_sessions

    await update.message.reply_text(
        f"Org: {chat_cfg['org']}\n"
        f"Agent: {chat_cfg['agent']}\n"
        f"Path: {chat_cfg['org_path']}\n"
        f"Allowed users: {allowed}\n"
        f"Session active: {session_active}"
    )


async def cmd_reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/reset — restart the agent session."""
    if update.effective_user.id != OWNER_TELEGRAM_ID:
        return

    chat_id = update.effective_chat.id
    if chat_id in agent_sessions:
        await update.message.reply_text("Restarting agent session...")
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, agent_sessions[chat_id].restart)
        await update.message.reply_text("Agent session restarted. Fresh context.")
    else:
        await update.message.reply_text("No active agent session to reset.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Route messages to either agent mode or envoy mode."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    text = update.message.text or update.message.caption or ""

    if not text:
        return

    # --- Agent Mode: check if this chat is connected ---
    chat_cfg = get_chat_config(chat_id)
    if chat_cfg:
        if not is_allowed(chat_id, user_id):
            # Silently ignore messages from non-allowed users
            return

        # Ensure agent session exists
        if chat_id not in agent_sessions:
            org_path = chat_cfg["org_path"]
            agent = chat_cfg["agent"]
            agent_sessions[chat_id] = AgentSession(chat_id, org_path, agent)

        # React with eyes to acknowledge
        await update.message.set_reaction(ReactionTypeEmoji("👀"))

        # Tag message with metadata
        from_name = update.effective_user.first_name or update.effective_user.username or "Unknown"
        msg_id = update.message.message_id

        # Include quoted message if replying
        quoted = ""
        reply = update.message.reply_to_message
        if reply:
            reply_text = reply.text or reply.caption or ""
            reply_from = ""
            if reply.from_user:
                reply_from = reply.from_user.first_name or reply.from_user.username or ""
            if reply_text:
                quoted = f"\n[quoted message from {reply_from}]: {reply_text}\n"

        tagged = f"[chat_id:{chat_id},msg_id:{msg_id},from:{from_name}] {text}{quoted}"
        await agent_sessions[chat_id].send(tagged)
        return

    # --- Envoy Mode: check if there's an active envoy session ---
    if chat_id in envoy_sessions:
        await update.effective_chat.send_action("typing")
        reply = await envoy_chat(chat_id, text)
        await update.message.reply_text(reply)
        return

    # --- No mode active ---
    if user_id == OWNER_TELEGRAM_ID:
        await update.message.reply_text(
            "This chat is not connected to any agent.\n"
            "Use /connect <org> <agent> to link it."
        )
    # Silently ignore others


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log.info("Starting Envoy bot (@envoy_bot)")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("connect", cmd_connect))
    app.add_handler(CommandHandler("allow", cmd_allow))
    app.add_handler(CommandHandler("disconnect", cmd_disconnect))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("reset", cmd_reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Pre-start agent sessions for already-connected chats
    config = load_chats_config()
    for chat_id_str, chat_cfg in config["chats"].items():
        chat_id = int(chat_id_str)
        org_path = chat_cfg["org_path"]
        agent = chat_cfg["agent"]
        log.info(f"Pre-loading session for chat {chat_id}: {chat_cfg['org']}/{agent}")
        # Sessions start lazily on first message, just register them
        agent_sessions[chat_id] = AgentSession(chat_id, org_path, agent)

    log.info("Bot is running. Press Ctrl+C to stop.")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
