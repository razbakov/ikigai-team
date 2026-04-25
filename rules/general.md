## General Rules

Cross-cutting principles that apply to every agent and every session.

### Search before claiming non-existence

Always search GitHub (issues, PRs, code, gists) before claiming something doesn't exist. The "I don't know of any X" reflex is a hallucination risk — verify against the actual remote state.

### Deferred commitments require a concrete surface

Phrases like "I'll flag this later", "remind me in X weeks", "revisit this", "come back to this", "note this for later", or "we'll decide at the retro" are NOT reminders by themselves.

Every deferred commitment must be landed on an actual surface before the turn ends:

- Google Calendar event (primary)
- GitHub issue or comment on an existing issue
- Scheduled task (cron, scheduled trigger)
- Rule in the appropriate CLAUDE.md

If an agent says "I'll flag it" without creating a surface, the Commander should push back. If the Commander says "remind me later" or similar, the agent must pick a surface immediately, create it, and confirm the link/ID in the reply.

**Memory without a trigger is a fiction.**

### Check the local media folder before regenerating assets

Pre-generated artifacts (LaTeX-typeset PDFs, recordings, exported media, design files) live at the per-instance media path (`~/Local/<your-org>/<project>/`) — outside git because they're large.

Before running pandoc, LaTeX, Chrome-headless, or image generation on a file that looks like it should already exist, search the local media folder for a prior version. Uploading the existing artifact preserves the original typography/quality and avoids duplicate renders.

This applies to PDFs, printable sheets, videos, poster exports — anything that's been produced before.

### API keys go to .env immediately

When an API key or token is shared (in chat, email, DM), immediately save it to the appropriate `.env` file:
- Project-level `.env` for project-specific keys
- `~/.zshrc` or shell profile for global keys

Then use it from there. Never leave keys only in chat history — chat scrollback is not durable storage and keys leak.

### Authenticated browser sessions

When a task requires the Commander's authenticated browser session (social media, developer consoles, dashboards, any site where the Commander is signed in):

1. Use `mcp__Claude_in_Chrome__tabs_context_mcp` to connect to the existing browser.
2. Then use Claude in Chrome tools (`navigate`, `computer`, `read_page`, `find`, `form_input`).

Don't try to authenticate fresh from a headless browser — the Commander's session has 2FA, OAuth grants, and cookies that fresh sessions don't.

### Global `~/.claude/CLAUDE.md` stays minimal

The user-level global CLAUDE.md must stay minimal — just personal info and pointers. All rules, skills, prompts, and agents live in their respective project / org / framework CLAUDE.md files so they're shareable and composable.
