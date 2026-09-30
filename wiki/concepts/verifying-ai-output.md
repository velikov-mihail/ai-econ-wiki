---
title: "Verifying AI Output"
tags: [concept, quality, verification, methodology]
sources:
  - "[[summaries/verifying-llm-output.md]]"
  - "[[summaries/koren-theorist-toolbox.md]]"
  - "[[summaries/matray-ai-guide.md]]"
  - "[[summaries/integration-collaboration-substack.md]]"
  - "[[summaries/integration-collaboration-markus-162-8.md]]"
  - "[[summaries/cc-series-24-agents-auditing-did.md]]"
  - "[[summaries/cc-changed-how-i-work-3.md]]"
  - "[[summaries/prompts-swarms-markus-166-4.md]]"
  - "[[summaries/kohler-agentic-reproduction.md]]"
date_updated: 2026-09-30
---

# Verifying AI Output

Verifying AI output means building deliberate checks that establish whether AI-produced code, analysis, or proofs are *correct*, not just whether they run or sound right. As agents make production cheap, verification becomes the scarce input and the main bottleneck in AI-assisted research.

## Context & Background

Agents are good at removing the errors that announce themselves: they iterate until code compiles, the script runs, and the table fills in. What remains are **silent errors**, outputs that look plausible but rest on a shortcut. Examples include a merge that drops half the sample, a panel balanced by deleting 40% of firm-years, clustering at the wrong level, or a proof step waved through with "clearly." Two features of LLMs make these errors dangerous. Models never flag their own uncertainty, and a model that produced an output is biased toward confirming it. Goldsmith-Pinkham calls the resulting backlog of unchecked results **verification debt**. Matray adds a third trait: the model is *quietly lazy*. It resolves ambiguity in the least-effort direction and declares work "redundant" to avoid it, so the question is not only "is this wrong?" but "is this cutting corners?" ([[summaries/matray-ai-guide|Matray]]).

## Key Principles

Across sources, the same handful of principles recur:

- **Independence.** The producer cannot be its own verifier. Review in a fresh session or agent, and understand the limits of each level of independence: a subagent is briefed and summarized by its parent, so a new session you brief yourself is cleaner. Asking a model to "ignore" earlier context does nothing; independence comes only from *removing* context ([[summaries/verifying-llm-output|Bäckman]]).
- **Diversity breaks correlated errors.** Two instances of the same model share blind spots. A model from a different developer ([[summaries/verifying-llm-output|Bäckman]]; Koren's `codex-math`), or a different programming language ([[summaries/cc-series-24-agents-auditing-did|Cunningham]]), makes errors closer to independent, so a match is informative.
- **Adversarial roles.** Assign an agent to *break* the work, not to review it politely: devil's-advocate agents ([[summaries/cc-changed-how-i-work-3|Cunningham]]), prover/verifier/judge splits ([[summaries/prompts-swarms-markus-166-4|Sandomirskiy]]), and a reviewer gate that must write an approval file before a workstream can close ([[summaries/koren-theorist-toolbox|Koren]]).
- **Reviewers report; humans fix.** A reviewer that edits hands you a second unverified diff and tends to close findings rather than fix correctness. Confident false positives are common, so make the reviewer prove the findings that matter.
- **Review the diff, not the codebase.** Git scopes the reviewer's attention to what changed, which improves focus and cuts token cost ([[summaries/integration-collaboration-substack|Goldsmith-Pinkham]], [[summaries/verifying-llm-output|Bäckman]]).
- **Don't let the agent grade its own test.** When independently reimplementing a result, run the script yourself: an agent that sees an implausible number will "debug towards plausibility."
- **Make unverified status visible and enforced.** Typed placeholders (`\unproven{}`), a verification ladder (informal → Lean-verified → readable), and hooks that mechanically block "done" without sign-off ([[summaries/koren-theorist-toolbox|Koren]]).
- **The human must understand, not just approve.** Comprehension checks, such as a quiz on the empirical consequences of a change, keep the researcher actually in the loop rather than rubber-stamping.

## A Ladder of Checks (cost vs. strength)

| Check | Cost | What it catches |
|---|---|---|
| Sample-construction table, merge diagnostics, variable distributions | Near zero | Right code, wrong data |
| Prose numbers vs. table numbers; reference verification | Near zero | Stale coefficients, invented citations |
| External benchmark | Low | Results that don't "make sense" |
| Fresh-agent review of the diff | Low | Shortcuts the author agent is blind to |
| Second model from a different developer | Medium | Errors correlated within one model family |
| Comprehension quiz for the researcher | Medium | The human not actually understanding the change |
| Independent reimplementation in another language, from spec only | High | Code that faithfully implements the *wrong* specification |
| Formal verification (Lean) | High, theory only | Gaps in proofs |

Reserve the expensive checks for main exhibits and for steps where a mistake would be invisible in the output: complex panel construction, hand-rolled event time, multi-source indices.

## Verification During Production

The cheapest verification happens while the work is being built: plan before code, have the agent list every question and default it would choose, execute one small step at a time and inspect the counts, and ask *why* (which decisions could reasonably differ?) rather than *what*. Log the resolved ambiguities in a `decisions.md`. This overlaps with [[concepts/plan-driven-development]] and [[concepts/pre-analysis-plans]].

## Related Concepts

- [[concepts/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/research-quality|Research Quality]]
- [[concepts/cross-language-replication|Cross-Language Replication]]
- [[concepts/version-control-research|Version Control for Research]]
- [[concepts/multi-agent-systems|Multi-Agent Systems]]
- [[concepts/sycophancy-and-bias|Sycophancy and Bias]]
- [[concepts/citation-hallucination|Citation Hallucination]]
- [[concepts/reproducibility-transparency|Reproducibility & Transparency]]
- [[concepts/ai-limitations|AI Limitations]]
