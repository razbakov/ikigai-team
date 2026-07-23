## Content & Publishing

Generic publishing rules. Per-domain rules (which languages to translate to, which platforms to cross-post to, your specific URL structure) belong in your private CLAUDE.md.

### Visual assets

- **Hero images** for blog posts and long-form content must be generated using `/image-from-gemini`. Never copy thumbnails from other sources or reuse stock images for primary hero positions.
- **YouTube thumbnails** must be Gemini-generated, not HTML-rendered. HTML + headless Chrome thumbnails look generic and hurt click-through. The paired blog post's hero image is usually the right source if it exists; otherwise generate a new one with Gemini.
- Resize thumbnails to 1280px wide with `sips --resampleWidth 1280` before uploading.

### Fact-check market claims before any external-facing deliverable

AI-generated business copy looks authoritative but is routinely wrong on specifics. Before any external-facing deliverable ships (pitch site, sales deck, landing page, sponsor pitch, investor memo, press release, partnership proposal), verify:

- **Specific numbers** — practitioner counts, market sizes, customer counts, competitor counts. Source it (industry report, government statistic, primary survey), use a defensible range, or omit the number. Round-number claims like "5,000" or "10K" without a citation are the most common failure.
- **"We're the first / no one does X / the only Y" superlatives** — search before claiming. There is almost always a small competitor that's been operating quietly for a decade; the false superlative destroys credibility the first time the reader recognises it.
- **Named competitors and peer references** — verify each named business is still operating, at the address, doing the thing. Referencing a venue that closed years ago, or a product that pivoted, telegraphs "didn't do the research."
- **Historical claims about other businesses** — opening dates, founder names, prices, when they pivoted. Web search before commit.

When the data isn't verifiable, write the copy without the specific:

- ❌ "5,000 active practitioners in Munich"
- ✅ "a thousand-plus active practitioners across Munich's school network"
- ❌ "the only authentic Cuban bar in Munich"
- ✅ "Munich has a few Cuban-themed cocktail bars, but no Cuban cultural home"

Don't add a disclaimer ("approximate", "as of writing"). Don't ship the specific claim if you can't source it. The reader meeting the document for the first time will not give the benefit of the doubt — they will catch the one detail that's wrong and discount the whole pitch.

### Cross-posting

- DEV.to posts must include `canonical_url` in frontmatter pointing back to the original.
- Each cross-post platform has its own metadata requirements — document them in the per-domain rules of your private repo, not here.

### Ticketing links (TicketTailor)

- When sharing a TicketTailor event anywhere (website CTA, flyer, socials, DM, email), link to the **ticket-list checkout URL** — `https://www.tickettailor.com/checkout/view-event/id/<id>/chk/<chk>/` — **not** the branded event-page short link (`buytickets.at/<store>/<id>`). The checkout link opens straight to the list of tickets, saving the visitor a click.
- The checkout URL is returned as the occurrence's `url` field from the API (and shown per occurrence in the dashboard).

### Frontmatter discipline

- All `last_updated` / `updated_at` fields must be actual datetimes (e.g. `2026-04-07 02:30`), never relative phrases like "today" or "just now". Future readers (including agents) cannot resolve relative timestamps.

### After deployment, update CLAUDE.md

After any deployment or URL change, update the relevant CLAUDE.md (PostHog table, Project Path Registry, deploy notes — wherever the URL is canonicalised) before reporting done. Stale URL references cascade into broken playbooks.

### Vercel auto-deploy is mandatory

When deploying to Vercel, always connect the GitHub repo and ensure auto-deploy on push works. Verify by pushing a commit and confirming the build succeeds remotely. Never leave a project relying on manual `vercel deploy` only — manual deploys silently rot.
