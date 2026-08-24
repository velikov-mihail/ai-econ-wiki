---
title: "Which Model to Use for Theory (Markus Academy 166-3)"
tags: [summary, ai-tools, economic-theory, ai-pricing-and-access, ai-agents]
sources:
  - "[[raw/Clippings/Which Model to Use AI for Economic Theory with Ortoleva & Sandomirskiy  Markus Academy  166-3.md]]"
date_updated: 2026-08-23
date_published: 2026-08-04
---

- **Author/Source**: Pietro Ortoleva (Princeton), with Fedor Sandomirskiy — Markus' Academy Ep. 166-3 (3rd of 5), hosted by Markus Brunnermeier
- **Original**: [https://www.youtube.com/watch?v=lLgD9WwFMvM](https://www.youtube.com/watch?v=lLgD9WwFMvM)

- **Key Ideas**
  - Ortoleva opens by flagging that this is the episode most likely to date — it reflects the state of the art as of late July 2026 — so he tries to isolate the durable structural point from the transient model rankings.
  - **The durable point: intelligence and stamina are substitutes.** Drawn on camera as an Econ 101 two-good diagram. *Intelligence* is the depth of theory the model can develop; *stamina* is how long it will grind. Fable 5 sits at high intelligence, low stamina; Sol Ultra at lower intelligence, very high stamina; GPT-5.6 Pro in between and, in their testing, close to Fable on depth.
  - **Stamina is two constraints, not one.** Price: running Fable for an 80-hour proof attempt "will consume thousands and thousands of dollars with an uncertain outcome" — which Ortoleva does not see academic research accounts absorbing any time soon. And *design*: some models simply aren't built to be told "spend at least 20 hours on this." In Codex you can literally issue that instruction, plus "create multiple agents," and the system is built to comply.
  - **The frontier timeline, by FrontierMath Tier 4 accuracy.** Pre-Fable: ChatGPT 5.4 Pro and 5.5 leading, an unreleased internal Gemini model near them, Claude 4.8 clearly below. **Fable 5** then overtook 5.5 outright at ~88, the highest ever recorded on the benchmark, delivering intuition deep enough that "people were falling in love with Fable." **But access broke**: Fable was taken offline for government intervention and is now API-only, with complicated and expensive pricing. **July 9**: OpenAI released GPT-5.6 Pro (browser, successor to 5.5, no Tier 4 score yet but apparently comparable to Fable) and **Sol Ultra** in ChatGPT Work, which runs many agents in parallel under a regular Pro subscription — far easier to bill to a university than API pricing, and significantly cheaper than API even so. Then **Opus 5** from Anthropic, "not quite Fable but trying to catch up." Four weeks between major releases: "this is the pace we should be expecting now."
  - **The verdict: GPT-5.6 Pro, narrowly.** Fable may be a little deeper, but 5.6 Pro's stamina advantage is large enough to outweigh it — with the caveat that Anthropic is changing access policy fast.
  - **Budget-tiered recommendations** (as of late July 2026):
    - **Pro (~$200/month)**: GPT-5.6 Pro in the browser *plus* Sol Ultra in ChatGPT Work. That combination is "the right one."
    - **$20/month**: OpenAI Plus over Claude — though Opus 5 may change that verdict.
    - **Free**: **Gemini Pro via Google AI Studio**, described as "a wonderful tool." Most of what the series covers for basic economic theory research "can be confidently solved" there. "You're not going to prove the Riemann conjecture, but it's an incredibly useful tool."
  - **Access inequality is now a research-capability issue.** Ortoleva stresses that it genuinely matters which tier you can afford, and that $200/month is expensive for many researchers.
  - **Browser or agents?** For empirical work, agentic "is where all the action is." For *theory*, the browser version of GPT-5.6 Pro is currently the best you can do for the core proof and brainstorming work. Agents earn their place on the **non-proof** parts — organizing literature, writing referee reports, managing folders, long multi-step jobs — and on problems that genuinely need stamina, where Sol Ultra decides how many agents to deploy.
  - **Matching problems to the tradeoff is an emerging skill.** Some problems reward creativity and out-of-the-box thinking; others just need grinding. Ortoleva is explicit that the model won't make this call for you and that he and Sandomirskiy are only starting to develop the judgment themselves. Brunnermeier's on-camera question — "where's your indifference curve?" — gets the honest answer: it depends on budget, and it varies by problem.

- **Summary**

This is the buying-guide episode, and Ortoleva handles the obvious problem — that any model ranking published in August 2026 is already decaying — by separating the ranking from the framework. The framework is a single tradeoff drawn as an indifference-curve diagram: intelligence and stamina are substitutes, and the right point on the frontier depends on your budget and on the problem.

The empirical content behind the diagram is a four-week sprint at the frontier. Fable 5 set a record on FrontierMath Tier 4 and impressed theorists enough that colleagues were talking about it in the corridors — and then became hard to actually use, taken offline for government intervention and returning as an expensive API-only product. OpenAI's response on July 9 was two-pronged: GPT-5.6 Pro in the browser at roughly comparable depth, and Sol Ultra in ChatGPT Work, which spawns parallel agents under an ordinary Pro subscription. Opus 5 followed. The access point matters as much as the capability point: a model billed through a Pro subscription is administratively feasible for a university, and API pricing at scale generally is not.

The stamina argument is the part worth keeping. Ortoleva's claim is that a slightly shallower model that grinds for twenty hours frequently beats a deeper model you can only afford to run briefly — and that this is not merely a price artifact. Some models aren't designed to be pushed: telling Fable to spend twenty hours on a problem doesn't really work, while Codex-style agentic environments treat exactly that instruction as native. He also concedes the honest uncertainty: theoretically a Pro model should manage sustained work, but whether it does in practice is unclear, and Episode 4's escalation trick is the workaround they've developed.

On browser versus agents, the theory answer diverges from the empirical one. Empiricists should be agentic. Theorists, for the core proof and brainstorming work, are currently best served by a browser session with the deepest model available — with agents reserved for the surrounding infrastructure (literature, referee reports, file management) and for problems where sheer persistence is the binding constraint.

- **Relevance to Economics Research**

The intelligence-versus-stamina frame is the most useful takeaway and outlasts every specific model named. It reframes model choice from "which is smartest" — the question the benchmark leaderboards answer — to "which point on the frontier fits this problem and this budget," which is a question economists are well equipped to reason about. It also explains an otherwise puzzling pattern reported throughout this wiki: agentic setups routinely outperform browser chats on long research tasks even when the browser model scores higher, because sustained iteration is doing the work.

The budget tiers make the [[concepts/ai-pricing-and-access]] problem concrete. There is now a defensible answer at every price point, including free — the Gemini Pro / Google AI Studio recommendation is the single most useful line for graduate students and researchers at institutions without AI budgets, and Ortoleva's framing is right: a free tool that handles most basic theory tasks is still a large advantage over no tool. (The tradeoff he notes elsewhere in the series is that AI Studio chats train Google's models, which matters for unpublished work.)

The browser-versus-agents split is a useful corrective to agentic maximalism. For theorists specifically, the recommendation is *not* to build an agent harness for proof work — the frontier browser model is better today — but to use agents for the surrounding scaffolding. That is a different allocation than the applied economists in the companion [[summaries/getting-started-economists|Ep. 162 series]] arrive at, and the difference traces directly to whether your bottleneck is executing a pipeline or thinking through a fixed point.

Finally, the four-week release cadence is itself a planning input: any workflow that hard-codes a specific model will need revisiting roughly quarterly.

- **Related Concepts**
  - [[concepts/ai-tools-landscape]]
  - [[concepts/ai-pricing-and-access]]
  - [[concepts/cost-and-budget]]
  - [[concepts/ai-agents]]
  - [[concepts/llm-reasoning]]
  - [[concepts/data-privacy]]

- **Related Summaries**
  - [[summaries/theory-miniseries-markus-166]]
  - [[summaries/ai-creativity-markus-166-2]]
  - [[summaries/prompts-swarms-markus-166-4]]
  - [[summaries/guide-which-ai]]
  - [[summaries/chatgpt-vs-claude]]
  - [[summaries/vibe-research-2]]
