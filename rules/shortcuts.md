## Shortcuts (meta commands)

These are the universal verbal shortcuts the Commander uses. Personal shortcuts (specific people, specific projects) belong in your private CLAUDE.md.

### Framework meta-shortcuts

- **`rule: <text>`** — decide whether the rule is project-specific or global, add it to the appropriate CLAUDE.md (project CLAUDE.md, org CLAUDE.md, or `~/.claude/CLAUDE.md`), and execute it immediately.

- **`learned?`** — analyse the process that just happened, extract lessons/insights, and add them to the project README.

- **`new skill`** — analyse the current conversation to extract the repeatable process that was just performed, then create a SKILL.md that captures it: trigger conditions, step-by-step process, inputs/outputs, templates used, integration points. The skill should let anyone (human or AI) reproduce the workflow from scratch.

- **`save`** — commit all changes, update all relevant docs and maps (CLAUDE.md project registries, now.md, strategy trackers, metrics, etc.) to reflect the current state. This is a checkpoint — make sure nothing is lost or out of sync. After committing, always ask "skills?" — evaluate whether the process just performed should become a reusable skill. If yes, create it; if not, say so briefly and move on.

- **`plan it`** — check if current output/research is saved to a file. If not, save it first. Then create a GitHub issue in the appropriate project repo (agent label + S3 body) and add it to the Control Center board.

- **`health`** — run a full systems health check: agent bots, Telegram bots, scheduled tasks, MCP servers, auth tokens, dispatch surface. Report as a pass/fail status board.

- **`sync`** — check git status of all projects and orgs (from your private Project Path Registry), commit any uncommitted changes with descriptive messages, and push all repos.

### "remind me" — pick the right surface

When the Commander says "remind me ...":

- **Has a specific start time** (meeting, appointment, hard block, recurring time slot) → **Google Calendar** via `gog cal create`. Default 15 minutes; full context in `--description=`.
- **Action item without a fixed doing-time** (a call to make, errand, follow-up, quick send, reading) → **Google Tasks** via `gog tasks add`. Use `--due=YYYY-MM-DD` if there's a deadline.

Rules of thumb:

- Never put an untimed action on the Calendar just to "not forget it" — that's what Tasks is for.
- Never put a hard appointment in Tasks — Calendar is the only surface with time-of-day semantics.

### Shortcut authoring guidance

If a shortcut applies only to one specific project, person, or campaign (e.g. "<person-name> email" → open latest email from a specific contact and apply changes to a specific repo), it belongs in your private CLAUDE.md, not in the framework. Framework shortcuts are universal patterns (capture, plan, save, sync, remind) — not specific automations.
