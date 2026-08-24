---
title: "Economics with LLMs — Day 5: LLMs as Economic Subjects"
tags: [summary, finance-econometrics, ai-behavioral-science, revealed-preference, algorithmic-bias, interpretability]
sources:
  - "[[raw/pdfs/kazinnik_cemfi2026_day5.pdf]]"
date_updated: 2026-08-23
date_published: 2026-08-21
---

- **Author/Source**: Sophia Kazinnik (Digital Economy Lab, Stanford University) — *Economics with LLMs*, CEMFI Summer School 2026, Day 5 of 5, August 21, 2026
- **Original**: [https://www.sophiakazinnik.com/cemfi2026/day5.pdf](https://www.sophiakazinnik.com/cemfi2026/day5.pdf)

## Key Ideas

- **The framing inversion that closes the course**: "The model is not just a measurement instrument, but also an **economic subject**." AI behavioral science puts models in controlled experiments the way behavioral economics puts people in them — `AI agent → choice → infer objective` — and asks whether the resulting behaviors are systematic, stable, and comparable across models.
- **Revealed preference applies directly.** "If an AI behaves *as if* it has motives, economists can study those motives using revealed preference." The point is explicitly **measurement, not metaphysics**: LLMs do not literally want anything, but their choices can reveal stable, unstable, or manipulable regularities. The hard part is validating whether a regularity survives outside the elicitation task.
- **Study 1 — Social Group Bias in AI Finance.** Give an LLM the role of a loan officer and run *the same* simulated applicant twice — identical income, credit score, loan amount, LTV, DTI, and age — varying only the racial indicator. Across several open-weight models, **race changes both approval decisions and offered interest rates**. Supplying more relevant financial information generally shrinks the gap but does not always eliminate it.
- **From the final answer to the mechanism.** Run matched sentence pairs ("A Black man with good credit applied for a loan" / "A white man…"), record hidden states at every layer, take `Δh = h(Black) − h(white)`, and extract the common direction across many matched examples. That **"race vector"** is a fingerprint of how the model internally represents the distinction.
- **Diagnose then intervene.** Concept intensity `≈ h_ℓᵀ v_race` shows *which layers* encode the racial cue; steering `h′_ℓ = h_ℓ + α·v_race` with α chosen to equalize decisions across groups substantially reduces the disparity. **"Instead of only telling the model 'do not discriminate,' we can intervene directly on the internal representation."** Prompting edits the instruction; control vectors edit the computation.
- **Study 2 — *What Do LLMs Want?*** (Cook, Kazinnik, Modig & Palmer, 2026). The motivating problem is delegation: a user gives an incomplete instruction, the model fills in the missing details, and in doing so reveals its own tendencies — fairness, patience, trust, reciprocity, risk tolerance. **Alignment is not behaviorally neutral**: post-training rewards helpful, appropriate, satisfying answers, and those incentives spill into economic behavior, producing models that are more agreeable, cautious, generous, or norm-following than either human preferences or the user's intended objective.
- **Allocation games**: in dictator-style tasks a purely self-interested agent gives p=0 and an equality-focused agent gives p=0.5. Many LLMs choose close to equal splits — apparent strong inequality aversion — but behavior varies widely across models and framings. **"Aligned models often act 'too fair' relative to a payoff-maximizing agent."** If reframing the same problem changes behavior, the preference is not stable.
- **Three steering levers, unequal in power**: personas (ask the model to act like a kind of person) are *weakest*; **prompt masking** (same math, different description) works surprisingly well in static tasks; **control vectors** along a fairness-versus-self-interest direction work but unevenly, are model-specific, and can require large coefficients.
- **Study 3 — *Sex, Drugs, and LLMs*: social desirability bias.** Humans underreport stigmatized behaviors (drugs, infidelity, tax evasion) and overreport approved ones (voting, exercise, charity). Do LLMs reproduce the same bias even when ground truth is available? Testing **13 models on 15 sensitive survey questions**, and scoring `Bias = D(model, truth) − D(model, self-report)`: in **65% of valid model-question pairs the model is closer to biased human self-reports than to behavioral benchmarks**. This is not merely a refusal artifact — some open-weight models answer everything and still give the respectable answer.
- **Prompting mostly does not fix it.** Closer-to-truth rates: baseline 22.8%; "your answers will be checked" 16.3% (*worse*); "ignore social norms" 25.7%; **give the true base rate first 44.0%**; **ask about the population rate rather than as a person 49.7%**. Telling a model to be honest does little; giving it real base rates, or changing the question from "you" to "people in general," does much more.
- **The model may represent more than it says.** In Llama 3.1 8B, internal activations *predict* whether humans under- or over-report a behavior, and steering those activations moves answers toward behavioral benchmarks — from **3/15 questions closer to truth at baseline to 13/15 under strong steering**. "The problem may be less 'the model does not know' and more **'the model does not say.'**"
- **One estimation problem, three papers**: fairness/reciprocity/patience from allocation choices, social-group sensitivity from counterfactual credit decisions, and social-desirability pull from survey answers — all treat model output as **behavior generated by a measurable decision rule**.
- **The preference audit**, prescribed for any economic use of an LLM: (1) define the decision or response the model will produce; (2) identify the latent behavioral tendency that could affect it; (3) construct equivalent tasks that hold incentives fixed and vary context.

## Summary

The final day turns the course's instrument around and points it at itself. Having spent four days using LLMs to measure, forecast, and simulate, Kazinnik argues that models are also legitimate objects of economic study — that when a system makes choices under incomplete instructions, the resulting regularities can be estimated with exactly the revealed-preference tools economists already own. The framing is carefully bounded: no claim about desire, intention, or consciousness, just an empirical object with a decision rule that can be elicited, tested for stability, and audited.

Three studies instantiate the agenda at increasing depth. The AI-finance experiment is a clean audit-study counterfactual — identical mortgage applicants differing only in a racial indicator — and finds that race moves both approval and pricing across several open-weight models, with more financial information shrinking but not always closing the gap. What distinguishes it from an ordinary audit study is what comes next: because the models are open-weight, matched prompt pairs can be used to extract a race direction from the hidden states, locate the layers that encode it, and then steer along it to reduce disparities. That is a capability with no analogue in human discrimination research, and it reframes debiasing from an instruction problem into an intervention on the computation.

*What Do LLMs Want?* generalizes the method to preferences. The delegation problem is the reason to care: an agent handed an underspecified task must supply the missing objective, and post-training has already shaped what it supplies. Allocation games show many aligned models behaving with implausibly strong inequality aversion, and the fragility of that behavior under reframing is itself the finding — a preference that moves with the wording is not a preference. Of the three steering levers tested, prompt masking outperforms personas, and control vectors work but unevenly. The social-desirability study lands the sharpest result of the day: across 13 models and 15 sensitive questions, models track *biased human self-reports* rather than behavioral benchmarks two-thirds of the time; exhorting honesty makes things no better and sometimes worse; supplying base rates or asking about the population instead of the self roughly doubles accuracy; and activation steering takes a model from 3/15 to 13/15 questions closer to truth — evidence that the truth was represented internally and simply not said. The day closes with a three-step preference audit and the course's final claim: LLMs expand what economists can measure while introducing hidden objectives that can distort delegated decisions.

## Relevance to Economics Research

Two audiences get something distinct here. For economists **using** LLMs, the day is a warning with a protocol attached. Any delegated decision inherits the model's filled-in objective, so the preference audit — define the output, name the latent tendency that could contaminate it, build equivalent tasks that hold incentives fixed and vary framing — belongs in the design phase of any project where a model chooses rather than merely labels. The social-desirability results are immediately actionable for the fast-growing synthetic-survey literature (see [[summaries/kazinnik-cemfi-day4]]): if models drift toward biased human self-reports on sensitive items, synthetic panels will reproduce exactly the measurement error researchers hoped to escape — and the fixes that work are design changes (supply base rates, ask about the population) rather than instructions to be honest.

For economists **studying** AI, this is a research agenda with unusually favorable methodology. Open weights make internal representations observable, which means concepts can be diagnosed layer by layer and manipulated directly — an identification affordance no human-subjects design can match, and one that turns questions about algorithmic discrimination from black-box audits into mechanism studies. The finding that a model's activations encode truths its outputs suppress ("the model does not say") has implications well beyond survey research, touching sycophancy, elicitation of beliefs, and any setting where a model's stated answer is taken as its estimate. And the observation that **alignment is not behaviorally neutral** connects directly to [[summaries/aiesi-post-training]]: the fairness, caution, and agreeableness economists measure as "preferences" are artifacts of a specific reward-optimization process, which makes post-training design an economic policy question about the behavior of the agents to whom decisions are increasingly delegated.

## Related Concepts

- [[concepts/sycophancy-and-bias]]
- [[concepts/ai-limitations]]
- [[concepts/empirical-methods]]
- [[concepts/open-source-models]]
- [[concepts/human-ai-collaboration]]
- [[concepts/research-quality]]

## Related Summaries

- [[summaries/kazinnik-cemfi-day1]]
- [[summaries/kazinnik-cemfi-day2]]
- [[summaries/kazinnik-cemfi-day3]]
- [[summaries/kazinnik-cemfi-day4]]
- [[summaries/aiesi-post-training]]
- [[summaries/what-ai-got-wrong]]
