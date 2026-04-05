# ikigai-team

The dream team. 6 AI agents for solo founders — 6 specialized agents that operate autonomously within clear domains, using Sociocracy 3.0 governance patterns.

## The Team

| Agent | Role | Personality |
|-------|------|------------|
| **Maya** | Chief of Staff | ISTJ — reliable, systematic, detail-oriented |
| **Viktor** | CTO | INTJ — strategic, efficient, quality-focused |
| **Luna** | Head of Content & Growth | ENFP — imaginative, enthusiastic, trend-aware |
| **Marco** | Head of Strategy & Business | ENTJ — analytical, decisive, results-focused |
| **Sage** | Personal Coach | INFJ — insightful, empathetic, purposeful |
| **Kai** | Community & Partnerships | ESFJ — warm, social, connector-minded |

## Quick Start

```bash
# Install the setup skill
claude install-skill https://github.com/razbakov/ikigai-team/tree/main/skills/setup-ikigai

# Run the setup wizard
claude "/setup-ikigai"
```

The wizard asks ~10 questions (name, projects, integrations) and generates the full 6-agent team.

## Architecture

```
You (Commander)
  |
  v
Maya (dispatch + track)
  |
  +---> Viktor (code)
  +---> Luna (blog, SEO, social)
  +---> Marco (OKRs, biz dev)
  +---> Sage (wellbeing)
  +---> Kai (contacts, events)
  |
  +---> Project Agents (route to org coordinators)
```

You're the human in the loop — strategic decisions, public face, approvals. Maya dispatches everything else. She never handles tasks directly.

## Website

The landing page and guides are built with Nuxt 4. To run locally:

```bash
pnpm install
pnpm dev
```

## Repository Structure

```
app/                    # Nuxt 4 website (landing page, guides, skills browser)
content/                # Markdown content (guides, skill descriptions)
public/images/agents/   # Agent avatar images
templates/              # Installable framework templates (.hbs)
  agents/               # 6 agent templates + project router
  infra/                # Telegram bot scripts (parameterized)
  ops/                  # Contact CRM template
  profile/              # profile.md, now.md templates
  CLAUDE.md.hbs         # Operational rules template
skills/
  setup-ikigai/         # Interactive setup wizard skill
docs/                   # Framework documentation
```

## Key Principles

- **Agents never handle tasks outside their domain** — they hand off
- **Maya never does work directly** — only dispatches and tracks
- **S3 governance** — consent-based decisions, domain delegation
- **Skills are independent** — install only what you need

## License

MIT
