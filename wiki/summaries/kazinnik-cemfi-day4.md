---
title: "Economics with LLMs — Day 4: Synthetic Agents, Simulations, and Counterfactuals"
tags: [summary, finance-econometrics, synthetic-agents, homo-silicus, multi-agent-systems, survey-methods]
sources:
  - "[[raw/pdfs/kazinnik_cemfi2026_day4.pdf]]"
date_updated: 2026-08-23
date_published: 2026-08-20
---

- **Author/Source**: Sophia Kazinnik (Digital Economy Lab, Stanford University) — *Economics with LLMs*, CEMFI Summer School 2026, Day 4 of 5, August 20, 2026
- **Original**: [https://www.sophiakazinnik.com/cemfi2026/day4.pdf](https://www.sophiakazinnik.com/cemfi2026/day4.pdf)

## Key Ideas

- **Simulation as a laboratory, not a data substitute.** LLM simulations are cheap, fast, and flexible, and let researchers model scenarios that are hard, slow, or risky to field with humans. The prescribed workflow is `theory → human validation → scaled simulation → external test`. "The research opportunity here is not replacing data, but **expanding the design space**."
- **Homo silicus** (Horton): *homo sapiens* is an actual human, *homo economicus* a mathematical model of one, *homo silicus* an LLM used as a computational model of one. Like *homo economicus* it can be wrong in many ways and still be useful. Instead of solving a model analytically, you instantiate an agent and observe repeated choices while varying information, preferences, status quo, and incentives. **Failures are informative** — they reveal where the model's behavioral representation departs from humans.
- **Simulation is experimental design**: the required number of runs follows the standard power formula `n = 2((z_0.975 + z_0.80)σ/Δ)²`, with σ the variation across runs and Δ the effect to detect. More noise or smaller effects mean more runs.
- **"Persona prompts are bundles."** A phrase like "you are wealthy" moves wealth, age, politics, risk tolerance, and norms *together*. A clean treatment pins the whole trait vector and varies only the coordinate of interest. And matching the mean response is not enough — check spread and relationships too.
- **A commercial ecosystem already exists**: Aaru (synthetic audiences, ~$1B headline valuation, Redpoint-led Series A Dec 2025, Interpublic partnership); Simile (grounded twins, $200M Series B at $2B in July 2026, founded by Joon Sung Park, Michael Bernstein, Percy Liang); Ipsos × Stanford PASCL (digital-twin panels validated on KnowledgePanel infrastructure); Qualtrics synthetic panels inside the survey stack; Expected Parrot (open-source, model-agnostic, with built-in human-validation workflows).
- **Bank run simulation.** Diamond–Dybvig (1983) frames runs as driven by a "shift in expectations" that could arise from almost any stimulus — which makes them ideal for simulation. Kazinnik crosses gender × income (5 bands) × education (4) × age (5) into **200 unique demographic groups**, then exposes synthetic depositors to six communication treatments plus a placebo: bank email, bank text, President message, Fed message, cautionary tale (a Reserve Bank tweeting a Great Depression bank-run article), network effect, and a weather-report placebo.
- **Eight models are benchmarked against 1,158 real Prolific respondents** (GPT-4o, GPT-4o-mini, GPT-4.1, o3, Gemma-2-27B, Qwen-2.5-72B, Llama-3.3-70B, DeepSeek-R1), 1,600 synthetic respondents each. **Model dispersion is enormous**: against a human baseline withdrawal rate of 47.6%, GPT-4.1 gives 97.5% and GPT-4o-mini 33.0%. Under the Fed-message treatment humans withdraw 34.5% while GPT-4o-mini and Llama go to ~0–2.5%. **Level-matching is model-specific; no model is a drop-in human.**
- **Bias is defined and estimated cell by cell**: `Δ_g = Pr(Y=1|g)_LLM − Pr(Y=1|g)_Human` over age × gender × education × income × treatment cells. Reported mean bias and R² from projecting Δ on cell characteristics: GPT-4o has mean bias 0.000 (R² 0.422), Gemma 0.194 (0.363), Qwen −0.224 (0.358), GPT-4.1 +0.494 (0.152). **The R² is the useful statistic** — a model with large but *predictable* bias can be corrected; a model with small but unstructured bias cannot.
- **Substantive findings survive**: age lowers withdrawal propensity; income and education raise it; every authoritative message (bank email/text, Fed, President) sharply reduces withdrawal intent, while the network effect dominates everything (probit coefficient +5.00). Message effects vary across population groups, which is the argument for **targeted crisis communication**. Free-text explanations from synthetic agents reproduce recognizably human mental models — FDIC insurance, trust and doubt, financial constraints, social panic, institutional credibility.
- **What is actually inside an agent**: `Agent = LLM + Instructions + State + Tools + Loop`. "The 'agent' is mostly **orchestration around an LLM**." From *homo economicus* (explicit optimization) through ABMs (behavioral rules, bounded rationality) to LLM agents (context-sensitive, language-native, able to process unstructured information and communicate).
- **Frameworks versus modeling**: LangChain (agent toolkit), LangGraph (flowchart/state machine), OpenAI Agents SDK (lightweight runtime), AutoGen (group chat), CrewAI (organization chart). "These frameworks do not give you the economic model, but the infrastructure for running it." Three interaction structures — manager, handoff, discussion — and **"the important modeling choice is the interaction structure, not the infra."**
- **Survey augmentation motivation is a real crisis**: surveys are expensive and slow, response rates are falling, non-response is demographically patterned, online panels breed professional respondents and identity misrepresentation, and **respondents are themselves now using LLMs** (Veselovsky et al. 2023; Zhang et al. 2025).
- **A systematic replication study**: UK willingness-to-accept data (Coyle & Nguyen 2023, categorical) and PSID (continuous), varying persona (expert advisor versus simulated own perspective), prompting strategy, model family (OpenAI versus Llama), fine-tuning, RAG, and temperature — benchmarked against OLS/multinomial logit *and* against **300 real human predictors** achieving 0.413 accuracy at one month (versus 0.111 random). Human prediction accuracy is the ceiling to beat.
- **Findings**: accuracy rises with the *value of data supplied* (demographics + benchmark valuations > benchmark alone > demographics alone); fine-tuning and RAG deliver significant boosts (GPT-4o-mini fine-tuned reaches 0.652, +17.06%); **prompt technique and temperature matter less than expected**; simpler models can beat reasoning models depending on task; accuracy exceeds 0.90 for some digital goods; valuations for young, wealthy, educated respondents may be *overestimated*, while accuracy is surprisingly high for low-income and 65+ respondents.
- **Five best practices**: ground agents in granular benchmarks (other WTA responses, last-wave income); prefer open-weight models for stability and fine-tune where possible; validate against humans and report both human accuracy and a **test–retest ceiling**; monitor heterogeneity to know where agents over- and under-estimate; and **correct bias before using at scale**.

## Summary

Day 4 asks when a simulation is useful enough. Kazinnik's answer is that an LLM agent is a measurement instrument like any other, and the *homo silicus* framing licenses its use the same way *homo economicus* is licensed — not because it is right, but because a tractable, manipulable, wrong model can still isolate mechanisms. What follows is a practical discipline for that use: treat run counts as a power calculation, recognize that persona prompts move whole bundles of traits rather than single coordinates, and check the distribution and correlation structure rather than only the mean.

The bank-run study is the day's centerpiece and its most sobering exhibit. Two hundred demographic cells crossed with seven communication treatments, run across eight LLMs and benchmarked against 1,158 human respondents, produce a table in which the same treatment yields withdrawal rates anywhere from 0% to 100% depending on which model you asked. Any conclusion drawn from a single unvalidated model would be arbitrary. What survives the comparison is not levels but structure — the demographic gradients, the ordering of treatment effects, the dominance of the network effect, and the qualitative content of agents' stated reasons, which map onto recognizably human categories. Kazinnik formalizes the fix by defining bias at the demographic-treatment cell level and reporting how much of it is *predictable*, which is the quantity that determines whether a model can be corrected rather than merely ranked.

The day then zooms out twice. First to agent architecture: an agent is an LLM plus instructions, state, tools, and a loop, and the orchestration frameworks (LangGraph, AutoGen, CrewAI and the rest) supply infrastructure, never the economic model — the substantive choice is the interaction structure between agents. Second to survey augmentation, motivated by a genuine and worsening data problem: falling response rates, patterned non-response, professionalized online panels, and human respondents who are themselves quietly using LLMs. The WTA/PSID replication study varies nearly every design lever and reports which ones actually matter. Grounding data matters most, fine-tuning and RAG help substantially, prompt engineering and temperature matter less, and the accuracy pattern is heterogeneous in ways that cut against intuition — good for some hard-to-reach groups, worse for the young and affluent. The closing best-practice list is a compact protocol: ground, stabilize, validate against a human test–retest ceiling, map heterogeneity, correct bias before scaling.

## Relevance to Economics Research

The bank-run withdrawal table is the single most useful artifact here for any economist contemplating synthetic subjects: it is direct, quantified evidence that **cross-model dispersion swamps most treatment effects**, which means results from one unvalidated model are uninterpretable. The accompanying bias framework is the constructive response — define bias at the cell level, project it on observables, and report the R², because *predictable* bias is correctable while unstructured bias is not. That is a reporting standard economists can adopt immediately, and it generalizes far beyond bank runs.

For applied work, three things transfer. The **power calculation for simulation runs** puts LLM experiments on the same footing as lab experiments and stops the arbitrary "I ran it 100 times." The **persona-bundle warning** is a clean identification point: varying "wealthy" in a prompt is not a clean treatment on wealth, and designs that ignore this confound the trait vector. And the **human test–retest ceiling** as a benchmark solves the recurring question of what accuracy is good enough — 0.413 for real human predictors on WTA reframes an LLM's 0.65 as strong rather than weak. The survey-augmentation results also carry a policy-relevant sting: since real respondents are already using LLMs, the choice is no longer between human and synthetic data but between *acknowledged* and *unacknowledged* synthetic content. Finally, the crisis-communication findings — authoritative messages reduce withdrawal intent, network effects dominate, and effects vary by demographic group — are a genuine substantive contribution to central bank communication research, and the design is a template for testing interventions that could never be fielded on real depositors.

## Related Concepts

- [[concepts/multi-agent-systems]]
- [[concepts/agentic-ai]]
- [[concepts/empirical-methods]]
- [[concepts/langgraph]]
- [[concepts/retrieval-augmented-generation]]
- [[concepts/sycophancy-and-bias]]
- [[concepts/research-quality]]

## Related Summaries

- [[summaries/kazinnik-cemfi-day1]]
- [[summaries/kazinnik-cemfi-day2]]
- [[summaries/kazinnik-cemfi-day3]]
- [[summaries/kazinnik-cemfi-day5]]
- [[summaries/ai-agents-generative-ai]]
- [[summaries/architecture-patterns]]
- [[summaries/aiesi-post-training]]
