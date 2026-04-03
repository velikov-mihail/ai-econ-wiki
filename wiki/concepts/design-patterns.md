---
title: "Design Patterns for AI Workflows"
tags: [concept, workflows, architecture]
sources:
  - "[[summaries/architecture-patterns.md]]"
  - "[[summaries/patterns.md]]"
  - "[[summaries/workflow-overview.md]]"
date_updated: 2026-04-03
---

# Design Patterns for AI Workflows

Design patterns for AI workflows are reusable templates and architectural approaches for structuring how researchers interact with AI tools — analogous to software design patterns.

## Context & Background

As researchers gain experience with AI tools, common patterns emerge for structuring effective interactions:

- **Prompt-Plan-Review-Revise (PPRR)**: Iterative cycle of planning and refinement
- **DAAF (Data Analyst Augmentation Framework)**: Structured framework for AI-assisted data analysis
- **Compilation and review**: AI compiles information, human reviews and curates
- **Skill-based architecture**: Reusable AI instructions packaged as "skills"
- **Pipeline pattern**: Sequential processing stages with defined inputs and outputs
- **Fan-out/gather**: Parallel processing of independent tasks followed by synthesis

## Practical Implications

- **Learn the common patterns**: Understanding established patterns saves you from reinventing them
- **Match pattern to task**: Different research tasks call for different interaction patterns
- **Document your patterns**: Write down workflows that work well so you and others can reuse them
- **Evolve patterns over time**: Refine your approaches based on what works

## Related Concepts

- [[concepts/ai-workflows|Ai Workflows]]
- [[concepts/plan-driven-development|Plan Driven Development]]
- [[concepts/claude-md-files|Claude Md Files]]
- [[concepts/agentic-workflows|Agentic Workflows]]
