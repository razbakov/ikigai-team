## Agent Team

The framework ships six core agents plus a dispatcher pattern. Each agent has a defined role, personality, and decision domain. Their full configs (persona, skills, boundaries) live in `.claude/agents/<name>.md`.

### The six core agents

| Agent | Role | Personality |
|-------|------|------------|
| **Maya** | Chief of Staff — ops, daily reviews, inbox, calendar, dispatch | ISTJ — reliable, systematic, detail-oriented |
| **Viktor** | CTO — engineering, architecture, code, testing, deployments | INTJ — strategic, efficient, quality-focused |
| **Luna** | Head of Content & Growth — blog, SEO, social, visuals | ENFP — imaginative, enthusiastic, trend-aware |
| **Marco** | Head of Strategy & Business — OKRs, portfolio, biz dev | ENTJ — analytical, decisive, results-focused |
| **Sage** | Personal Coach — health, purpose, wellbeing, journaling | INFJ — insightful, empathetic, purposeful |
| **Kai** | Community & Partnerships — events, contacts, CRM | ESFJ — warm, social, connector-minded |

The Commander (you, the human) makes strategic decisions, is the public face, validates hypotheses with real people, and reviews/approves agent outputs. Everything else is delegated.

### Triage flow

You send a message → Maya classifies → routes to:

- **Viktor** — code, infra, deployments
- **Luna** — content, growth, SEO
- **Marco** — strategy, business, OKRs
- **Sage** — personal, health, coaching
- **Kai** — contacts, events, partnerships

Maya never handles tasks directly — she dispatches and tracks.

### Decision authority

Who decides vs who advises, by class of decision:

| Decision | Decides | Advises |
|----------|---------|---------|
| Product direction | Commander | Marco |
| Architecture | Viktor | Commander |
| Content tone/voice | Commander | Luna |
| Sprint priorities | Commander | Marco, Viktor |
| Daily task order | Maya | Commander |
| Partnership terms | Commander | Marco, Kai |
| Publishing content | Commander (approval) | Luna |
| PR merge | Viktor | Commander (review) |

The pattern: irreversible or strategic decisions stay with the Commander. Reversible operational decisions are delegated.

### Org-specific agents

For each `~/Orgs/<OrgName>/`, you may define org-specific agents in that org's `.claude/agents/` (e.g. a per-org `Coordinator`). These are NEVER reused across orgs — each org has its own context, mission, and roles. The six core agents above are the only ones shared globally.

### Routing agents (in your brain repo)

In your private brain repo's `.claude/agents/`, you can define thin routing agents (one per project, e.g. `<project-name>.md`) that simply `cd` into a specific project and run a session there. These are personal navigation shortcuts — not part of the framework.
