---
title: "My Claude Code Setup - Academic Workflow Template"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/My Claude Code Setup.md]]"
date_updated: 2026-04-03
---
- **Original**: [https://psantanna.com/claude-code-my-workflow/](https://psantanna.com/claude-code-my-workflow/)


**Author/Source**: Pedro Sant'Anna, [psantanna.com](https://psantanna.com/claude-code-my-workflow/)

## Key Ideas

- A comprehensive Claude Code template covering the full academic lifecycle: slides, papers, data analysis, replication packages, proposals, and presentations
- Uses a "contractor mode" orchestrator where the user describes the task and Claude autonomously plans, implements, reviews, fixes, and verifies until quality gates pass
- Includes 10 specialized agents (proofreader, slide auditor, pedagogy reviewer, R reviewer, TikZ critic, domain reviewer, adversarial QA pair, translator, verifier)
- Features an adversarial critic-fixer loop: two agents check each other's work across up to 5 rounds, where the critic cannot fix and the fixer cannot approve
- Quality scoring system requires every output to score 80+ on a 0-100 scale before shipping; the orchestrator verifies every output
- Includes 22 slash commands and 18 context-aware rules covering LaTeX compilation, proofreading, deployment, literature review, data analysis, and more
- Adopted by 15+ research groups across economics, energy, political science, and engineering; part of a growing community ecosystem

## Summary

This article describes an actively maintained Claude Code workflow template designed for academic work. Created by Pedro Sant'Anna (an econometrician), the template goes well beyond basic chatbot usage to implement a sophisticated multi-agent system. The "contractor mode" orchestrator means the user provides a high-level task description and Claude handles the entire implementation pipeline: planning the approach, running specialized review agents, fixing issues, and re-verifying until quality thresholds are met.

The system's distinguishing feature is its adversarial quality assurance: a critic agent and fixer agent iterate over outputs for up to 5 rounds, with hard separation of roles (the critic cannot make changes, the fixer cannot approve its own work). This mirrors the peer review process in academia. The template also includes a Beamer-to-Quarto pipeline for converting LaTeX slides to web-friendly formats, a plan-first workflow that starts non-trivial tasks in plan mode, and a `[LEARN:tag]` system where corrections persist in a MEMORY.md file across sessions. The template is open source and has been adopted by 15+ research groups, with extensions from several community projects.

## Relevance to Economics Research

This is one of the most directly applicable Claude Code setups for academic economists. The template covers the exact deliverables economists produce: research papers (with LaTeX compilation), presentation slides (Beamer to Quarto), data analysis (R-focused), literature reviews, replication packages, and research ideation. The adversarial critic-fixer loop enforces quality standards that parallel peer review. The fact that it has been adopted by 15+ research groups including economics groups suggests it is production-tested for the specific demands of academic research workflows. The `/data-analysis` and `/review-paper` commands directly address core economics research tasks.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ai-agents]]
- [[concepts/ai-workflows]]
- [[concepts/claude-code-skills]]
- [[concepts/research-quality]]

## Related Summaries

- [[summaries/claude-code-newbies]]
- [[summaries/claude-code-hacks]]
- [[summaries/ai-for-professionals]]
- [[summaries/starter-templates]]
