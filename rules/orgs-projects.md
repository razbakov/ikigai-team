## Orgs vs Projects

The framework splits your work across two top-level categories.

### Layout

- **`~/Orgs/<org-name>/`** — multi-repo organisations, governance, partnerships, contacts, ops. **No application code lives here.**
- **`~/Projects/<project-name>/`** — single-repo code projects. Even if a project belongs to an org, the code lives here.

### When do I need which?

**Decision rule: every code thing starts as a Project. Promote to "Project + Org" only when there's something to govern beyond the code.**

| Scenario | What you create |
|---|---|
| New code repo, solo, you're the only person | `~/Projects/<name>/` only. No org needed. |
| Code repo + you're starting to negotiate partnerships, manage contributors, run events around it | Add `~/Orgs/<OrgName>/` alongside. Code stays in Projects, governance moves to Orgs. |
| Service business with no product code (yet) | `~/Orgs/<name>/` only. The "code" is per-client work in their own repos. |
| Community / event series with no code | `~/Orgs/<name>/` only. Code can come later as a Project. |
| Fork or experiment of an existing code project | `~/Projects/<name>/`. Don't make an org for an experiment. |

If the answer to "do other people care about this beyond the code?" is no → Project. If yes → also Org.

### Why the split exists

Three concrete reasons, in order of how often they bite:

1. **Different cadence.** Code churns hourly (commits, builds, deploys). Governance churns weekly (decisions, partnerships, KR rollups). Putting them in one repo means daily reviews live next to `node_modules/` deletions, and `git log` becomes useless for either purpose.
2. **Different agents, different context.** When the engineering agent opens a code repo it should see code, types, and tests — not a 200-row contacts directory. When the community agent opens an org it should see partnerships and ops — not 50k lines of UI components. The split keeps each agent's context relevant. Mixed repos force every agent to filter noise.
3. **Different blast radius.** Code repos get cloned, forked, deployed, sometimes open-sourced. Orgs hold contacts, NDAs, partner emails, financial notes. Accidentally pushing an org as public is a privacy incident; pushing a project as public is normal. Hard separation prevents the accident.

### Promotion trap

Don't promote to an Org because something *feels* important. The threshold is "are there relationships, contacts, partnerships, or recurring events to track?" — not size, not revenue, not how much you care about it. A solo blog with no contacts stays a Project forever. A weekly meetup with five organizers becomes an Org from day one even if it has zero code.

### Multi-repo orgs

A single Org can list many Projects in its registry. WeDance-shaped orgs typically end up with 3–5 code repos (web app, mobile app, marketing site, internal tools) — each one is a separate `~/Projects/<name>/`, and the Org's `CLAUDE.md` references all of them in its project registry. Each Project's `CLAUDE.md` `@`-imports the framework but doesn't need to know about the Org.

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
