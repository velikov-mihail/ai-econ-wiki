---
title: "Plan-Driven Development"
tags: [concept, workflows, planning, methodology]
sources:
  - "[[wiki/summaries/prompt-plan-review-revise.md]]"
  - "[[wiki/summaries/claude-code-hacks.md]]"
  - "[[wiki/summaries/architecture-patterns.md]]"
  - "[[wiki/summaries/patterns.md]]"
  - "[[wiki/summaries/ai-agents-econ-research.md]]"
  - "[[wiki/summaries/workflows.md]]"
date_updated: 2026-04-03
---

## Definition

**Plan-driven development** is a workflow philosophy in which every non-trivial task begins with an explicit plan that is reviewed and approved before any implementation begins. In the context of AI-assisted research, this means writing a structured plan to a file, reviewing it (often with a fresh-context agent), and only then starting a new session to execute it. The approach directly counteracts the most common failure mode of agentic AI: context window degradation from long, unstructured sessions.

The most formalized version is Chris Blattman's **PPRR pattern** (Prompt, Plan, Review, Revise): `/prompt` structures rough thinking into a formal prompt, Plan Mode explores without executing, `/review-plan` spins up a fresh agent for independent critique, and `/done` captures session context for continuity. Matt Van Horn's "plan first, always" principle operationalizes the same idea: every idea immediately becomes a `plan.md` file via a planning skill before any code is written.

## Context & Background

Plan-driven development emerged as a response to a specific failure mode: agentic AI systems that are given open-ended tasks without a plan tend to lose coherence as their context windows fill, make increasingly poor decisions as earlier instructions get pushed out of context, and pursue approaches that drift from the user's intent. Multiple sources converge on the same solution: separate planning from execution, and treat the plan as a reviewable artifact.

The pattern has deep parallels in economics research. Pre-analysis plans, research design documents, and grant proposals all embody the same principle: think carefully before committing to expensive execution. The difference is that with AI tools, the cost of planning has dropped dramatically -- a structured plan can be produced in minutes rather than days -- while the cost of unplanned execution (wasted tokens, incorrect output, context degradation) remains high.

## Key Perspectives

**Blattman (PPRR)** ([[wiki/summaries/prompt-plan-review-revise.md]]) provides the most complete framework. The four-step loop was demonstrated by building a website in 90 minutes on a plane. The intellectual centerpiece is the `/review-plan` step: a fresh agent reads the plan cold, mimicking external peer review. The author ran `/review-plan` twice with different reviewer personas to catch blind spots -- missing prerequisites, assumed knowledge, structural errors, and usability problems. The `/done` step addresses session continuity by writing structured handoff notes. Combined with CLAUDE.md, the loop creates a system where AI interactions compound rather than starting fresh each time.

**Van Horn** ([[wiki/summaries/claude-code-hacks.md]]) takes plan-driven development to its extreme. His core workflow flips the traditional 80/20 coding-to-planning ratio: every idea immediately becomes a `plan.md` via the `/ce:plan` skill, which launches parallel research agents to analyze the codebase, search past solutions, and produce a grounded plan with acceptance criteria. Implementation then becomes mechanical execution via `/ce:work`. He also uses `/last30days` research queries before planning to ground decisions in current community knowledge rather than stale training data.

**Blattman (Patterns)** ([[wiki/summaries/patterns.md]]) catalogs the design patterns that make plan-driven development work. Phased Execution breaks complex workflows into stages with user checkpoints ("STOP: Discuss with user before proceeding"). Iteration Gates present output and explicitly ask whether to proceed, adjust, or stop. These patterns prevent irreversible actions from running without review.

**Blattman (Architecture Patterns)** ([[wiki/summaries/architecture-patterns.md]]) extends plan-driven thinking to pipeline architecture. The Collection-Compilation-Review pipeline structures any document-heavy workflow into discrete stages that can be reviewed independently. The Threshold Gate pattern checks whether expensive work will matter before doing it. The Validation Stack layers four independent checks on the principle that no single layer catches all error types.

**Panjwani** ([[wiki/summaries/ai-agents-econ-research.md]]) identifies "not planning before implementation" as one of the three biggest beginner mistakes economists make with AI. He recommends writing plans to files and starting fresh sessions for execution, specifically because long unstructured sessions degrade agent performance as context windows fill.

## Practical Implications

- **Always plan non-trivial tasks**: Before asking an agent to implement anything complex, write a plan. Review it. Then start a fresh session for execution.
- **Use fresh-context review**: Have a separate agent (not the one that wrote the plan) critique it. This catches blind spots that self-review misses due to the self-bias problem.
- **Write plans to files**: Plans stored as `plan.md` files serve as durable artifacts that persist across sessions and can be shared with collaborators.
- **Use personas for review**: Assign different expert identities to review agents (e.g., "methodologist," "applied researcher," "hostile referee") to get diverse perspectives on the plan.
- **Build in checkpoints**: Use Phased Execution patterns with explicit STOP points before irreversible actions (sending emails, overwriting data, submitting to journals).
- **Ground plans in current knowledge**: Run research queries before planning to ensure the plan reflects current best practices, not stale training data.

## Open Questions

- How much planning overhead is optimal? At what point does planning become over-engineering for simple tasks?
- Should research plans produced by AI be pre-registered or shared with co-authors before execution, analogous to pre-analysis plans?
- How do plan-driven workflows interact with exploratory data analysis, where the path forward is inherently uncertain?
- Can the PPRR loop be adapted for theoretical work where the "implementation" is proving theorems rather than writing code?

## Sources

- [[wiki/summaries/prompt-plan-review-revise.md]] -- Blattman's PPRR loop: the foundational plan-driven workflow
- [[wiki/summaries/claude-code-hacks.md]] -- Van Horn's "plan first, always" principle with parallel research agents
- [[wiki/summaries/architecture-patterns.md]] -- Pipeline architecture and validation patterns
- [[wiki/summaries/patterns.md]] -- Phased Execution, Iteration Gates, and Depth Calibration
- [[wiki/summaries/ai-agents-econ-research.md]] -- Panjwani on planning as essential for context window management
- [[wiki/summaries/workflows.md]] -- The layered workflow system building from PPRR upward
