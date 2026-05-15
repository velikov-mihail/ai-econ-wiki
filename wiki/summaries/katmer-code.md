---
title: "KatmerCode: Claude Code inside Obsidian"
tags: [summary, claude-code-skills, obsidian, peer-review, citation-verification]
sources:
  - "[[raw/articles/Claude Code inside Obsidian — with academic research skills, inline diff editing, and MCP support..md]]"
date_updated: 2026-05-15
date_published: 2026-05
---

- **Author/Source**: Halil Kaan Canan, GitHub
- **Original**: [https://github.com/hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)

- **Key Ideas**
  - Obsidian plugin that runs Claude Code as a sidebar chat panel using the [Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk). Built for researchers who write in Obsidian and want AI assistance for literature review, citation checking, manuscript editing, and peer review without leaving the editor.
  - **Inline diff editing**: word-level track changes directly in the editor — red strikethrough for removals, green underline for additions, accept (✓) or undo (✕) per change.
  - Connects to any **MCP server** configured in `~/.claude.json`. Supports `/compact`, tabs, session resume, streaming — everything Claude Code terminal can do.
  - **Seven academic research skills as slash commands**:
    - `/peer-review` — 8-criteria evaluation (originality, argument, literature, methodology, …), radar chart, section-by-section feedback.
    - `/cite-verify` — checks every reference against CrossRef, Semantic Scholar, OpenAlex; flags mismatches in author/year/title; tests claim faithfulness.
    - `/lit-search` — parallel queries across arXiv, Semantic Scholar, PubMed, OpenAlex; dedupes and ranks.
    - `/citation-network` — interactive citation graph (vis.js) with timeline view.
    - `/research-gap` — identifies temporal, methodological, thematic, and application gaps, scored by feasibility and impact.
    - `/journal-match` — recommends target journals from your reference profile.
    - `/abstract` — generates abstracts in 5 formats (structured, narrative, graphical, highlights, social media).
  - Reports render as HTML inside Obsidian, with tables and charts. Longer skills (peer review with cite verification, gap analysis) parallelize via subagents.
  - Honest framing: "research aids, not oracles" — `/peer-review` is not a substitute for a human reviewer; `/cite-verify` may falsely flag valid refs when database coverage is thin. Outputs are a map, not the territory.

- **Summary**

KatmerCode is the most credible attempt yet to put Claude Code inside the editor most academics already write in. The plugin is desktop-only (it shells out to the local Claude Code CLI) and exposes the agent as a sidebar chat plus a slash-command surface for seven academic skills. The inline diff UX is the standout feature: instead of a separate "show changes" preview, the model's edits are word-level track-changes you accept or reject inside your live document — closer to the Word/Google Docs collaboration pattern than the file-overwrite pattern most Claude Code users are used to.

The skills themselves are workmanlike but well-bounded. `/cite-verify` hits real bibliographic APIs (CrossRef, Semantic Scholar, OpenAlex) rather than relying on the model's parametric memory — directly addressing the citation-hallucination problem central to many AI-assisted research tools. `/journal-match` and `/research-gap` are the most distinctive contributions; both lean on the cited reference profile rather than abstract semantic similarity, which produces more grounded recommendations.

- **Relevance to Economics Research**

For economists already using Obsidian for note-taking and literature management (a sizable subset), KatmerCode collapses the toolchain: PDFs annotated in Obsidian, drafts written in Obsidian, peer review and citation verification run in the same sidebar. The inline-diff editing pattern is also a useful design reference for anyone building research workflows that need lower friction than file-overwrite. For empirical economists less invested in Obsidian, `/cite-verify`'s database-first verification protocol is portable to other workflows (the same APIs work from any agent).

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/ai-peer-review]]
  - [[concepts/citation-hallucination]]
  - [[concepts/literature-review-ai]]
  - [[concepts/ide-and-terminal]]

- **Related Summaries**
  - [[summaries/ars-claude-code]]
  - [[summaries/coarse-ink]]
  - [[summaries/haaland-reviewer]]
  - [[summaries/cc-series-44-four-criteria-referee]]
