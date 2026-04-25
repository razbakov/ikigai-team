## Skills

Skills are reusable workflows that any session can invoke via `/<skill-name>`. They live in a separate, shareable repo — not in any single project's `.claude/skills/`.

### Where skills live

- All skills must be **shareable** and **reusable** by other users.
- Save them to a dedicated skills repo (e.g. `~/.local/share/skill-mix/sources/skills@<your-handle>/`), not to any specific project's `.claude/skills/` directory.
- Project-local skills are an anti-pattern: they cannot be discovered by agents working in other contexts.

### What skills must NOT contain

- **No config.** No URLs, no chat IDs, no API endpoints, no project-specific path mappings, no per-org IDs.
- Config belongs in the relevant org or project CLAUDE.md.
- Skills must stay generic and reusable across instances.

If a skill needs config, it should reference it abstractly (e.g. "the Control Center project number — see your private CLAUDE.md") rather than hardcode a value.

### Naming and review

- Before publishing a new skill, always review it with `/skill-creator`.
- Skill names should be verbs or noun-phrases that describe what they do (e.g. `daily-review`, `process-inbox`, `image-from-gemini`).
- A skill SKILL.md must specify: trigger conditions, step-by-step process, inputs/outputs, templates used, integration points.

A well-written skill lets anyone (human or AI) reproduce the workflow from scratch without having met the original author.
