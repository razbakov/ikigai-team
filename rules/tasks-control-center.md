## Tasks & Control Center

How work gets tracked across all your projects without dropping anything.

### All tasks live as GitHub issues

- All tasks live as **GitHub issues**, tracked on a **Project v2 board** (the "Control Center"). Never add task items to markdown files. Never use Notion for tasks.
- Each task issue is created in the **project's own repo** (matching the Project Path Registry in your private CLAUDE.md), labeled with one `agent:*` label, and added to the Control Center board with `gh project item-add <project-number> --owner <owner> --url <issue-url>`.
- Every task issue must have an **S3 body** (Sociocracy 3.0):
  - **Tension** — what hurts or feels off
  - **Driver** — the underlying need driving this work
  - **Requirement** — what success looks like
  - **Response Options** — possible ways forward

### Board columns

`Inbox → To do → In progress → To review → Done`

- Don't move to "To review" if the issue or its PR has unresolved threads.
- "To review" means deliverables are in the PR — the PR body must link to every artifact (files, URLs, deployed preview).
- Prefer closing issues via `Closes #N` in PR bodies (auto-closes on merge and moves the card to Done).

### Keep the issue current while you work on it

Whenever you work on an issue (Linear, GitHub, or any tracker), the issue itself must show where the work stands — the Commander reads the tracker, not your session.

- **Status:** move it when the work moves. Starting → In Progress. PR opened or result delivered → the "delivered, waiting for review" state (e.g. In Review / To review). Blocked → say so on the issue. Never set the final Done state unless the instance config allows it.
- **Comment when needed** — when there is something a reader of the issue would want: the PR or deliverable link, a finding that changes the scope or plan, a blocker and what unblocks it, a decision you made and why, or what is left undone. Keep it short and factual.
- **Don't comment** routine progress noise ("started", "still working") — the status already says that.
- Do this as part of the work, in the same session, not as a follow-up.

### Tasks vs personal action items

- **GitHub Issues** (Control Center board) = delegated or cross-session work. Anything an agent picks up. Anything that needs an S3 body, a PR, a deliverable. **This is the system queue.**
- **Google Tasks** = personal actions only the Commander does (call, send, buy, read). No agent involvement, no PR, no deliverable. **This is a presentation layer, not a queue** (see next section).

If a task needs an agent, it's a GitHub issue. Never a Google Task.

### Tasks/Calendar are a presentation layer, not a system queue

The Commander is human; they can hold ~5 commitments per day. The team is not human; it can hold infinite parallel state. Therefore:

- **Google Tasks and Google Calendar** are *today's curated slice* the Commander has explicitly consented to. They are the presentation layer between the system and the human.
- **The system queue is GitHub Issues + `ops/`.** Anything the team is tracking, anything in flight, anything not yet consented-to lives there.
- **A hard daily cap on actionable items** (calendar blocks + tasks combined, excluding sleep/meals/standing meetings) prevents flooding. The cap is per-Commander config in private CLAUDE.md; default suggestion: 5.
- **Items only enter Tasks/Calendar via the daily consent gate** (see `daily-review.md`). No agent, no skill, no daily-review process may auto-add items — they may only *propose* during the morning consent step.
- **Items removed at end-of-day go back to the system queue**, not to a hidden personal backlog. The next day's consent gate re-competes for the cap slots. No silent backlog growth.

This rule fixes the failure mode where Tasks becomes a dumping ground for everything anyone (the Commander, agents, daily-review, follow-ups) thinks should happen, until the volume guarantees nothing gets done. In sociocracy terms: the Commander cannot have objections to items they never consented to, and labeling unconsented items "missed follow-ups" against any reliability KR is a category error — the leak is on the team, not on the Commander.
