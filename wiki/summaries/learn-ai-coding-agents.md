---
title: "Learn About AI Coding Agents"
tags: [summary, ai-agents, skills, agents-md, claude-md, configuration]
sources:
  - "[[raw/articles/Learn About AI Coding Agents - Awesome Econ AI Stuff.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Antonio Mele (London School of Economics), via Awesome Econ AI Stuff (meleantonio.github.io)
- **Original**: [https://meleantonio.github.io/awesome-econ-ai-stuff/pages/learn.html](https://meleantonio.github.io/awesome-econ-ai-stuff/pages/learn.html)

- **Key Ideas**
  - **Skills** are reusable instruction sets ("expert knowledge packages") stored as `SKILL.md` files that teach agents how to perform domain-specific tasks; they follow a progressive disclosure pattern (discovery, activation, execution).
  - **Rules** are persistent project-level or personal configuration files: `AGENTS.md` (project-specific, version-controlled, shared with team) and `CLAUDE.md` (personal, local, Claude Code only).
  - Skills and subagents serve different purposes: skills add **knowledge** (like a recipe book), subagents **parallelize work** (like hiring a contractor). Skills share the main context; subagents run in isolated contexts.
  - The full configuration hierarchy (from lowest to highest priority): organization policies, user `CLAUDE.md`, project `AGENTS.md`, task-level skills, and the user's immediate prompt.
  - A practical economics example walks through the hierarchy: agent reads `AGENTS.md` to learn project conventions, activates a `stata-econometrics` skill for regression analysis, and the user's prompt overrides specific defaults.

- **Summary**

This educational resource from the Awesome Econ AI Stuff project provides a structured guide to the building blocks of AI coding agent systems. It defines and distinguishes four key concepts: skills (reusable instruction sets in `SKILL.md` format), rules (persistent configuration via `AGENTS.md` and `CLAUDE.md`), subagents (parallel isolated processes), and the resolution hierarchy that determines which instructions take precedence when they conflict.

The guide emphasizes practical application for economists. Skills follow the Agent Skills standard (agentskills.io) and are portable across multiple AI tools (Claude Code, Cursor, Gemini CLI). The `AGENTS.md` file is positioned as the primary project-level configuration --- version-controlled, shared with collaborators, and compatible with 60k+ projects --- while `CLAUDE.md` holds personal preferences. The distinction between skills (which add domain knowledge to the main agent) and subagents (which run independently for parallelizable tasks) is clarified with concrete examples: "Run a DiD analysis following best practices" calls for a skill, while "Read all 50 do-files and summarize what variables each creates" calls for a subagent.

- **Relevance to Economics Research**

This is an essential reference for economists setting up their AI coding environment. The `AGENTS.md` example for an economics research project (with rules for data handling, Stata/R conventions, LaTeX formatting, and reproducibility) provides a template that researchers can adapt immediately. Understanding the skill/subagent distinction and the configuration hierarchy is foundational for building reliable, reproducible agent-assisted research workflows, especially in collaborative projects where multiple researchers need consistent agent behavior.

- **Related Concepts**
  - [[concepts/skills-vs-agents]]
  - [[concepts/agentic-ai]]
  - [[concepts/claude-md-files]]
  - [[concepts/agentic-workflows]]
  - [[concepts/mcp-protocol]]

- **Related Summaries**
  - [[summaries/agents-vs-skills]]
  - [[summaries/ai-agents-econ-research]]
  - [[summaries/ai-agents-generative-ai]]
  - [[summaries/claude-code-what-comes-next]]
