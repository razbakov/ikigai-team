## Contacts

How to capture and maintain people in the operating system.

### File layout

- One directory per person: `contacts/<firstname-lastname>/contact.md`
- Frontmatter: `name`, `type`, `projects`, `location`, `contact`, `status`
- Chat text logs: kept in the repo
- Media attachments (photos, voice notes, files): stored at `~/Local/<your-org>/contacts/<name>/`, not in the git repo (binary bloat, privacy)

### When adding a new contact

Spawn a subagent to research the person online (LinkedIn, Twitter, GitHub, public profile) and enrich the contact file with:
- Background and current role
- Mutual connections / overlap with the Commander's projects
- Most recent public activity (posts, talks, releases)
- Anything that would change how the Commander would approach them

This is mandatory — manual contact creation without enrichment leaves stubs that get forgotten.

### Meetings belong in the calendar

Any meeting referenced in a contact file must also be a Google Calendar event. Don't track meetings in markdown alone — calendar is the single source of truth for who-met-whom-when.

### Per-instance rules

Spelling preferences (e.g. specific umlauts, transliterations), language defaults, and preferred contact methods belong in your private CLAUDE.md, not in the framework.
