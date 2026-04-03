# CLAUDE.md

## What This Is
A knowledge base about AI usage and workflows in economics, business,
and social science research. Raw sources live in raw/. You compile
and maintain a structured wiki in wiki/.

## Core Rules
- I don't edit wiki/ directly. You write and maintain it.
- Every wiki page gets YAML frontmatter (title, tags, sources, date_updated)
- Use [[wikilinks]] for internal links (Obsidian format)
- Maintain wiki/index.md as master table of contents with brief summaries
- Maintain wiki/concepts/index.md listing all concept pages
- When summarizing sources, always link back to the original in raw/

## Vault Structure
- raw/articles/ — clipped web articles (.md)
- raw/papers/ — PDFs, TeX files
- raw/images/ — local images
- wiki/summaries/ — one summary per source
- wiki/concepts/ — concept pages synthesizing across sources
- output/ — query results, slides, charts

## Workflow
1. Read sources in raw/
2. Create summaries in wiki/summaries/
3. Identify cross-cutting concepts, create pages in wiki/concepts/
4. Link everything, maintain indexes
5. File query outputs back into the wiki when valuable
