---
title: "Claude Code 104: Building Your AI-Powered Research Management System (Bilal)"
tags: [summary, foundations-setup, claude-code, obsidian, research-management]
sources:
  - "[[raw/articles/Claude Code 104 Building Your AI-Powered Research Management System.md]]"
date_updated: 2026-05-26
date_published: 2026-05-25
---

- **Author/Source**: Mushtaq Bilal, X thread (fourth installment in the Claude Code for academics series)
- **Original**: [https://x.com/MushtaqBilalPhD/status/2058888916858544472](https://x.com/MushtaqBilalPhD/status/2058888916858544472)

- **Key Ideas**
  - End-to-end recipe for a personal AI-powered research management system using **Obsidian + Claude Code + Web Clipper**. One-time setup; afterwards the system absorbs new material with a single prompt.
  - **Two-folder architecture inside one Obsidian vault** (`MyWiki/`): a `raw/` inbox folder for everything you collect (PDFs, clipped webpages, notes) and a `wiki/` folder where Claude Code builds bidirectionally-linked synthesized notes.
  - **Obsidian as a graphic interface for a folder**: anything in the vault folder is also in Obsidian, and vice versa. The Obsidian double-bracket wikilink convention makes the wiki navigable.
  - **Obsidian Web Clipper** (browser extension) captures webpages as markdown into the `raw/` folder. Critical setup step: in the Clipper's default template, change Note location from `Clippings` to `raw` so clips land in the right place automatically.
  - **Two instruction files** govern Claude Code's behavior:
    - `AGENTS.md` — project-wide instructions (researcher's field, topic, source types, organization scheme, linking conventions, citation rules, an explicit "never edit/move/delete anything in raw/" rule).
    - `Index.md` — the wiki's table of contents, organized around main themes; updated whenever new notes are added.
  - **Bootstrap prompt** after setup: *"Read AGENTS.md, look at everything in the raw folder and build the initial wiki structure."* Claude Code then reads the raw inbox and writes the organized, cross-linked wiki.
  - The article includes copy-paste prompt templates for both `AGENTS.md` and `Index.md` creation, with placeholders for field, topic, source types, and themes. Both prompts instruct Claude Code to ask up to 3–5 clarifying questions before writing.
  - "What Not to Do" rules: do not pre-organize the raw folder (let Claude do it); do not skip reading the generated `AGENTS.md` and `Index.md`; treat `AGENTS.md` as a living document that must evolve with the project.

- **Summary**

This fourth installment is more operational than conceptual: it documents a specific stack (Obsidian vault + Claude Code + Obsidian Web Clipper) and the exact instruction files (`AGENTS.md`, `Index.md`) that make the stack behave as a self-organizing knowledge base. The architecture mirrors what is canonical in this very wiki — a `raw/` inbox folder is never edited by the agent, and a `wiki/` folder is where synthesis happens with bidirectional double-bracket wikilinks. The Web Clipper closes the input loop so that webpages can be captured with one click into the same place where PDFs and notes already live.

Two design choices distinguish this from the simpler "one folder, one CLAUDE.md" pattern in [[claude-code-101-bilal|101]]. First, the read/write separation: by convention, the agent only writes to `wiki/` and only reads from `raw/`. Second, the explicit Index.md as a living navigation hub, separate from the project-level instructions in `AGENTS.md`. Note the AGENTS.md naming convention — this matches the cross-tool standard also used by OpenAI Codex (see [[codex-101-bilal]]), positioning the system as agent-agnostic rather than Claude-specific.

- **Relevance to Economics Research**

This is the canonical recipe for any economist who wants a long-running knowledge base that survives across projects: a referee-correspondence wiki, a literature-review-in-progress, a working-paper notes system, or a course prep vault. The read-only-raw / write-only-wiki separation is the right discipline for a project that accumulates clipped Federal Reserve speeches, working papers from NBER, and personal notes — all in markdown, all locally owned, all queryable by an agent. The two-file instruction pattern (`AGENTS.md` + `Index.md`) is more lightweight than the nested-CLAUDE.md pattern from [[claude-code-102-bilal|102]] and fits a single-vault use case better than a multi-subfolder dissertation project. For economists with many parallel projects, both patterns compose: one vault per project, with its own AGENTS.md.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/claude-md-files]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/claude-code-101-bilal]]
  - [[summaries/claude-code-102-bilal]]
  - [[summaries/bilal-beginners-guide]]
  - [[summaries/codex-101-bilal]]
  - [[summaries/codex-102-bilal]]
