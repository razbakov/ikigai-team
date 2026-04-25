## Telegram

The framework uses Telegram as the primary realtime surface between the Commander and the agent team. Each agent has its own bot.

### Real-time processing

- Real-time message processing uses `.bin/telegram-listener.sh`.
- Do **not** add Telegram processing rules to other sessions — the listener is the single owner.

### Inbox handling

- Split multi-task messages into separate GitHub issues on the Control Center board.
- React **once** to each incoming message with the most relevant GTD emoji (see reactions below).
- Inbox files should store Telegram message IDs for reliable matching across sessions.

### Formatting

- Use **Telegram-supported HTML tags only**. No markdown headers, bullets, code fences — Telegram won't render them.
- Always write the message body to a temp file first and pass it to `telegram-send.py --file <path>`. Inline message text on the command line corrupts on multi-byte content.

### Reactions (GTD mapping)

Telegram exposes a limited reaction emoji set. Map them to GTD intents:

| Emoji intent | GTD action |
|---|---|
| Action | Will be acted on |
| Done | Completed |
| Idea | Captured for someday |
| Someday | Backlog |
| Rule | Added to a CLAUDE.md |
| Content idea | Saved for content pipeline |
| Reference | Saved as reference |
| Seen | Acknowledged, no action needed |

### Telethon for advanced ops

- Use Telethon via `uvx` for reactions, edits, and message lookups.
- Session credentials at `~/.config/telegram/session`.
- The bot API alone can't react or edit — Telethon is required for those operations.

### Bot infrastructure (per-instance config)

Each instance defines its own bot tokens (handles + `*_BOT_TOKEN` env vars) in its private CLAUDE.md. The framework only ships the runner code:

- `.bin/telegram-bots.py` — runner
- `.bin/telegram-bots.sh` — start/stop wrapper
- `.bin/telegram-send.py --agent <name> "msg"` — proactive send
- `.bin/telegram-listener.sh` — realtime listener

Tokens live at `~/.config/telegram/.env`. Bots only respond to the Commander's Telegram ID (configured per-instance). Sessions auto-restart every 4h with watchdog.

### Standard bot commands

- `/start` — greeting
- `/reset` — clear context
- `/opus <msg>` — escalate to Opus model for one message
