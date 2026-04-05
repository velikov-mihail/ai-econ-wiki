---
title: "Claude Code Series (Part 6): Video Explainer of Claude Code in Action"
tags: [summary, claude-code-skills, project-exploration, claude-md, directory-organization, progress-logs]
sources:
  - "[[raw/articles/Claude Code Series part 6 Video Explainer of Claude Code in Action.md]]"
date_updated: 2026-04-05
date_published: 2026-01-14
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-series-part-6-video-explainer](https://causalinf.substack.com/p/claude-code-series-part-6-video-explainer)

- **Key Ideas**
  - Starting a project with Claude Code follows a sequence: exploration (let Claude scan the directory), documentation (README.md + CLAUDE.md), rule-setting, reorganization, and progress logging.
  - CLAUDE.md is the "seatbelt" -- a persistent instruction file containing rules like never delete data, never delete programs, stay in this folder, use a legacy folder, copy don't move.
  - Chat sessions are ephemeral; if they crash, all conversational context is lost. Progress logs (timestamped markdowns) serve as "autosave" so the next Claude instance can reconstruct context.
  - Claude Code autonomously explores project directories -- finding files, reading timestamps, summarizing manuscripts -- without being told where anything is.
  - Reorganizing a messy 10-year-old project (150+ files) into a clean directory structure took about 30 minutes of conversation, with Claude executing all file operations.

- **Summary**

Cunningham records a 30-minute video walkthrough of starting a Claude Code session on an old (2016) research project about Texas HB2 abortion clinic closures. The video demonstrates four steps. First, exploration: Claude Code scans the directory without guidance, finding 105 data files, Stata do-files, R scripts, LaTeX tables, and manuscripts, and reconstructing the project timeline from file timestamps. Second, documentation: Cunningham has Claude create a README.md and a CLAUDE.md containing five iron-clad rules (never delete data, never delete programs, stay in this folder, use a legacy folder, copy don't move). Third, reorganization: after discovering a contradiction between the rules (copy-only) and the need to move files into a legacy folder, Cunningham and Claude negotiate an amendment allowing a one-time move. Claude then reorganizes 150+ files into a clean hierarchy (code/, data/, output/, docs/, legacy/, log/). Fourth, progress logging: Claude writes timestamped log entries documenting everything accomplished, so future sessions can pick up where the current one left off.

The post emphasizes the collaborative, conversational nature of working with Claude Code -- Cunningham did not have the solution worked out in advance; they figured it out together through dialogue. He also notes the tension: Claude moved over a hundred files in seconds, which is powerful but could be dangerous without rules and version control.

- **Relevance to Economics Research**

Provides a concrete, step-by-step template for how an economist can onboard an old or messy research project into a Claude Code workflow. The CLAUDE.md rules and progress-log pattern are directly transferable to any empirical project. The emphasis on legacy folders and copy-only operations addresses the social scientist's cardinal concern about data preservation.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/claude-md-files]]
  - [[concepts/agentic-workflows]]
  - [[concepts/context-management]]
  - [[concepts/version-control-research]]
  - [[concepts/ai-for-non-coders]]

- **Related Summaries**
  - [[summaries/cc-changed-how-i-work-5]]
  - [[summaries/cc-series-7-beautiful-decks]]
  - [[summaries/cc-changed-how-i-work-1]]
  - [[summaries/real-claude-md]]
  - [[summaries/ai-project-folders]]
