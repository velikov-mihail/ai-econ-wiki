---
title: "AI for Economic Theorists & Mathematicians (Markus Academy 166 Mini-Series Overview)"
tags: [summary, academic-research, economic-theory, ai-agents, prompt-engineering]
sources:
  - "[[raw/Clippings/AI for Economic Theorists & Mathematicians, a Mini-Series.md]]"
date_updated: 2026-08-23
date_published: 2026-08-03
---

- **Author/Source**: Pietro Ortoleva & Fedor Sandomirskiy (Princeton), Markus' Academy Ep. 166 mini-series — hosted by Markus Brunnermeier, with support from Pablo Balsinde (Stockholm School of Economics)
- **Original**: [https://markusacademy.substack.com/p/ai-for-economic-theorists-and-mathematicians](https://markusacademy.substack.com/p/ai-for-economic-theorists-and-mathematicians)
- **Slides**: [Google Drive](https://drive.google.com/file/d/1PL2-1CE3Qd57l0VnS7As4TfMqRvPJHw2/view?usp=sharing)

- **Key Ideas**
  - The follow-up to the Markus Academy mini-series on [Claude Code for applied economists](https://markusacademy.substack.com/p/claude-code-for-applied-economists), this time for **theorists**. Four episodes released (a fifth to follow).
  - **Episode 1 — Theory as a fixed point.** Unlike mathematics, economic models do not try to prove a conjecture; they illustrate a mechanism. Writing a theory paper is therefore a search for a fixed point — iterating over defensible assumptions and proofs until they jointly deliver the desired insight. AI's contribution is to **speed up the iterations**, not to replace the search. Seven use cases; sketching is the most underused.
  - **Episode 2 — Can AI be creative?** Model quality in econ theory is subjective, so look to math for evidence, where a proof either holds or it doesn't. Verdict: **poor at attribution, fantastic at aggregation**, and genuinely strong at counter-examples.
  - **Episode 3 — Which model.** **Intelligence and stamina are substitutes.** Their verdict for theory today: GPT-5.6, narrowly over Fable, because stamina beats raw intelligence when you can run for hours.
  - **Episode 4 — Prompting, adversaries, and swarms.** Prompt engineering has given way to **context engineering**; let the model expand your two-liner into the prompt; never let a session grade its own work; and the 64-agent swarm behind the cycle-double-cover proof is a reusable template.
  - Recurring theme across all four: **verification must be external**. Prover/verifier/judge separation, hostile-referee attacks, and counter-example hunting all put the model in an adversarial rather than an approving role.
  - Also recurring: **the risk of AI-driven rabbit holes scales with your own ignorance** — the less you know about the area, the longer you will chase a plausible-sounding dead end.

- **Summary**

This is the landing page for a four-part Markus Academy mini-series in which two Princeton theorists — Pietro Ortoleva and Fedor Sandomirskiy — work through what AI is and is not currently good for in economic theory and mathematics. It is the theory-side counterpart to the earlier Goldsmith-Pinkham series on Claude Code for applied economists, and the framing is deliberately different: applied economists have data pipelines to automate, theorists have a fixed-point search to accelerate.

Ortoleva's organizing metaphor (Episode 1) is the most portable idea in the series. A theory paper is not a proof of a pre-specified conjecture; it is a simultaneous search over assumptions, model structure, and results, iterated until the pieces cohere into something both defensible and interesting. AI does not solve the fixed-point problem, but it collapses the cost of each iteration — sketching three candidate models from a vague intuition, checking whether a proposed proof survives, suggesting which assumption would rescue a false statement. He is explicit that "reliable" does not mean submittable: frontier models can prove the results in an economist's typical notation-heavy model, but the output is raw material, not a draft.

Sandomirskiy's contribution (Episodes 2 and 4) supplies the empirical evidence and the operational recipe. On creativity, the honest reading of the record is mixed: the October 2025 claim that GPT-5 had cracked ten open Erdős problems collapsed under scrutiny when Bloom showed the model had merely surfaced known solutions — a failure of attribution, not of retrieval. The flip side is real and underrated: no lemma buried in an unread appendix is ever lost again. Where models have clearly produced new mathematics is in **counter-examples** — the unit distance conjecture and the Jacobian conjecture both fell to model-found disproofs — and in **parallel exploration**, where Sol Ultra proved the cycle double cover conjecture running 64 agents. Episode 4 turns that into a template: swarms with a supervisor that kills converging agents, an escape hatch letting a stuck agent write its blocking obstacle to a Markdown file for escalation to a stronger model, and strict prover/verifier/judge separation. Sandomirskiy reports that running Sol Ultra this way for fifteen hours cracked a conjecture he and his coauthors had worked on for a year — one that neither GPT-5.6 Pro nor Fable had solved on their own.

Episode 3 is the practical buying guide, and rests on the series' sharpest general claim: **intelligence and stamina are substitutes**. A weaker model run for a long time in an agentic environment often gets further than a smarter model run briefly in a browser — and many of the deepest models are neither built nor priced for twenty consecutive hours of work.

- **Relevance to Economics Research**

Almost all existing wiki coverage of AI in economics is applied: data pipelines, replication, empirical verification, referee reports. This series fills the theory gap, and does so without either of the two usual distortions — it neither claims models are inventing new economics nor dismisses them as autocomplete.

Three things transfer beyond theory. First, the **fixed-point framing** generalizes: any research process whose bottleneck is iteration cost rather than execution cost gets faster in proportion to how cheap each iteration becomes, which is a cleaner way to predict where AI helps than "is the task hard." Second, **intelligence-versus-stamina** is a resource-allocation rule any researcher can apply to their own subscription budget — and it explains why agentic setups outperform browser chats on long tasks even when the browser model is smarter. Third, the **adversarial verification stack** (prover, verifier, independent judge; never let a session grade its own work) is exactly the discipline empirical economists need for AI-assisted analysis, where the failure mode is a confident, plausible, wrong result. The counter-example finding is the most encouraging for theorists specifically: a model that reliably finds the case that breaks your proposition is doing referee work that is genuinely hard for humans and genuinely valuable.

The rabbit-hole warning — that wasted time scales with your own ignorance — is the series' version of the domain-expertise argument that runs through the rest of this wiki.

- **Related Concepts**
  - [[concepts/llm-reasoning]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/ai-agents]]
  - [[concepts/prompt-engineering]]
  - [[concepts/context-management]]
  - [[concepts/domain-expertise-vs-ai-skills]]
  - [[concepts/ai-limitations]]
  - [[concepts/research-quality]]

- **Related Summaries**
  - [[summaries/theory-core-uses-markus-166-1]]
  - [[summaries/ai-creativity-markus-166-2]]
  - [[summaries/which-model-markus-166-3]]
  - [[summaries/prompts-swarms-markus-166-4]]
  - [[summaries/prompts-to-paper]]
  - [[summaries/vibe-research-2]]
  - [[summaries/getting-started-economists]]
