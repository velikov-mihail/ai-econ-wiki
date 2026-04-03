---
title: "Skills vs Agents"
tags: [concept, agentic-workflows, claude-code]
sources:
  - "[[summaries/agents-vs-skills.md]]"
  - "[[summaries/building-skills.md]]"
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/agentic-everything.md]]"
  - "[[summaries/skill-library.md]]"
date_updated: 2026-04-03
---

# Skills vs Agents

## Definition

In agentic AI coding tools like Claude Code, **skills** and **agents** are the two primary building blocks for automating research workflows. A **skill** is a reusable markdown-based prompt saved as a slash command that runs inside the main conversation, sharing full context and enabling interactive, multi-step workflows with user checkpoints. An **agent** is a subprocess that runs in a fresh, isolated context window -- it receives explicit inputs, performs a task, and returns outputs without access to the prior conversation history.

The distinction matters because the choice between skill and agent determines whether the AI benefits from (or is constrained by) the conversation so far. Skills excel when context continuity is valuable; agents excel when a fresh perspective or parallel execution is needed.

## Context & Background

The skills-vs-agents framework emerged from the Claude Code ecosystem in early 2026, articulated most clearly by Chris Blattman and adopted by the economics research community through figures like Aniket Panjwani and Claes Backman. The framework addresses a practical problem: as researchers build increasingly complex AI-assisted workflows, they need a principled way to decide which tasks should run interactively (sharing the researcher's context) and which should run independently (with clean separation). The distinction parallels familiar patterns in research -- you want your RA to share context when iterating on your analysis, but you want a fresh pair of eyes when reviewing a draft.

## Key Perspectives

**Blattman ([[summaries/agents-vs-skills.md|Agents vs Skills]])** provides the canonical decision framework. Skills are best for tasks requiring conversation context, user interaction, multi-step workflows with checkpoints, or state modification (writing files, sending emails). Agents are best for review and critique, parallel evaluation, and tasks with clear input/output boundaries. His most important insight is the **self-bias problem**: when Claude reviews its own work in the same conversation, it systematically finds its output acceptable because it "knows what it meant." Using an agent with a fresh context breaks this pattern. He demonstrates **agent debates** where agents impersonating different methodological traditions (grounded theory vs. thematic analysis) or named economists (Imas, Bursztyn, Thaler) generate genuinely novel perspectives.

**Blattman ([[summaries/building-skills.md|Building Skills]])** details the skill development lifecycle: notice a repeated pattern, do it manually 3-4 times, write the skill, test and iterate, then stabilize. Skills accept arguments, reference external files, and can encode complex patterns like phased execution with user checkpoints, depth calibration, and critic stances. The key insight is that skills are just structured markdown -- no code or compilation required.

**Panjwani ([[summaries/ai-agents-econ-research.md|AI Agents for Economic Research]])** frames skills as "saved playbooks" for domain-specific tasks and identifies underutilizing skills as one of the three biggest beginner mistakes. He points to concrete economist-made skills for paper review, data analysis, and grant writing.

**Svoronos ([[summaries/agentic-everything.md|Agentic Everything]])** emphasizes that directing agents effectively is itself a separate, practice-intensive skill distinct from domain expertise. Subject-matter knowledge becomes more valuable, not less, because spotting when an agent goes wrong requires strong mental models of what should be happening.

## Practical Implications

For economics researchers, the skills-vs-agents distinction maps onto natural divisions in the research workflow:

- **Use skills** for interactive data analysis sessions, iterative figure refinement, multi-step robustness check pipelines, and any workflow where the researcher needs to make decisions at intermediate stages.
- **Use agents** for paper review (to avoid self-bias), parallel code review, stress-testing research designs via agent debates, and any evaluation task where prior context would create blind spots.
- **Build skills early** for tasks you repeat: formatting regression tables, running standard robustness checks, generating summary statistics, reviewing drafts against journal-specific guidelines.
- **Use agent debates** as an on-demand seminar: assign agents distinct methodological identities and let their disagreements surface unexamined assumptions in your research design.

## Open Questions

- How should researchers evaluate when self-bias from shared context actually matters versus when context continuity is more valuable? The boundary is not always clear.
- As context windows grow larger, does the case for agents weaken (because skills can handle more complexity) or strengthen (because self-bias compounds with longer conversations)?
- Can skills and agents be composed into larger workflows where skills handle interactive phases and agents handle review phases? What are the best patterns for this?
- How do these patterns change across different AI tools (Claude Code vs. Codex vs. Cursor)?

## Sources

- [[summaries/agents-vs-skills.md|Agents vs Skills]] -- Blattman's decision framework and agent debate examples
- [[summaries/building-skills.md|Building Skills]] -- Skill development lifecycle and design patterns
- [[summaries/ai-agents-econ-research.md|AI Agents for Economic Research]] -- Panjwani's practical guide for economists
- [[summaries/agentic-everything.md|Agentic Everything]] -- Svoronos on the qualitative shift to agentic tools
- [[summaries/skill-library.md|Skill Library]] -- Curated collection of reusable skills
