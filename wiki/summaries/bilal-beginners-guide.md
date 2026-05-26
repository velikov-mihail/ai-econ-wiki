---
title: "A Beginner's Guide to Claude Code for (Non-Technical) Academics"
tags: [summary, foundations-setup, claude-code, project-organization, subagents]
sources:
  - "[[raw/articles/A Beginner's Guide to Claude Code for (Non-Technical) Academics.md]]"
date_updated: 2026-05-26
date_published: 2026-05-22
---

- **Author/Source**: Mushtaq Bilal, X long-form post (8,000+ words)
- **Original**: [https://x.com/MushtaqBilalPhD/status/2057786613795639582](https://x.com/MushtaqBilalPhD/status/2057786613795639582)

- **Key Ideas**
  - An omnibus, three-chapter consolidation of Bilal's Claude Code series for non-technical academics. Chapter 1 = getting started (the [[claude-code-101-bilal|101]] material); Chapter 2 = organizing longer projects (the [[claude-code-102-bilal|102]] material); Chapter 3 = subagents, chaining, MCP connectors, hooks, scheduled tasks, and Git for version control.
  - Core mental model: "instead of you bringing your files to an AI app in the browser, you bring the AI into the folder containing all your data." Claude Code can read, edit, and create files — the chatbot UI cannot.
  - **CLAUDE.md as a project constitution** — a global file at the project root covers role, standards, writing style, and critique style; local CLAUDE.md files in subfolders (`Literature`, `Chapters`, `Data`, `Notes`, `Correspondence`) carry task-specific conventions. Claude Code reads both when working inside a subfolder.
  - **Skills** are markdown files for one specific task (e.g., extracting actionable items from Zoom transcripts), distinct from CLAUDE.md (project-wide context) and from auto-memory (Claude's own internal notes). All three layers compose to produce better responses.
  - **Plan Mode vs. Custom Slash Commands**: Plan Mode for complex one-off tasks (3+ steps, multiple subfolders, lengthy outputs); custom slash commands stored in `.claude/commands/*.md` for repetitive tasks. Rule of thumb: do not automate something you have not done manually at least four times.
  - **Subagents** have their own context window and their own instructions file in `.claude/agents/`. Critical property: a subagent's reading and reasoning stay inside its own context, so the main session does not get "context clutter." Concrete subagent roster for academics: Literature Reviewer, Citation Checker, Methodology Auditor, "Reviewer 2." Iron rule: subagents must never edit drafts — they only produce report files.
  - **Chained subagents as a research pipeline**: worked example is a four-stage systematic review pipeline (`Importer-Deduplicator` → `TA-Screener` → `Full-Text Screener` → `Data Extractor`). Each stage emits a numbered CSV that the next stage consumes. Build and test one subagent at a time before chaining.
  - **MCP connectors** in the Customize menu bring Zoom transcripts, Google Drive drafts, Zotero citations, and PubMed/arXiv into the same session — but the author warns against connecting apps that hold confidential or unpublished data.
  - **Hooks and scheduled tasks**: pre-edit safety hook that snapshots a chapter before edits; weekly literature-scan scheduled task that hands new PubMed papers to a Literature Reviewer subagent. Never set up hooks or scheduled tasks that delete files.
  - **Git for project-wide version control**: contrasts Word's per-file history with Git's whole-project snapshots. Commit after every meaningful work session, write descriptive commit messages, and treat Git as version control — not as a backup.

- **Summary**

This is the most complete single-document onramp Bilal has published — an 8,000-word, three-chapter consolidation aimed squarely at humanities and qualitative researchers who have used ChatGPT in a browser but never touched a terminal. Chapter 1 establishes the basic "bring the AI into your folder" model, walks through install, the first session, and CLAUDE.md (manual vs. automatic creation, with sections for Role, Standards, Writing Style, Critique Style). Chapter 2 reprises the nested-CLAUDE.md pattern for multi-year projects with the now-canonical `Literature / Chapters / Data / Notes / Correspondence` folder taxonomy, and adds Plan Mode and custom slash commands as the two complementary tools for one-off complex tasks vs. repeated routines.

Chapter 3 is the most substantive addition relative to the earlier 101/102 threads: it builds up subagents from first principles (separate context window, separate instruction file, never edit source files), then chains them into a four-stage systematic-review pipeline as the headline worked example. It closes with MCP connectors, hooks, scheduled tasks, and Git, packaging the operational pieces that distinguish a long-running research project from a one-off chat. The repeated "What Not to Do" sections function as a compact set of Iron Rules — do not delegate original argument; do not duplicate global and local CLAUDE.md instructions; do not chain a subagent that has not been tested individually; do not write a slash command for a task you have not done four times manually; do not treat Git as backup.

- **Relevance to Economics Research**

For empirical economists, the systematic-review pipeline example transposes directly onto literature surveys, referee-response workflows, and replication audits. The subagent design discipline — single specific task, never edit source files, separate context — is a transferable pattern for any project that mixes long-running drafts, data work, and correspondence. The "never delegate original argument" guardrail aligns with the broader [[concepts/domain-expertise-vs-ai-skills|domain-expertise]] framing: agents accelerate the labor-intensive parts of scholarship without replacing the researcher's judgment about argument and evidence. For coauthored projects, the nested-CLAUDE.md pattern plus a `Correspondence/` subfolder is a concrete operational template for [[concepts/revise-and-resubmit|R&R workflows]].

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/claude-md-files]]
  - [[concepts/claude-code-skills]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/mcp-protocol]]
  - [[concepts/version-control-research]]
  - [[concepts/context-management]]
  - [[concepts/domain-expertise-vs-ai-skills]]

- **Related Summaries**
  - [[summaries/claude-code-101-bilal]]
  - [[summaries/claude-code-102-bilal]]
  - [[summaries/codex-101-bilal]]
  - [[summaries/codex-102-bilal]]
  - [[summaries/agentic-everything]]
  - [[summaries/starter-templates]]
