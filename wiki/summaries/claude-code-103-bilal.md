---
title: "Claude Code 103 for Academic Researchers (Bilal)"
tags: [summary, foundations-setup, claude-code, subagents, version-control]
sources:
  - "[[raw/articles/Claude Code 103 for Academic Researchers 1.md]]"
date_updated: 2026-05-26
date_published: 2026-05-20
---

- **Author/Source**: Mushtaq Bilal, X thread (third installment in the Claude Code for academics series)
- **Original**: [https://x.com/MushtaqBilalPhD/status/2057033643973865585](https://x.com/MushtaqBilalPhD/status/2057033643973865585)

- **Key Ideas**
  - Third installment of Bilal's Claude Code for academics series, focused on two operationally important topics: **chaining subagents into a research pipeline** and **version control with Git**.
  - **A subagent has three characteristics**: (1) designed for one very specific task; (2) has its own working memory (separate context window); (3) exists as a markdown file on disk. Its separate memory is the point — invoking a subagent mid-session does not clog the main session.
  - **Why chain**: one subagent can only do one task. Chaining lets the output of one feed the input of the next, like a relay race. Worked example: a `First-Drafter` → `Literature-Discoverer` mini-pipeline that turns raw voice-note transcripts into a list of relevant papers.
  - **Headline worked example — a four-stage systematic-review pipeline**:
    - `Importer-Deduplicator` → reads RIS/PubMed/BibTeX files, deduplicates on DOI and title, writes `01_deduplicated.csv`.
    - `TA-Screener` → applies inclusion/exclusion criteria from `protocol.md` to titles/abstracts, marks include/exclude/unclear, writes `02_title_abstract_screen.csv`.
    - `Full-Text Screener` → matches included records to PDFs, applies criteria to full texts, writes `03_fulltext_screen.csv`.
    - `Data Extractor` → pulls predefined fields (population, design, sample size, country, interventions); marks missing fields "Not available"; never extrapolates.
  - **Build-and-test discipline**: build one subagent at a time and verify in Excel before moving to the next. Switch to **Plan Mode** before chaining so Claude shows the orchestration before executing. Iron rule across all stages: subagents must never edit, modify, or delete source files (raw inputs are read-only).
  - **Git for whole-project versioning**: a Word file shows you Monday's version of a single draft; Git shows you Monday's version of the entire project (drafts + data + transcripts). Bilal positions this as the right tool for the realistic case where one Tuesday revision spans drafts, data, and deleted transcripts and needs to be rolled back as a unit.
  - **Three operational Git rules**: (1) write descriptive commit messages — "Updates" is useless after the third time; (2) commit after every meaningful session, not occasionally; (3) Git is *version control*, not *backup* — if the computer crashes, the `.git` history goes with it. Use cloud or external drives for actual backup.
  - **Setup via Claude Code prompts**: *"Set up Git in this folder and create an initial commit with all my current files."* For session-end commits: *"Commit the current state of the project with the note 'Revised Chapter 4, aligned introduction with figure, and added new reading materials.'"* For rollback: *"Show me the last ten commits with their dates and notes,"* then *"Restore the whole project to [Commit ID] and save it as 'Restored Project [Date].'"*

- **Summary**

Episode 103 is where Bilal's beginner-oriented series gets operationally serious. The first half — chaining subagents into a research pipeline — is the most concrete payoff of the entire 101/102/103 arc, because it shows that the conceptual material on CLAUDE.md and subagents in earlier episodes was leading toward something an academic can actually deploy: a four-stage systematic-review pipeline where each stage emits a numbered CSV that the next stage consumes. The build-one-at-a-time discipline is the right craft advice — most chain failures are filename mismatches between stages, and the only way to catch them is to inspect each intermediate file in Excel before wiring the next stage in.

The second half — Git as whole-project version control — is the unusual addition for a non-technical-academic audience. Bilal's framing is unusually clean: it's the camera that takes a snapshot of the *whole* project at a moment in time, not a per-file history like Word's revision pane. The Tuesday-rollback scenario (revise a chapter section, edit a data figure, delete some transcripts) is the right motivating case for why per-file history isn't enough. The three Git rules at the end (descriptive commits, frequent commits, Git ≠ backup) are exactly what most academics get wrong on first contact.

**Relation to other Bilal pieces in this wiki**: this 103 thread is largely the source material for Chapter 3 of the [[bilal-beginners-guide|omnibus Beginner's Guide]]. The omnibus consolidates 101 + 102 + 103 with light editing and adds a Chapter 1 onramp; this 103 is the original, more compact version of the subagent-chaining + Git material.

- **Relevance to Economics Research**

For empirical economists, the four-stage systematic-review pipeline transposes directly to literature-survey work for working papers and R&Rs. The same chain shape applies elsewhere: replication audits (`extract-citations` → `match-to-source-papers` → `verify-tables` → `flag-discrepancies`), referee-response workflows (`parse-referee-report` → `map-to-revision-plan` → `draft-responses`), and any multi-step pipeline that produces numbered intermediate CSVs. The read-only-raw discipline is the right convention for any project that mixes confidential data with agent-generated outputs. The Git portion is more elementary than what most empirical economists already do, but the framing of Git-as-whole-project-snapshot rather than per-file-history is a useful way to explain the tool to qualitative-research coauthors.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/version-control-research]]
  - [[concepts/agentic-workflows]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/bilal-beginners-guide]]
  - [[summaries/claude-code-101-bilal]]
  - [[summaries/claude-code-102-bilal]]
  - [[summaries/claude-code-104-bilal]]
  - [[summaries/codex-102-bilal]]
