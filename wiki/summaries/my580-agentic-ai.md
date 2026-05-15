---
title: "MY580: Agentic AI for Social Science and Data Science Research"
tags: [summary, ai-agents, teaching, agentic-workflows, lse]
sources:
  - "[[raw/articles/MY580 - Agentic AI for Social Science and Data Science Research.md]]"
date_updated: 2026-05-15
date_published: 2026-05
---

- **Author/Source**: Daniel de Kadt (London School of Economics), workshop repo on GitHub
- **Original**: [https://github.com/ddekadt/MY580_agentic_ai/tree/main](https://github.com/ddekadt/MY580_agentic_ai/tree/main)

- **Key Ideas**
  - MY580 is a hands-on workshop at LSE introducing social science and data science researchers to agentic AI through a free, terminal-based coding assistant.
  - Primary tool is **Gemini CLI** (Google's free terminal-based agent as of May 2026), chosen for accessibility — but the principles are vendor-agnostic and apply to Claude Code, Codex, or other agentic assistants.
  - Workshop covers how modern AI agents **plan, use tools, and execute multi-step tasks**, using Python and R as the analysis languages.
  - Recommended IDE is **Positron** (Posit's modern fork of VS Code aimed at data scientists).
  - Pedagogical scaffolding: students get a starter `project_student/` folder with a blank `GEMINI.md` (the Gemini analogue of `CLAUDE.md`) and pre-staged raw data, plus a reference `project_demo/` showing a worked example.
  - Setup is intentionally low-friction: ~10-minute install, only requires a personal Google account for the free tier, runs on any laptop.

- **Summary**

The MY580 workshop materials, authored by Daniel de Kadt at the London School of Economics, package a one-day introduction to agentic AI for social science and data science researchers. Unlike most agentic AI tutorials in the academic-research orbit, which assume Anthropic's Claude Code, MY580 standardizes on **Gemini CLI** specifically because Google's free tier removes the cost barrier for student adoption. The author is explicit that the choice is pragmatic, not ideological: the workshop teaches general principles of agentic AI use, and students with paid Anthropic or OpenAI accounts are encouraged to substitute their preferred tool.

The repo bundles OS-specific setup guides (Windows and macOS), starter and demo project folders, and a workshop slide deck (`MY580_agentic_ai.html`). The split between `project_student/` (a blank `GEMINI.md` plus raw data) and `project_demo/` (a worked Module 4 example) mirrors the increasingly standard pattern in agentic-AI pedagogy: give students a configuration file scaffold, pre-staged data, and a reference implementation they can read but not edit. The choice of Positron as the recommended IDE is notable — it signals that the workshop treats agentic AI as part of a data-science stack, not a pure software-engineering one.

- **Relevance to Economics Research**

MY580 is one of the first agentic-AI workshops at a major social science department (LSE Methodology) and represents how methods training is starting to absorb agentic AI as a core competency rather than an elective. For economists building similar workshops, three design choices are instructive: (1) standardizing on a **free** tool to maximize student access, even at the cost of using a less-capable agent; (2) using a `GEMINI.md` / `CLAUDE.md`-style configuration file as the central pedagogical artifact students fill in themselves; and (3) explicitly framing the workshop as vendor-agnostic principles rather than tool-specific tricks, hedging against the rapid pace of capability change. The pre-staged `data/raw/` pattern and the demo/student folder split are directly reusable for an economics-research equivalent.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-in-education]]
  - [[concepts/claude-code]]
  - [[concepts/domain-expertise-vs-ai-skills]]

- **Related Summaries**
  - [[summaries/agentic-bootcamp-1-aslim-beam]]
  - [[summaries/agentic-bootcamp-2-aslim-beam]]
  - [[summaries/learn-ai-coding-agents]]
  - [[summaries/ai-agents-econ-research]]
  - [[summaries/agentic-everything]]
