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

### Tasks vs personal action items

- **GitHub Issues** (Control Center board) = delegated or cross-session work. Anything an agent picks up. Anything that needs an S3 body, a PR, a deliverable.
- **Google Tasks** = personal actions only the Commander does (call, send, buy, read). No agent involvement, no PR, no deliverable.

If a task needs an agent, it's a GitHub issue. Never a Google Task.
