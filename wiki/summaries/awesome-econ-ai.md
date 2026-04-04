---
title: "Awesome Econ AI Stuff: AI Skills for Economists"
tags: [summary, ai-tools, skills, economists, open-source, cursor, claude-code]
sources:
  - "[[raw/articles/Awesome Econ AI Stuff - AI Skills for Economists.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---

- **Author/Source**: Antonio Mele (and contributors), hosted at meleantonio.github.io/awesome-econ-ai-stuff/
- **Original**: [https://meleantonio.github.io/awesome-econ-ai-stuff/](https://meleantonio.github.io/awesome-econ-ai-stuff/)

## Key Ideas

- A curated, open-source collection of **18+ ready-to-use AI skills** organized across 8 categories, designed to plug into AI coding assistants like Claude Code, Cursor, Codex, and Gemini CLI.
- Skills cover the full economics research workflow: **Analysis** (panel data in Python, IV/DiD/RDD in R, Stata regressions), **Communication** (Beamer presentations, publication-quality visualizations), **Data** (API fetching from FRED/World Bank, Stata data cleaning), **Engineering** (code refactoring, git workflows, spec-driven development), **Ideation** (research question generation), **Literature** (lit review assistant), **Theory** (general equilibrium model builder, LaTeX economic models), and **Writing** (paper drafting, LaTeX tables).
- Skills are installed by cloning Git repositories into your AI tool's skills directory (e.g., `~/.claude/skills/`) and invoked via slash commands or natural language.
- The collection is tool-agnostic: works with Claude Code, Cursor, Codex, and Gemini CLI.
- Setup takes under 2 minutes per skill: install the AI tool, clone the skill repo, invoke via slash command.
- Notable specialized skills include `general-equilibrium-model-builder` (Walrasian GE models with Julia computation) and `r-econometrics` (IV, DiD, RDD with proper diagnostics).

## Summary

"Awesome Econ AI Stuff" is an open-source repository that curates AI skills specifically designed for economists' research workflows. Each skill is a pre-configured module that teaches an AI coding assistant (Claude Code, Cursor, Codex, or Gemini CLI) how to perform a specific research task -- from running difference-in-differences analyses in R with proper diagnostics, to generating publication-ready LaTeX regression tables, to building and solving Walrasian general equilibrium models.

The collection spans eight categories that map to the stages of economics research. Analysis skills handle econometric estimation in Python, R, and Stata. Data skills automate fetching from APIs like FRED and World Bank or cleaning messy datasets. Theory skills can typeset economic models in LaTeX or build computable GE models in Julia. Writing skills draft papers with proper academic structure and generate publication-quality tables. Engineering skills handle the software infrastructure -- git workflows, code refactoring, and spec-driven development. The ideation and literature skills assist with generating research questions and synthesizing academic literature.

The project emphasizes accessibility: skills are installed by cloning a Git repository and invoked via simple slash commands (e.g., `/r-econometrics Run a DiD analysis on treatment_data.csv`). This lowers the barrier for economists who are not software engineers but want to leverage AI coding assistants effectively. The open-source nature means the community can contribute new skills and improve existing ones.

## Relevance to Economics Research

This resource directly addresses the gap between general-purpose AI tools and the specific needs of economics researchers. Rather than crafting custom prompts for each task, economists can use pre-built skills that encode best practices for econometric analysis, data handling, and academic writing. The skill-based approach is particularly valuable for researchers transitioning from traditional tools (Stata, R, MATLAB) to AI-augmented workflows, as the skills abstract away the complexity of prompting while ensuring proper statistical methodology (e.g., correct standard errors, appropriate diagnostics). The collection also serves as a template for building custom skills tailored to specific research projects.

## Related Concepts

- [[concepts/ai-skills]]
- [[concepts/ide-and-terminal]]
- [[concepts/claude-code]]
- [[concepts/agentic-workflows]]

## Related Summaries

- [[summaries/using-llms-cursor]]
- [[summaries/guide-which-ai]]
- [[summaries/llm-collaboration]]
- [[summaries/claude-code-skills]]
- [[summaries/skill-library]]
