---
title: "Multi-Agent Systems"
tags: [concept, ai-agents, architecture]
sources:
  - "[[summaries/ars-claude-code.md]]"
  - "[[summaries/haaland-reviewer.md]]"
  - "[[summaries/worldseed.md]]"
  - "[[summaries/coarse-ink.md]]"
  - "[[summaries/cc-series-24-agents-auditing-did.md]]"
  - "[[summaries/ai-creativity-markus-166-2.md]]"
date_updated: 2026-08-23
---

# Multi-Agent Systems

Multi-agent systems coordinate multiple LLM-driven agents — each with a distinct role, prompt, and sometimes private information — to produce outcomes no single agent could produce alone. In academic research the dominant pattern is panel review (an Editor-in-Chief plus several reviewers plus a Devil's Advocate), but the same architecture is increasingly used for hypothesis generation, replication audits, and emergent simulation.

## Context & Background

Two design philosophies are visible in current tools:

- **Pipelined / orchestrated** — agents are called in a fixed sequence by an orchestrator. Each agent's output is schema-validated, normalized, and handed to the next. Examples: [[summaries/ars-claude-code|ARS]]'s 10-stage pipeline; [[summaries/haaland-reviewer|Haaland's Reviewer]]'s deterministic 10-step flow; [[summaries/coarse-ink|coarse.ink]]'s single-pass review.
- **Emergent / world-seeded** — agents are given roles, rules, private information, and consequences; the orchestrator only enforces the rules. The sequence emerges. Example: [[summaries/worldseed|WorldSeed]], whose Autoresearch demo produced 72 peer-reviewed papers in 11 hours through emergent role drift no one configured.

A third philosophy appears in mathematical proof search: **parallel exploration with a stopping rule**. GPT-5.6 Sol Ultra proved the cycle double cover conjecture by spawning 64 agents to pursue different proof strategies simultaneously, under an explicit instruction not to return an answer before eight hours of work ([[summaries/ai-creativity-markus-166-2|Markus Academy 166-2]]). Here the agents share a goal rather than roles, and the orchestrator's job is to kill converging branches rather than to sequence outputs. The swarm buys coverage of a large search space; the minimum-runtime instruction buys persistence past the point where a single session would give up.

Cross-cutting design concerns include: (1) preventing the agents from sharing a cognitive frame ("frame-lock" — the Devil's Advocate attacks arguments but never premises); (2) anti-sycophancy protocols so reviewers don't concede under pushback; (3) traceability — every output linked back to the agent that produced it, the inputs it saw, and the schema it passed.

## Practical Implications

- **Define explicit roles and private information.** What does each agent know that the others don't? Asymmetry is what drives non-trivial collective behavior.
- **Use schema validation between agents, not free text.** Haaland's Reviewer requires every reviewer JSON to pass schema + semantic checks before reaching the normalization layer.
- **Build for traceability from the start.** WorldSeed builds a search-evolution graph linking every paper back to its hypothesis, experiment, citations, and reviewer reasoning. Pipelines without this graph are unauditable.
- **Choose pipelined vs. emergent based on objective.** Pipelined is right when you need reproducibility and auditability (peer review, replication). Emergent is right when you want the system to find directions you didn't pre-specify (hypothesis generation, ABM simulation).
- **Anti-sycophancy is an engineering problem, not a prompting one.** ARS's Concession Threshold Protocol scores rebuttals 1–5 before allowing a concession.

## Key Sources

- [[summaries/ars-claude-code|Academic Research Skills (ARS)]] — 13+12+7+10-agent suite with explicit anti-sycophancy and integrity gates
- [[summaries/haaland-reviewer|Reviewer (Haaland)]] — Schema-validated multi-agent reviewer for econ papers
- [[summaries/worldseed|WorldSeed]] — Emergent multi-agent world engine
- [[summaries/coarse-ink|coarse.ink]] — Open-source paper reviewer (~$2/review)
- [[summaries/cc-series-24-agents-auditing-did|Multiple Agents Auditing Your DiD Code]] — Cross-language replication as hallucination measurement

## Related Concepts

- [[concepts/ai-agents|AI Agents]]
- [[concepts/agentic-workflows|Agentic Workflows]]
- [[concepts/ai-peer-review|AI-Assisted Peer Review]]
- [[concepts/human-in-the-loop|Human in the Loop]]
- [[concepts/automated-research|Automated Research]]
