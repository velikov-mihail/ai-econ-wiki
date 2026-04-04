# /maintain — Full wiki maintenance pass

Orchestrates ingest detection, lint, and index rebuild in one command.

## Trigger

User runs `/maintain` or asks for a maintenance pass.

## Steps

1. **Detect pending sources**: Run `python tools/find_new_sources.py`. Report how many raw files lack summaries. List them.

2. **Run full lint**: Execute all checks from the `/lint` skill (frontmatter validation, orphan detection, index drift, mkdocs nav drift, duplicate detection). Print the structured report.

3. **Rebuild indexes**: Run `python tools/build_index.py --write` to ensure indexes match current files.

4. **Summarize findings**: Print a concise dashboard:
   ```
   === Maintenance Summary ===
   Pending sources:  N
   Errors:           N
   Warnings:         N
   Info:             N
   Indexes:          rebuilt
   ```

5. **Offer next steps**:
   - If pending sources exist: "Run `/ingest` to process them one-by-one."
   - If errors found: list the top issues and suggest fixes.
   - If everything clean: "Wiki is healthy."

6. **Log the operation** in `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] maintain | Maintenance pass
   - Pending sources: N
   - Errors: N
   - Warnings: N
   - Indexes rebuilt: yes
   ```

7. **Commit** index changes if any were made, with message: `Maintain: rebuild indexes`

## Key Rules

- This skill is **read-mostly** — it reports and rebuilds indexes, but does NOT auto-process pending sources or auto-fix lint errors (those require `/ingest` and `/lint --fix` respectively).
- Keep the output scannable — use the dashboard format above.
- Run this weekly or after adding new sources to `raw/`.
