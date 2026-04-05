---
title: Telegram Bots
description: Message your agents from your phone. Optional but powerful.
---

Each agent can have a dedicated Telegram bot. You message them directly — they respond with full tool access.

## Why

- Message Maya from your phone while walking
- Send Viktor a bug report from a screenshot
- Drop Kai a voice note about someone you just met
- Get Sage to check in on you during the evening

## Setup

The setup wizard generates Telegram infrastructure if you say yes during `/setup-ikigai`.

Or set up manually:
1. Create bots via [@BotFather](https://t.me/BotFather) on Telegram — one per agent
2. Save tokens to `~/.config/telegram/.env`
3. Start the bot runner: `.bin/telegram-bots.sh`

Detailed setup: see [docs/telegram-setup.md](https://github.com/razbakov/ikigai-team/blob/main/docs/telegram-setup.md) in the repo.

## How It Works

You send a message → bot reacts with 👀 → agent processes → agent replies via the bot.

Sessions auto-restart every 4 hours. If an agent is unresponsive for 2 minutes, it auto-recovers.

## Security

Bots only respond to your Telegram user ID. Everyone else gets "This bot is private."
