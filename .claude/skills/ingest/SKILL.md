---
description: "Detect and process new raw sources into wiki summaries. Args: --all (skip per-source approval)"
user_invocable: true
---

# /ingest — Process new raw sources into wiki summaries

Detect and process raw sources that don't yet have wiki summaries.

## Trigger

User runs `/ingest` or asks to process new sources.

## Arguments

- `--all` — Process all pending sources without pausing for approval between each one. Still commits each individually. Default (no flag) pauses after each source for user review.

## Steps

1. **Detect pending sources**: Run `python tools/find_new_sources.py` to list raw files without summaries. If nothing pending, report that and stop.

2. **Process one source at a time**. For each pending source:

   a. Read the raw file (from `raw/articles/` or `raw/papers/`).

   b. Create a summary in `wiki/summaries/` following the existing template. Use `wiki/summaries/agentic-everything.md` as the reference template. Every summary must have:
      - YAML frontmatter: `title`, `tags` (first tag is `summary`, second is the category slug), `sources` (wikilink to raw file), `date_updated`, `date_published`
      - Author/Source line with link to original
      - Key Ideas (bullet points)
      - Summary (1–3 paragraphs)
      - Relevance to Economics Research
      - Related Concepts (wikilinks to `concepts/`)
      - Related Summaries (wikilinks to `summaries/`)

   c. Assign to one of the existing categories by tag. Read the canonical list from `tools/categories.json`.

   d. Add the new summary to the appropriate category landing page in `wiki/summaries/`.

   e. Update or create relevant concept pages in `wiki/concepts/` if the source introduces new cross-cutting themes.

   f. **Update `wiki/authors.md`**: Add the new summary under the author's existing heading (alphabetical by first name). If the author doesn't have a heading yet, create one in the correct alphabetical position with their affiliation if known.

   g. Rebuild indexes: `python tools/build_index.py --write` (regenerates `summaries/index.md`, `concepts/index.md`, and `wiki/recent.md`).

   h. Append an entry to `wiki/log.md` (newest first, below the header):
      ```
      ## [YYYY-MM-DD] ingest | Title
      - Source: raw/articles/Filename.md
      - Summary: wiki/summaries/slug.md
      - Concepts updated: list or "none"
      ```

   i. **Show the diff and wait for user approval** before moving to the next source. (Skip this step if `--all` was passed.)

   j. Commit with message: `Add summary: <title>`

3. **After all sources processed** (or user stops):

   a. **Refresh derived pages** — update hardcoded counts and content to match current wiki state:
      - `wiki/index.md` — category summary counts in the Categories section
      - `wiki/visualizations/category-map.md` — summary counts in the mermaid diagram nodes
      - `wiki/visualizations/source-timeline.md` — add any new dated summaries in chronological order, update summary statistics at bottom
      - (`wiki/recent.md` is auto-regenerated in step 2g — no manual update needed.)

   b. Report summary of what was added.

## Key Rules

- Process **one source at a time** — never batch.
- Always match the style and depth of existing summaries.
- Use short slug filenames (e.g., `ai-normal-technology.md`, not the full article title).
- Cross-reference: link new summaries from related existing summaries where natural.
- For PDFs/papers: extract key findings, methodology, and relevance to econ research.
- **Missing URLs**: If a raw source (e.g., a local PDF or presentation) has no discoverable URL, ask the user for one before finalizing the summary. Don't guess or fabricate links. If the user confirms there is no URL, cite it as a local file only.
