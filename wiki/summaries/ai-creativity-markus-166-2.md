---
title: "Can AI Be Creative? (Markus Academy 166-2)"
tags: [summary, academic-research, economic-theory, llm-reasoning, ai-limitations, multi-agent-systems]
sources:
  - "[[raw/Clippings/Can AI Be Creative? AI for Economic Theory with Ortoleva & Sandomirskiy  Markus Academy  166-2.md]]"
date_updated: 2026-08-23
date_published: 2026-08-04
---

- **Author/Source**: Fedor Sandomirskiy (Princeton), with Pietro Ortoleva — Markus' Academy Ep. 166-2 (2nd of 5), hosted by Markus Brunnermeier
- **Original**: [https://www.youtube.com/watch?v=LbedQKu-5XM](https://www.youtube.com/watch?v=LbedQKu-5XM)

- **Key Ideas**
  - **Why the evidence has to come from math.** Episode 1's use cases all presuppose that models can generate genuinely new insight. Testing that in economic theory is hopeless — whether a suggested assumption or model tweak is *good* is a subjective judgment colleagues will disagree about. In mathematics a proof either has gaps or it doesn't. So math supplies the benchmark, even though the bar there is higher than economic theory requires.
  - **The cautionary data point: the ten Erdős problems.** In October 2025 OpenAI announced an internal model had solved ten open problems from Erdős's list. The claim collapsed within a day when Thomas Bloom, who maintains erdosproblems.com, showed the "new proofs" were repackaged results already in the literature.
  - **Diagnosis: poor at attribution, superb at aggregation.** Models genuinely do not know where the ideas they produce came from — that is the fundamental limitation the episode exposed. The optimistic flip side is the same capability seen from the other end: models are exceptionally good at surfacing a result buried in an appendix of a paper no one has read. They aggregate the whole of accumulated human knowledge.
  - **Terence Tao's ledger keeps the score honest.** Of the 1,000+ problems on the Erdős list, as of July 2026 only 19 had been solved with AI involvement, and of those only about 10 proofs count as genuinely new — and even those combine existing literature ideas, most via specialized pipelines rather than an off-the-shelf subscription model.
  - **The unit distance conjecture (open since 1946) falls.** The conjecture: among *n* points in the plane, no configuration asymptotically beats the rectangular grid for the number of pairs at distance exactly one. An internal OpenAI model **constructed a counter-example** — the conjecture was false. The public thinking transcript is available. Mathematicians who had worked on the problem said they would accept the model's proof for any journal without hesitation, while noting the argument, though new and unexpected, built cleverly on existing literature rather than inventing new theory.
  - **Models are especially strong at counter-examples, discrete math, and number theory.** If your problem lives in graph theory, expect AI to be useful.
  - **The Jacobian conjecture (open since 1939) falls to a subscription model.** Fable (Anthropic) constructed a counter-example. The significance: this is a *general-purpose* model you can subscribe to — the same one that writes your simulation code and improves your emails — not a lab-internal research system. The conjecture sits on Smale's list of problems for the 21st century, alongside the Riemann hypothesis and P vs NP.
  - **The cycle double cover conjecture: a positive result, not just a refutation.** GPT-5.6 Sol Ultra *proved* this key graph-theory conjecture. The method is the notable part: the model was explicitly instructed to spawn **64 agents working in parallel** on different proof strategies, and instructed not to return an answer until it had worked for at least eight hours — though it in fact reached the result in about one hour.
  - **The frontier moved from lab-internal to subscription in roughly a month.** Sandomirskiy is explicit that a month earlier the honest summary would have been "only internal frontier models make real mathematical progress." The Jacobian and cycle-double-cover results changed that.
  - **Why this matters more for economic theory than for math.** Two reasons: the mathematical sophistication bar in economics is lower than at the math frontier, and — crucially — **economists' assumptions are not written in stone**. Counter-example generation, the models' clearest strength, is exactly what the fixed-point workflow needs: drop an assumption, ask whether the theorem survives, and let the model show you it doesn't.
  - Brunnermeier's AlphaGo analogy draws a distinction: the Go move was creative in a different way — exploring a near-infinite space of moves with intuitions about where to search that the best human players lacked, rather than recombining known results cleverly.

- **Summary**

Sandomirskiy takes up the question Episode 1 left hanging: the seven use cases only pay off if models can produce genuine insight rather than fluent recombination. His answer is a qualified yes, and the value of the episode is in how carefully he qualifies it. Rather than relying on the subjective impression that frontier models feel creative — which he and his colleagues share — he goes to mathematics, where correctness is decidable, and walks through four data points in order of increasing strength.

The first is a warning. OpenAI's October 2025 announcement that an internal model had cracked ten open Erdős problems fell apart in a day: Bloom showed the model had surfaced known solutions and presented them as new. Sandomirskiy extracts the right lesson, which is not that models are frauds but that **attribution is a genuine architectural weakness** — a model does not know the provenance of what it produces. Read the other way, the same fact is an underrated strength: no lemma sitting in an unread appendix is ever lost again. Tao's running ledger of the Erdős list keeps this calibrated — 19 of 1,000+ problems touched by AI as of July 2026, roughly 10 with genuinely new proofs, most via bespoke pipelines.

The stronger data points are three conjectures. The unit distance conjecture, open since 1946, was disproved by a counter-example from an internal OpenAI model — with domain experts saying they would accept the proof at any journal. The Jacobian conjecture, open since 1939 and on Smale's 21st-century list next to Riemann and P vs NP, was disproved by Fable, a model available on a consumer subscription. And the cycle double cover conjecture was *proved* — the positive result Ortoleva pushes for on camera, half-joking that he doesn't want to be the guy who only publishes negative results — by GPT-5.6 Sol Ultra running 64 parallel agents under an instruction not to stop before eight hours.

The pattern across all three is consistent with the attribution diagnosis: the arguments were new and unexpected but built on existing ideas used in ways nobody expected to work. No model built new theory. Sandomirskiy's closing argument is that this is *more* than enough for economic theory, both because the technical bar is lower and because the counter-example strength maps directly onto the fixed-point workflow — where the productive question is usually "does the theorem survive without this assumption?"

- **Relevance to Economics Research**

This is the most rigorous treatment of the "is it really creative" question in the wiki, and it is useful precisely because it refuses both easy answers. The attribution/aggregation distinction is the portable idea: a model that cannot tell you where an idea came from but can retrieve anything ever published is a specific kind of instrument, and knowing which kind tells you how to use it and how to check it. For literature review this means the model is an excellent recall device and an unreliable citation source — which is exactly the [[concepts/citation-hallucination]] problem stated at its root cause.

For theorists, the counter-example finding is immediately operational. The models' clearest demonstrated strength is constructing the case that breaks a claim, and that is the single most valuable service a referee provides. Running your propositions past a model with the explicit instruction to find a counter-example is cheap insurance, and unlike proof-checking it has a verifiable output: either the counter-example works or it doesn't.

The Jacobian result carries a separate practical message about access. When a $20–200/month general-purpose subscription model disproves a conjecture on Smale's list, the frontier-capability-versus-consumer-access gap that structures much of the [[concepts/ai-pricing-and-access]] discussion has narrowed sharply — at least for reasoning-heavy, verifiable tasks. And the cycle-double-cover method previews Episode 4's swarm architecture: parallel exploration with a stopping rule is a template economists can run today.

- **Related Concepts**
  - [[concepts/llm-reasoning]]
  - [[concepts/ai-limitations]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/citation-hallucination]]
  - [[concepts/ai-pricing-and-access]]
  - [[concepts/emergent-behavior]]
  - [[concepts/automated-research]]

- **Related Summaries**
  - [[summaries/theory-miniseries-markus-166]]
  - [[summaries/theory-core-uses-markus-166-1]]
  - [[summaries/which-model-markus-166-3]]
  - [[summaries/prompts-swarms-markus-166-4]]
  - [[summaries/vibe-research-2]]
  - [[summaries/openai-automated-researcher]]
