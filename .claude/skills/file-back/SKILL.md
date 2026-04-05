---
description: "Save conversation analysis back into the wiki. Args: concept | summary | output (optional target type)"
user_invocable: true
---

# /file-back — Save conversation analysis back into the wiki

After a conversation that produced useful analysis, file the results back into the wiki as a permanent page.

## Trigger

User runs `/file-back` or asks to save analysis/output back into the wiki.

## Arguments

- `concept` — File as a new or updated concept page in `wiki/concepts/`
- `summary` — File as a new summary in `wiki/summaries/`
- `output` — File as an output artifact in `output/`
- *(no argument)* — Ask the user or infer from context

## Steps

1. **Identify the content** to file back. Ask the user what from this conversation should be saved, or use context if obvious.

2. **Determine destination** — if a target type was passed as an argument, use it. Otherwise pick one of:
   - **New concept page** in `wiki/concepts/` — if the analysis synthesizes across multiple sources into a new theme
   - **Update existing concept page** — if it extends an existing concept
   - **New summary** in `wiki/summaries/` — if it's a summary of a specific source
   - **Output file** in `output/` — if it's a query result, chart, or one-off analysis that doesn't fit the wiki structure

3. **Format the page** with proper:
   - YAML frontmatter (`title`, `tags`, `date_updated`, and `sources` if applicable)
   - [[wikilinks]] to related summaries and concepts
   - Attribution: note that this was generated from a conversation/query

4. **Update indexes**:
   - If new concept: add to `wiki/concepts/index.md`
   - If new summary: add to category landing page and run `python tools/build_index.py --write`
   - Cross-link from related existing pages where natural

5. **Log the operation** in `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] file-back | Title
   - Destination: wiki/concepts/foo.md (or output/foo.md)
   - Type: new concept / updated concept / new summary / output
   ```

6. **Commit** with message: `File back: <title>`

## Key Rules

- Always confirm the destination and scope with the user before writing.
- For `output/` files, use descriptive filenames (e.g., `output/agent-comparison-2026-04.md`).
- Don't duplicate content that already exists in the wiki — link to it instead.
