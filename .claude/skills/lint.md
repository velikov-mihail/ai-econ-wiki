# /lint — Health-check the wiki

Run diagnostics on the wiki and report issues. Optionally auto-fix mechanical problems.

## Trigger

User runs `/lint` or `/lint --fix`.

## Checks

Run all of the following and classify each finding as **error**, **warning**, or **info**:

### Errors
- **Frontmatter validation**: Run `python tools/validate_frontmatter.py`. Report any missing fields, broken wikilinks, or invalid YAML.
- **Orphan summaries**: Summary files in `wiki/summaries/` that are not listed on any category landing page.
- **Orphan concepts**: Concept files in `wiki/concepts/` that are not listed in `wiki/concepts/index.md`.

### Warnings
- **Zero concept links**: Summaries that don't link to any concept page in their "Related Concepts" section.
- **Index drift**: Files on disk in `wiki/summaries/` or `wiki/concepts/` that don't appear in the corresponding `index.md`. Or index entries pointing to files that don't exist.
- **mkdocs.yml nav drift**: Pages listed in `mkdocs.yml` nav that don't exist on disk, or wiki pages not in the nav.

### Info
- **Pending sources**: Run `python tools/find_new_sources.py` and report count of unprocessed raw files.
- **Duplicate detection**: Run `python tools/find_duplicates.py` and report any flagged pairs.
- **Summary count**: Total summaries, concepts, and categories.

## Output

Print a structured report grouped by severity (errors first, then warnings, then info). Include file paths for each finding.

## `--fix` mode

If the user passes `--fix`, automatically repair these mechanical issues:
- Rebuild indexes via `python tools/build_index.py --write`
- Add orphan summaries to the appropriate category landing page (based on their tags)
- Add orphan concepts to `wiki/concepts/index.md`
- Commit fixes with message: `Lint --fix: <brief description of repairs>`

Do NOT auto-fix content issues (broken wikilinks to non-existent pages, missing frontmatter fields) — report those for manual review.

## Logging

Append a summary to `wiki/log.md`:
```
## [YYYY-MM-DD] lint | Health check
- Errors: N
- Warnings: N
- Info: N
- Auto-fixed: yes/no
```
