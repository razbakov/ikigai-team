## Orgs vs Projects

The framework splits your work across two top-level categories.

### Layout

- **`~/Orgs/<org-name>/`** — multi-repo organisations, governance, partnerships, contacts, ops. **No application code lives here.**
- **`~/Projects/<project-name>/`** — single-repo code projects. Even if a project belongs to an org, the code lives here.

This separation matters because:
- Org logbooks accumulate slowly (one daily review, a few contacts a week). Code repos churn fast.
- Mixing them puts large binaries / build artifacts next to long-form governance prose.
- Agents working in code mode shouldn't see all your contact and partnership history; agents working on partnerships shouldn't pull in code dependencies.

### Creating a new organisation

When asked to "create an organisation":

1. **Find the related project under `~/Projects/`** and extract all context (README, CLAUDE.md, product docs, brand assets).
2. **Create `~/Orgs/<OrgName>/`** using the `/org-coach` skill on autopilot — it produces the full S3 structure with governance, domains, roles, and agent definitions.
3. **Always create fresh, org-specific agents** (Coordinator, Autopilot, and domain-specific roles). NEVER reuse the framework agents (Maya/Viktor/Luna/Marco/Kai/Sage) inside an org — they have different context and responsibilities per org.
4. **Add a routing agent** to your private brain repo's `.claude/agents/` that `cd`s to the org and runs a session there with the org's coordinator agent.

The dispatch infrastructure (e.g. envoy bot) auto-discovers orgs from `~/Orgs/` — no registration needed.

### Interactive product development sessions

When the work is interactive product development (editing code, iterating on UI, debugging), open a new session inside the project folder (`cd ~/Projects/<project> && claude`) for proper context. Don't try to do code work from the brain or org session — the session needs to be physically inside the code repo for git, build tools, and project-local CLAUDE.md to work.

For non-interactive tasks (e.g. "ship a small fix"), dispatch a routing agent that runs from inside the project folder.
