---
title: "ZeroPaper: An Autonomous Research System"
tags:
- summary
- finance-econometrics
- automated-research
- finance-research
- AI-pipeline
- multi-agent-systems
sources:
- '[[raw/papers/ZeroPaper - An Autonomous Research System.pdf]]'
date_updated: 2026-05-15
date_published: 2026-05-01
---

- **Author/Source**: Alejandro Lopez-Lira (working paper, 2026-05-01)
- **Original**: companion paper to [https://github.com/alejandroll10/zeropaper](https://github.com/alejandroll10/zeropaper) (SSRN abstract: 6687378)

## Key Ideas

- ZeroPaper takes a research domain as input and produces a publication-candidate LaTeX manuscript as output with no human intervention between launch and completion. The pipeline runs 10 numbered stages and 6 adversarial gates, coordinates ~30 specialized agents, and amortizes to ~$2/paper on a flat-fee Claude Code Max subscription (roughly one cent of marginal cost).
- The paper's contribution is twofold: (1) the **system itself** (Section 4), and (2) the **design discipline** — ten premises about LLM behavior and cost (Section 2), and six principles derived from them (Section 3) — that lets a pipeline of this length terminate without drift.
- **Ten premises** group into weaknesses (self-bias, long-context degradation, coherence drift, stochastic error, path-of-least-resistance), capabilities (reads-any-text, judges open-ended predicates, fresh instances are less correlated but not independent), and deployment (tokens-and-time cost, infrastructure fails independently of work).
- **Six design principles** trace to those premises: (1) the pipeline is a Markov machine with external control flow — state lives in a JSON file every stage reads/writes, not in conversation history; (2) context is costly — every byte in always-loaded files must justify its cost; (3) delegate — orchestrator routes, fresh-context subagents do the work; (4) verify, do not trust — every gate uses ≥2 verifiers with distinct framings, including a free-form skeptical reader; (5) termination must be mechanical, not at the orchestrator's discretion; (6) parallelize independent dispatches.
- Three architectural choices neutralize the dominant failure modes: (i) every substantive advance is gated by an adversarial agent that has not seen the generator's reasoning (kills self-bias); (ii) every loop has a mechanical termination predicate (kills "one more try" runaway); (iii) every gate runs at least two evaluators with distinct framings (kills single-evaluator blind spots).
- The orchestrator is itself an LLM session — it reads `process_log/pipeline_state.json`, dispatches to a subagent, writes output to a versioned artifact tree under `output/stageN/`, updates state, and commits. Every state change is a separate git commit; provenance is reconstructable line-by-line.
- Stage rundown: Stage 0 Problem Discovery (`literature-scout` → `gap-scout` → Gate 0); Stage 1 Idea Generation (`idea-generator` ↔ `idea-reviewer` up to 5 rounds; parallel `novelty-checker` and `idea-prototyper` screens); Stage 2 Theory Development (versioned `theory_vN.md`, Math Audit gate with structured + free-form auditors, novelty check on full theory); Stage 2b Theory Exploration (numerical verification, calibration, plots); Stage 3 Implications (per-prediction gap-scout: NOVEL / PUZZLE-CANDIDATE / SUPPORTED / DEAD); Stages 3a/3b optional empirical and LLM-experiment extensions; **Puzzle Triage** when empirics contradict theory (NORMAL-PROCEED / FIX-EMPIRICS / RECONCILE / BACK-TO-IDEA / PIVOT / HONEST-NULL); Stage 4 Self-Attack + triager; Gate 4 Scorer Decision with structured + freeform scorers + mandatory `branch-manager` third component; Stage 5 Paper Writing (intro/conclusion last); Stage 6 Referee Simulation with three independent referees (standard, freeform, mechanism) aggregated by an `editor`; Stages 7–9 Style, Bibliography Verify, Polish (six parallel agents, max two rounds).
- Scorer thresholds are tier-explicit: ADVANCE at ≥75 for top-5 target tier, 65 for field journals, 55 for letters. Plateau detection (delta <3) triggers either a deepening playbook or a regeneration round; five ABANDON verdicts on the same problem are required before retreating to Stage 0.
- Editor aggregation rule at Gate 5 is intentionally harsh: any single Reject vote from the structured or freeform referee produces aggregated Reject (with one escape — downgrade to Major Revision if rejection is on journal-fit grounds only); MISATTRIBUTED or DECORATIVE verdicts from the mechanism referee force Major Revision.
- Author is explicit that the paper does **not** claim ZeroPaper produces publishable papers — only that the architecture is structured to avoid the failure modes most often degrading automated-research prototypes, and that the implemented principles trace to those failure modes. Empirical publication rate is "measurable but not yet measured."

## Summary

The paper formalizes the design discipline behind ZeroPaper (introduced practically in [[summaries/zeropaper-template]]). The motivating empirical fact is that long-running autonomous LLM pipelines fail in characteristic ways — self-bias, long-context degradation, coherence drift, stochastic error, and a path-of-least-resistance bias toward declaring premature completion. A pipeline that ignores these fails silently or loops forever. The paper's central methodological move is to ground every architectural choice in one or more of ten premises about LLM behavior, and to require that any proposed design principle "trace" to at least one premise — otherwise it is decoration.

Principles 1 and 2 together force delegation: the machinery lives somewhere other than the orchestrator's running context, loaded or spawned only when needed. Lopez-Lira distinguishes four delegation vehicles by cost and isolation profile — docs (content read on demand, cheapest, zero isolation), scripts (deterministic code, no model tokens during execution), skills (self-contained modules loaded on trigger), and agents (fresh-context sub-conversations with their own system prompt, substantial but not total context isolation). The agent isolation is "real rather than rhetorical" only because of Premise 8: fresh instances are less correlated but not independent. Multi-verifier variance reduction has a floor at the model-level correlation; crossing different models (Claude / Codex / Gemini) lowers the floor further.

Principle 4 (verify, do not trust) has five corollaries that every verification stage must honor: verification is a distinct stage, not a sub-step (a worker that spawns its own verifier inside its own stage has not escaped self-bias); at least two verifiers with distinct framings (structured + free-form); at least one free-form critique (numeric scores are easy to game when the worker can see them); each verifier framed adversarially ("find errors" not "evaluate correctness"). Principle 5 (mechanical termination) is the bulwark against the orchestrator rationalizing "one more try" indefinitely — every runaway loop must have at least one mechanical branch on its termination path, and termination triggers when marginal value stops, not only when a cap is hit (delta thresholds escalate when score-delta-feedback-novelty falls below a threshold).

Section 4 walks through how those principles instantiate in the worked system. The orchestrator does no research itself — it reads state, picks a vehicle, dispatches, updates state. Substantive output comes only from specialized agents. The artifact tree under `output/` doubles as the process log; the git log of a completed run is a linear record of who did what and when. The state file (`pipeline_state.json`) is the single source of truth for where the pipeline is, and because it is JSON and committed, another orchestrator session in any of the three host runtimes can resume an interrupted run deterministically. The paper closes with the Puzzle Triage and Gate-5 editor-aggregation rules — both designed to prevent the pipeline from either silently suppressing contradictions (the path-of-least-resistance failure mode) or over-reacting to noisy verifier output.

## Relevance to Economics Research

This is the most explicit design specification for an autonomous research pipeline in economics. Three things matter for researchers reading it:

1. **The premise-principle structure is portable.** The ten premises are claims about LLM behavior, not about ZeroPaper specifically. They apply to any long-running autonomous LLM pipeline — including the Korinek workflows in [[summaries/applications-generative-ai]], the Andrews framework in [[summaries/andrews-ai-research]], the Kohler-Hoyle-Ash reproduction pipeline in [[summaries/kohler-agentic-reproduction]], and parallel pipelines in [[summaries/ai-powered-scholarship]], [[summaries/ralph-wiggum-asset-pricing]], [[summaries/dickerson-ai-asset-pricing]], and [[summaries/project-ape]]. Each can be audited against the ten premises: does it isolate verifiers, mechanically terminate, externalize state? Where it does not, the paper claims to predict the failure mode.
2. **The honesty about scope is the cleanest in this literature.** Lopez-Lira distinguishes "the architecture avoids known failure modes" (a structural claim he defends) from "the architecture produces publishable papers" (an empirical claim he explicitly does not yet make). This is a useful template for how economists should write about and review autonomous-research claims — separate architectural correctness from publication-rate empirics.
3. **It clarifies what should be in `CLAUDE.md` vs. elsewhere.** The paper's Principle 2 (context is costly) gives a budget rule for the always-loaded orchestrator config: every line must be load-bearing for this step, every step, and on step 1000. Domain invariants pass; ornamental prose does not. This is directly applicable to anyone writing their own `CLAUDE.md` or `AGENTS.md` for econ workflows (see [[summaries/real-claude-md]], [[summaries/your-claude-md]]).

For empirical-finance users, the Puzzle Triage taxonomy (NORMAL-PROCEED / FIX-EMPIRICS / RECONCILE / BACK-TO-IDEA / PIVOT / HONEST-NULL) and the Gate-3a feasibility check are the operational answer to "what happens when the data refuses to confirm the model?" — a research question the autonomous-pipeline literature has not previously addressed in print.

## Related Concepts

- [[concepts/automated-research]]
- [[concepts/multi-agent-systems]]
- [[concepts/ai-agents]]
- [[concepts/context-management]]
- [[concepts/claude-md-files]]
- [[concepts/sycophancy-and-bias]]
- [[concepts/human-in-the-loop]]
- [[concepts/reproducibility-transparency]]

## Related Summaries

- [[summaries/zeropaper-template]] — the practical README for the same pipeline this paper formalizes
- [[summaries/zeropaper-gallery]] — 22 finance papers produced end-to-end by this pipeline
- [[summaries/automated-research-finance]] — the original collaboration call before the public release
- [[summaries/stress-test-research-pipeline]] — Lopez-Lira's upstream idea-evaluation pipeline
- [[summaries/applications-generative-ai]] — Korinek's broader taxonomy of generative-AI uses in economics
- [[summaries/korinek-2023]] — Korinek (2025) on agentic LLM systems for economic research, cited as nearest predecessor
- [[summaries/ai-powered-scholarship]] — Novy-Marx & Velikov's parallel finance-paper pipeline
- [[summaries/ralph-wiggum-asset-pricing]] — Chen's open-source Ralph loop framework
- [[summaries/dickerson-ai-asset-pricing]] — Dickerson's multi-agent asset pricing repo
- [[summaries/project-ape]] — Social Catalyst Lab's automated policy-evaluation pipeline
- [[summaries/kohler-agentic-reproduction]] — agentic reproduction of social-science results, a complementary application of the same design discipline
