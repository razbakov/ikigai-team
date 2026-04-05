#!/usr/bin/env python3
"""
Send a Telegram message via the Envoy bot (@ai_lifeos_bot).

Used by Claude agent sessions spawned by the Envoy bot to reply to chats.

Usage:
  python3 telegram-send-envoy.py --chat <chat_id> "Your message"
  python3 telegram-send-envoy.py --chat <chat_id> --file /tmp/reply.txt
  python3 telegram-send-envoy.py --chat <chat_id> --react <msg_id> 🫡

Requires: ENVOY_BOT_TOKEN in ~/.config/telegram/.env
"""
import asyncio
import os
import re
import sys
from pathlib import Path

ENV_FILE = Path.home() / ".config" / "telegram" / ".env"


def load_env(path):
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def get_bot():
    from telegram import Bot

    token = os.environ.get("ENVOY_BOT_TOKEN")
    if not token:
        print("Missing ENVOY_BOT_TOKEN in .env")
        sys.exit(1)
    return Bot(token=token)


def strip_markdown_escapes(text: str) -> str:
    return re.sub(r'\\([_*\[\]()~`>#+=|{}.!\-])', r'\1', text)


async def react_to_message(chat_id: int, message_id: int, emoji: str):
    from telegram import ReactionTypeEmoji

    bot = get_bot()
    await bot.set_message_reaction(
        chat_id=chat_id,
        message_id=message_id,
        reaction=[ReactionTypeEmoji(emoji)],
    )
    print(f"Reacted to msg {message_id} with {emoji}")


async def send_message(chat_id: int, text: str):
    bot = get_bot()
    text = strip_markdown_escapes(text)
    has_html = bool(re.search(r'<[a-z]+[ />]', text, re.IGNORECASE))
    parse_mode = "HTML" if has_html else None
    chunks = [text[i:i + 4000] for i in range(0, len(text), 4000)]
    for chunk in chunks:
        try:
            await bot.send_message(chat_id=chat_id, text=chunk, parse_mode=parse_mode)
        except Exception:
            await bot.send_message(chat_id=chat_id, text=chunk)
    print(f"Sent to chat {chat_id}: {text[:80]}...")


def main():
    load_env(ENV_FILE)

    if "--chat" not in sys.argv:
        print("Usage: telegram-send-envoy.py --chat <chat_id> <message>")
        sys.exit(1)

    chat_idx = sys.argv.index("--chat")
    chat_id = int(sys.argv[chat_idx + 1])

    # React mode
    if "--react" in sys.argv:
        react_idx = sys.argv.index("--react")
        msg_id = int(sys.argv[react_idx + 1])
        emoji = sys.argv[react_idx + 2]
        asyncio.run(react_to_message(chat_id, msg_id, emoji))
        return

    # File mode
    if "--file" in sys.argv:
        file_idx = sys.argv.index("--file")
        file_path = sys.argv[file_idx + 1]
        message = Path(file_path).read_text().strip()
    else:
        skip = set()
        for flag in ("--chat", "--react"):
            if flag in sys.argv:
                fi = sys.argv.index(flag)
                skip.add(fi)
                skip.add(fi + 1)
        remaining = [a for i, a in enumerate(sys.argv[1:], 1) if i not in skip]
        message = " ".join(remaining)

    if not message:
        print("No message provided")
        sys.exit(1)

    asyncio.run(send_message(chat_id, message))


if __name__ == "__main__":
    main()
