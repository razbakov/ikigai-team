---
title: Envoy
description: Let your agents talk to other people on your behalf.
---

Envoy is a single Telegram bot that connects anyone to any of your agents — without giving them access to your full system.

## Two Modes

### Agent Mode — connect a group chat to an agent

You have a Telegram group with your co-founder. You want them to talk to Viktor directly.

> **You:** `/connect wedance coordinator`
>
> **Envoy:** "Connected to wedance / coordinator. Use /allow 123456 to add team members."

Now anyone in that group who is on the allow list can message the agent. The agent runs in your org's context — full tool access, full project knowledge.

> **Co-founder:** "What's the status of the payment flow?"
>
> **Viktor:** "PR #47 is merged. Stripe webhook handler is live on staging. One failing test left — I will fix it today."

### Envoy Mode — outbound conversations on your behalf

You want Marco to interview a potential partner. You create an agenda and share a link.

The partner clicks the link, and Marco introduces himself and works through the agenda naturally — one question at a time, conversational, not a survey. Answers get recorded automatically.

> **Marco:** "Hi Sarah! Alex asked me to chat with you about the SDTV partnership. Mind if I ask a few questions?"
>
> **Sarah:** "Sure!"
>
> **Marco:** "What's your team's biggest challenge with content distribution right now?"

When all questions are answered, Marco marks the conversation complete and you get the results.

## Why This Matters

- Your agents can represent you in conversations while you sleep
- External people get a focused, professional experience — not your whole system
- Every conversation is tracked and recorded
- You control exactly who can talk to which agent

## Setup

During team setup, say yes to Telegram integration. Envoy is included in the bot scripts.

Or set up manually — details in the [repo](https://github.com/razbakov/ikigai-team/blob/main/skills/setup-ikigai/references/scripts/telegram-envoy-bot.py).

## Commands

| Command | Who | What |
|---------|-----|------|
| `/connect <org> <agent>` | You | Link this chat to an org's agent |
| `/allow <user_id>` | You | Add someone to the allow list |
| `/disconnect` | You | Remove the agent link |
| `/status` | Anyone | Show current chat configuration |
