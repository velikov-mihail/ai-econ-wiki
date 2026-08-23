---
title: "Prompts and Agent Swarms (Markus Academy 166-4)"
tags: [summary, prompt-engineering-workflow, economic-theory, multi-agent-systems, context-management]
sources:
  - "[[raw/Clippings/Promtps and Agent Swarms AI for Econ Theory with Ortoleva & Sandomirskiy  Markus Academy  166-4.md]]"
date_updated: 2026-08-23
date_published: 2026-08-04
---

- **Author/Source**: Fedor Sandomirskiy (Princeton), with Pietro Ortoleva — Markus' Academy Ep. 166-4 (4th of 5), hosted by Markus Brunnermeier
- **Original**: [https://www.youtube.com/watch?v=OBJ0h8j_m8Y](https://www.youtube.com/watch?v=OBJ0h8j_m8Y)

- **Key Ideas**
  - **Prompt engineering → context engineering.** The magic-phrase era is over: early models were acutely sensitive to phrasing, which is what made "prompt engineer" a six-figure job title. The broader term now covers designing *what information the model has access to*, not just how the task is worded.
  - **Prompt quality matters most when your model is weakest.** Frontier models (GPT-5.6 Pro, Fable) produce good output even from imperfect context. On Gemini Pro in Google AI Studio, context design is doing real work. This inverts the usual assumption that prompting skill is a frontier-user's game.
  - **Five components of a well-specified prompt**: the question, the information you're supplying (and what each file is), the expected output format (LaTeX, Markdown, code), the quality criteria for a good answer, and **incentives** — most importantly, never ask a model to grade its own output.
  - **Trick 1 — Prompt expansion. The best prompt for a model is written by that model.** Start with a lazy two-liner; ask the model to optimize it, specifying which model will run it and in what environment (web chat vs. agentic), telling it to preserve your intent, and asking it to **fold the contents of attached files into the prompt itself**. A two-line prompt becomes several pages, and you then run the expanded version with nothing attached.
  - Prompt expansion pays off three ways: it saves the tedium of writing pages of spec; **it catches misunderstandings** (reading the expansion shows you whether the model grasped your intent); and it surfaces quality criteria you hadn't thought of, which can fuel your own thinking. Sandomirskiy spends roughly **15 minutes reviewing the expanded prompt** — far less than colleagues who hand-write the whole thing.
  - **Use the same model for expansion and execution.** Brunnermeier asks whether one could design the prompt in Gemini and run it in Fable; Sandomirskiy's answer is no — a model knows what *it* likes as input, and Gemini has no idea about Fable 5's prompting quirks because Fable postdates its training data.
  - **Worked example.** In a paper with coauthors, Theorem 1 assumes the games are regular. The two-line prompt: look at Theorem 1 in the attached paper, either prove it without regularity or construct a counter-example; if you find a counter-example, brainstorm alternative assumptions. Run through prompt expansion (with the paper attached, definitions folded in), then executed. **Both Gemini Pro and GPT-5.5 Pro constructed counter-examples** — regularity can't be dropped. The difference: Gemini failed to suggest interesting alternative assumptions, while ChatGPT Pro proposed one the authors would have put in the paper.
  - **One task per prompt** — and the weaker your model, the more this matters. The three-part prompt above is only safe on a frontier Pro subscription; otherwise decompose and run in parallel.
  - **Trick 2 — Prover vs. verifier as a zero-sum game.** Models like to please the user: if it senses you want the conjecture proved, it will try to look like it has a proof. So run **two instances of your best model in parallel**, one proving and one hunting for gaps, and feed minor gaps back to the prover for a few cycles. Use a different *instance*, not necessarily a different model — always use the best model you have.
  - **Trick 3 — Add a judge when the game isn't zero-sum.** When one instance proposes a direction (a new assumption, a reformulated statement) there's no objective right answer, so the critic's objections can't simply be scored. Introduce a **third instance as judge**, fed both outputs, to assess whether the criticism is valid. In agentic environments such structures can be built automatically from a single prompt.
  - **Trick 4 — Never feed PDFs.** PDFs look like text to humans but not to models. Attaching one forces the model to convert it first, which **pollutes and consumes the context window** and distracts it from the actual task. Feed LaTeX if you have it; if all you have is a PDF, run a separate conversion to Markdown first and attach that. This "makes a big difference" for proofreading, and matters most for models without huge context windows.
  - **Trick 5 — Summarize and restart.** Long back-and-forth conversations, tool calls, and PDF conversions all accumulate in the context window, and "as for people, when we keep a lot of things in our mind, it distracts us from what is relevant." Ask the model to summarize the session's relevant insights into a Markdown file, then attach that to a fresh instance.
  - **The swarm recipe, reverse-engineered from OpenAI's published cycle-double-cover prompt.** Three explicit instructions: (1) **run for at least eight hours**; (2) **spawn 64 agents** exploring different proof strategies in parallel; (3) the **supervising agent must eliminate agents that have converged on the same direction**. Diversity of approach is enforced, not hoped for — converged agents get restarted.
  - **Sandomirskiy's own addition — the escape hatch.** In an agentic environment you often can't run the most intelligent model. So instruct the swarm: if you are stuck for an hour, write the blocking obstacle to a Markdown file, hand it up to the best model you *can* access, and paste that model's suggestion back so the swarm keeps grinding. **Running Sol Ultra this way for 15 hours cracked a conjecture he and his coauthors had worked on for almost a year.** This is the concrete way to combine stamina and intelligence that Episode 3 promised.
  - **Proofreading**: AI catches not just typos but major logical gaps and subtle inconsistencies. Dedicated tools — Refine.ink (covered earlier on Markus Academy by Benjamin Golub), coarse.ink, reviewer3.com — are best saved for a polished draft right before submission. Along the way, do DIY proofreading: a two-line "proofread the attached paper for [target audience]" run through prompt expansion, producing a long prompt with sections for typos, storytelling, proof gaps. Split it into narrow prompts if your model is weak — or ask the expansion step to generate the split for you.
  - **Because AI is non-deterministic, run proofreading prompts multiple times.** Each pass surfaces new subtle issues — "and maybe hallucinate a few as well."
  - **Wrap what works into a reusable artifact.** Sandomirskiy keeps a **custom GPT for proofreading** with a fixed target audience, built from a prompt expansion he was happy with, so he never re-expands. Brunnermeier notes Anthropic's Skills do the same job.
  - **Delegate only the easy fixes.** Have the model collect typo-level issues into a Markdown file and hand that to an agent to apply. Major issues discovered in proofreading "should not be outsourced to an AI."

- **Summary**

This is the operational episode, and the densest in the series. Sandomirskiy's framing is that prompt engineering as a craft of magic phrases has been absorbed into context engineering — designing what the model knows, not how you phrase the ask — and that the payoff to doing it well is *inversely* related to how good your model is. Someone on a $200/month Pro subscription can be sloppy; someone on free-tier Gemini cannot.

The central technique is prompt expansion: write a lazy two-liner, have the same model that will execute it turn it into a multi-page specification with the contents of your attachments folded in, spend fifteen minutes reading the result, then run it. The three benefits compound — you skip the tedium, you catch misunderstandings before burning a long run on them, and you see quality criteria you would not have specified. Sandomirskiy insists the expansion and execution model be the same, because a model knows its own preferences and cannot know a newer model's. His worked example — asking whether a regularity assumption in his own Theorem 1 can be dropped — shows both the method and a clean capability comparison: Gemini Pro and GPT-5.5 Pro both found the counter-example, but only ChatGPT Pro proposed a replacement assumption good enough to put in the paper.

The verification architecture follows from a behavioral claim: models want to please, so a session asked to check its own proof will find it correct. The fix is structural rather than rhetorical — a prover instance and a verifier instance of the same (best available) model, running as a zero-sum game, with minor gaps cycled back. When the task has no objective answer, as when the model proposes a new assumption, a third instance acts as judge over the exchange. Two mechanical points round out the single-session advice: never attach a PDF (convert to Markdown or use LaTeX, because conversion eats context and distracts the model), and summarize-and-restart when a session gets long.

The last section is the swarm. Reading OpenAI's published cycle-double-cover prompt, Sandomirskiy extracts three reusable instructions — a minimum eight-hour runtime, 64 agents on divergent proof strategies, and a supervisor that kills agents which have converged, forcing diversity. His own contribution is an escape hatch for the intelligence-stamina tradeoff: let a stuck agent write its blocking obstacle to Markdown, escalate that file to the smartest model you can reach, and paste the answer back down to the swarm. Fifteen hours of that cracked a year-old conjecture that neither GPT-5.6 Pro nor Fable had solved on its own.

- **Relevance to Economics Research**

Nearly all of this transfers out of theory. **Prompt expansion** is the highest-leverage habit in the episode and costs nothing to adopt — it is a general answer to the complaint that good prompts are too tedious to write, and the fifteen-minute review is a genuine error-catching step, not ceremony. The **same-model rule** is a specific, testable claim worth knowing.

The **prover/verifier/judge stack** is the theory-side version of the adversarial verification discipline that runs through this wiki — Cunningham's Referee 2, multi-agent DiD auditing, Haaland's schema-validated reviewers. Sandomirskiy adds the mechanism: sycophancy is the reason self-grading fails, so the fix has to be architectural. Empirical economists should read "never let a session grade its own regression output" for the same reason.

**Never feed PDFs** is the most immediately useful mechanical tip for economists, whose inputs are overwhelmingly PDFs — working papers, referee reports, published articles. Converting to Markdown first is a small step that measurably improves output and preserves context window.

The **escape hatch** is the most original idea in the series and generalizes past proofs: any long autonomous run — a replication sweep, a large text-classification job, a multi-day data-cleaning agent — can be given a protocol for writing down what blocked it and escalating to a stronger model. That is a cheap way to buy frontier intelligence at the few moments it matters without paying frontier prices for the whole run, and it directly addresses the cost problem from [[summaries/which-model-markus-166-3|Episode 3]].

Finally, **non-determinism as a reason to re-run** is a point economists should find natural and often miss in practice: if the output distribution is non-degenerate, one draw is not an answer. Running a proofreading or review prompt several times and pooling findings is the sampling logic applied to AI output — with the standard caveat that some of the extra findings will be hallucinated and need screening.

- **Related Concepts**
  - [[concepts/prompt-engineering]]
  - [[concepts/context-management]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/sycophancy-and-bias]]
  - [[concepts/human-in-the-loop]]
  - [[concepts/document-processing]]
  - [[concepts/ai-peer-review]]
  - [[concepts/claude-code-skills]]

- **Related Summaries**
  - [[summaries/theory-miniseries-markus-166]]
  - [[summaries/which-model-markus-166-3]]
  - [[summaries/ai-creativity-markus-166-2]]
  - [[summaries/prompting-insights-golub]]
  - [[summaries/refine-ink-golub]]
  - [[summaries/coarse-ink]]
  - [[summaries/cc-series-24-agents-auditing-did]]
