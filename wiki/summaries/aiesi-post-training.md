---
title: "Post-Training LLMs (AIESI 2026)"
tags: [summary, institutional-societal, post-training, reinforcement-learning, llm-reasoning, ai-agents]
sources:
  - "[[raw/pdfs/aiesi_post-training_public.pdf]]"
date_updated: 2026-08-23
date_published: 2026-08
---

- **Author/Source**: Kawin Ethayarajh (Assistant Professor of Applied AI, University of Chicago Booth) — AI and Economics Summer Institute 2026, Chicago, August 6–11, 2026
- **Original**: [https://kawine.github.io/assets/aiesi_post-training_public.pdf](https://kawine.github.io/assets/aiesi_post-training_public.pdf)

## Key Ideas

- **"The model you use is not the model that was pretrained."** Pretraining learns a distribution over text; a plausible continuation is not a useful response. Post-training converts a base model into a *behavioral policy* — a mapping from context to response — with goals spanning interface (instruction following, tool calls), capability, preference, safety, and product constraints.
- **Post-training ≠ alignment.** Post-training answers "when in the lifecycle?"; alignment answers "aligned to what objective?" Most alignment happens in post-training, but not all post-training is alignment.
- **Six-stage stack**: SFT (imitate) → offline preference optimization (compare) → online RL (explore) → RLVR and environments (verify) → distillation (transfer) → world adaptation (anticipate).
- **SFT is imitative and leaves information on the table.** It teaches formats and routines and creates a stable interface, but cannot express *which* of n valid options is better, *how costly* a mistake is, or what happens under the model's own mistakes. Data quality dominates quantity — LIMA found 16× more examples gave no measured gain.
- **Offline preference methods** (DPO, IPO, SimPO, ORPO) optimize a *relative* likelihood margin and share pathologies such as likelihood displacement (both chosen and rejected log-likelihoods fall). Ethayarajh's own **KTO** instead scores each response separately as desirable/undesirable, with a prospect-theoretic (reference-dependent) utility function implicit in the loss — and, unlike paired objectives, needs no SFT warm start.
- **Economics shows up inside the machinery**: Bradley–Terry utility underpins reward models; KTO embeds Kahneman–Tversky prospect theory; the Stanford Human Preferences dataset (385K comparisons scraped from Reddit askacademia-style forums) was the only academic dataset used to post-train Llama 2.
- **Online RL** (REINFORCE → PPO → GRPO) makes the training distribution move with the model. GRPO drops PPO's learned critic in favor of a within-prompt group baseline — less memory, better throughput. Most rewards are sequence-level; token-level credit assignment largely does not work.
- **"Post-training is a principal-agent problem with an extremely capable agent."** We can only optimize what we can measure, and optimization pressure exposes every gap between proxy reward and true goal (reward overoptimization: measured reward rises while actual quality falls).
- **Verifiability × grindability** as a two-dimensional map of feedback economics: coding and formal proofs are cheap-to-verify and fast-to-grind; **economics papers, clinical care, and sales are neither**. A cheap verifier turns inference compute into training data — which is why RLVR scales predictably (early fits predict 100,000-GPU-hour runs) while RLHF on a learned proxy plateaus.
- **The bottleneck is shifting from examples to environments.** An RL environment is a sandbox — realistic state, tools with realistic permissions and failure modes, a task generator at the policy's frontier, a simulator, a shortcut-resistant verifier, and reproducibility.
- **On-policy distillation** asks the teacher to score the *student's own* trajectories, giving dense per-token credit where RLVR gives one bit at the end. In the cited experiment this copied an RL-discovered policy with 7–10× fewer gradient steps and 50–100× less compute.
- **World adaptation / "mecha-nudges"** (Frey & Ethayarajh 2026): post-training assumes the environment is exogenous, but once agents matter, humans redesign content and interfaces *for machines*. A mecha-nudge increases machine-usable information without materially degrading human-usable information — distinct from prompt injection, SEO, and adversarial examples. Etsy evidence: post-ChatGPT listings gained >40% of the maximum possible increase in machine-usable information, and conditional on seller fixed effects, one extra bit of machine-usable information is associated with **+43.5%** reviews for agent-selected listings post-ChatGPT versus **−18.1%** pre-ChatGPT.

## Summary

Ethayarajh's AIESI lecture is a technical tour of everything that happens *after* pretraining, pitched at economists. The organizing claim is that the deployed model is a behavioral policy, not a text predictor, and that each post-training stage differs mainly in what its feedback format can express. SFT records an exact target and teaches formats; preference methods record a winner and a loser and teach relative ordering; KTO records a single desirable/undesirable label and restores an absolute anchor. Online RL adds exploration — the policy generates its own rollouts, so the training distribution moves with the model — and REINFORCE, PPO, and GRPO are presented as one policy-gradient core with different baselines and update constraints.

The second half is about where reward comes from. Ethayarajh frames post-training explicitly as a principal-agent problem: we optimize the measured proxy, and under enough optimization pressure the policy finds the proxy's blind spots. That reframes RLVR's success — programmatic checkers are near-zero marginal cost, millisecond latency, and admit millions of attempts, so verifiable domains (code, math) scale predictably while learned-proxy RLHF plateaus. The consequence is a shift in the binding constraint from curated examples to *environments*: realistic sandboxes with tools, task generators, simulators, and shortcut-resistant verifiers. On-policy distillation then appears as the efficiency lever — once expensive RL finds a policy, dense token-level teacher signal on the student's own trajectories copies it orders of magnitude more cheaply, which is also how parallel domain experts get merged back into one model.

The deck closes on original economics research. Post-training treats the deployment environment as fixed, but agents that search, rank, recommend, and purchase change economic payoffs, and people respond by redesigning the environment — a feedback loop, not ordinary covariate shift. "Mecha-nudges" are transformations that raise machine-usable information while preserving human-usable information. Using Etsy listings around ChatGPT's release, Ethayarajh and Frey document both the adaptation and its payoff, robust across prompts, labels, model families, controls, and placebos, and stronger where AI use is less taboo. The open questions are identification in deployed systems, agent–environment co-evolution and equilibrium, welfare incidence, and governance.

## Relevance to Economics Research

Three distinct payoffs. First, **mechanism literacy**: economists who understand that a model is a policy trained against a measurable proxy can reason about *why* LLM outputs behave as they do — sycophancy, refusal patterns, format rigidity, and reasoning style are training artifacts, not personality. Second, **the verifiability map is a direct statement about our own field's exposure**: Ethayarajh places economics papers in the hard-to-verify, slow-feedback quadrant, which explains why agents improve fastest at coding and slowest at judgment-heavy research, and predicts where the gains will and will not arrive. Third, **mecha-nudges open a genuine research agenda** — an economics of environments adapting to machine readers, with implications for search, marketing, platform design, disclosure regulation, and measurement. The deck also supplies unusually clean examples of economic theory embedded in ML practice (Bradley–Terry utility in reward models, prospect theory in KTO), and the principal-agent framing of reward specification is a ready-made bridge for contract theorists.

## Related Concepts

- [[concepts/llm-reasoning]]
- [[concepts/ai-limitations]]
- [[concepts/hard-vs-easy-tasks]]
- [[concepts/sycophancy-and-bias]]
- [[concepts/agentic-ai]]
- [[concepts/open-source-models]]

## Related Summaries

- [[summaries/bitter-lesson]]
- [[summaries/ai-progress-mental-model]]
- [[summaries/which-model-markus-166-3]]
- [[summaries/kazinnik-cemfi-day1]]
- [[summaries/shape-of-ai]]
