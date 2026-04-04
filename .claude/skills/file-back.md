# /file-back — Save conversation analysis back into the wiki

After a conversation that produced useful analysis, file the results back into the wiki as a permanent page.

## Trigger

User runs `/file-back` or asks to save analysis/output back into the wiki.

## Steps

1. **Identify the content** to file back. Ask the user what from this conversation should be saved, or use context if obvious.

2. **Determine destination** — one of:
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
