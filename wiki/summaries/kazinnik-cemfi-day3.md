---
title: "Economics with LLMs — Day 3: Forecasting, Prediction, and Survey Augmentation"
tags: [summary, finance-econometrics, forecasting, training-data-leakage, synthetic-agents, empirical-methods]
sources:
  - "[[raw/pdfs/kazinnik_cemfi2026_day3.pdf]]"
date_updated: 2026-08-23
date_published: 2026-08-19
---

- **Author/Source**: Sophia Kazinnik (Digital Economy Lab, Stanford University) — *Economics with LLMs*, CEMFI Summer School 2026, Day 3 of 5, August 19, 2026
- **Original**: [https://www.sophiakazinnik.com/cemfi2026/day3.pdf](https://www.sophiakazinnik.com/cemfi2026/day3.pdf)

## Key Ideas

- **A forecaster is an information set plus a loss function.** LLMs complicate both: the training corpus is huge and partly hidden, so historical forecasting can quietly become *memory rather than prediction*; and a single number gives a point forecast with no uncertainty attached.
- **The reframe**: don't ask "what will inflation be next year?" Ask for a *distribution*, record the information set available at forecast time, and compare against experts, benchmarks, or simple statistical models.
- **Formal framework**: with `y_{t+H} = f(x_t, z_t) + ε_{t+H}`, humans access both observables `x_t` and unobservables `z_t` (private insight, tacit knowledge, intuition) but add bias `Δ_{i,t}` with possibly non-zero mean; traditional algorithms process `x_t` efficiently but cannot see `z_t`; LLMs are algorithm-like in access but form expectations from a massive text-based distribution. The gap between human and AI forecasts turns on the **relative size of the two biases**.
- **Two prompt ingredients close that gap**: (1) **forecaster characteristics** to capture systematic bias patterns, and (2) **past median SPF forecasts** as a proxy for the unobservable `z_t` — human forecasts are used as a channel through which latent information reaches the model.
- **The paper** — *Simulating the Survey of Professional Forecasters* (with Anne L. Hansen, John J. Horton, Daniela Puzzello, Ali Zarifhonarvar). Synthetic forecasters are built at the individual level from public data (LinkedIn, personal sites): education, job title, affiliation, company location, experience, sector/geographic bias, social media presence. The prompt is reproduced in full in the deck. Sample: SPF point forecasts, 1999–2023, five horizons (nowcast through t+4), plus a 2024 out-of-sample validation.
- **Three results**: (1) **AI ≈ humans** — qualitatively similar forecast paths with quantitative differences; (2) **AI ≻ humans** — LLM forecasts often achieve lower MAE, especially at *longer horizons* and most pronounced for real GDP and unemployment; (3) **AI ≻ humans | human input** — the accuracy advantage *depends on the human signal in the prompt*. Strip out personas and past SPF medians and performance degrades.
- **The mechanism**: "LLMs extract latent (`z_t`) information from human forecasts while also processing `x_t` more effectively." The upshot is a hybrid — AI plus human signals beating either pure-human or purely data-driven ML — and the prospect of a **"virtual forecasting lab"** for cheap, fast, adaptable survey augmentation.
- **The forecasting failure mode is lookahead, not noise.** In measurement the central risk is noisy or biased labels; in forecasting it is that the model has seen future text, revised data, solved benchmarks, or leaked labels. **"A model that looks good in backtests may be grading its memory."** Mitigations used: strict as-of-date instructions, real-time vintage data, 2024 out-of-sample tests, and a **recall test** — asking the model to reproduce past realized values, where errors run **16× larger** than the baseline nowcasting errors.
- **The econometric contract.** An LLM is "a very talented but mysterious intern": powerful *and* brittle. Two distinct research tasks with different validity conditions —
  - **Prediction** (text → outcome, minimize out-of-sample error). Key condition: **no training leakage**. Best practice: open-source models with known cutoffs, and test data that did not circulate publicly before that date. Prompting cannot un-train a model. Documented econ leakage: models complete congressional bill descriptions verbatim and predict passage with implausibly high accuracy; models reproduce exact finance headlines.
  - **Estimation** (text → latent construct → downstream regression). Key condition: LLM measurement error must not be systematically related to the regression variables.
- **"Accuracy alone does not guarantee valid downstream inference."** Even seemingly non-systematic error can bias estimates depending on how the measured concept enters the model. Worked example: if the LLM systematically understates hawkishness *when inflation is high*, a regression on `V̂` will understate how strongly hawkishness responds to inflation.
- **Debiasing recipe**: run the LLM on the large sample for cheap scale, hand-code a small representative validation sample, estimate the LLM's systematic error there, and add the correction back. Kazinnik's analogy — a blurry scanner over thousands of pages: if the blur is consistent, inspecting a few pages by hand corrects the whole scan. Gold-standard-only is unbiased but high-variance; naive plug-in is low-variance but possibly biased; **debiased dominates when LLM labels are informative, the primary sample is large, the validation sample is representative, and errors are structured enough to estimate.**
- **With no validation data there are only three weak options** — assume zero error (not credible), model the error structurally (heroic), or redefine the target as "the LLM's label" (changes the question). *Collect some validation labels.*
- **Chronologically consistent LLMs** (He, Lv, Manela & Wu 2025): ChronoBERT/ChronoGPT are vintage models whose training data stop at a known historical cutoff, so embeddings cannot encode the future even when the prompt is clean. Applied to next-day return prediction from financial news, the chronologically consistent models perform about as well as the much larger Llama 3.1 — **lookahead bias is modest in that application, but its magnitude is model- and application-specific.** The real contribution is a way to *measure* leakage rather than assume it away.
- **Forecasting is more than the mean**: point forecasts test consensus-matching; scenario forecasts test conditioning on counterfactual paths; structural scenarios test whether the model knows *why*; density forecasts test calibration. A model can be accurate and badly calibrated — 85% correct while routinely claiming 99% confidence.
- **Replication package for LLM-based estimation**: benchmark gold labels, prompts plus an open-source model snapshot with fixed weights, and the debiasing/estimation code. Closed models risk non-replicable outputs.

## Summary

Day 3 moves from measuring the present to predicting the future, and immediately identifies why that shift is dangerous. Forecasting requires knowing what the forecaster knew; an LLM's information set is a partly undisclosed training corpus, so any historical backtest risks scoring recall rather than inference. Kazinnik builds a compact framework separating observables from unobservables, and locates humans, classical algorithms, and LLMs by what they can access and what bias they add. The insight that organizes the day's headline paper is that human forecasts themselves carry latent information — so feeding an LLM past SPF medians and individual forecaster personas is a way of routing `z_t` into a model that otherwise cannot see it.

The SPF simulation delivers three findings in ascending order of interest. Synthetic forecasters track human ones qualitatively; they often beat them on MAE, especially at longer horizons and for real GDP and unemployment; and — critically — that edge is conditional on the human input in the prompt. Remove the personas and prior medians and the advantage shrinks. This is not "AI replaces forecasters" but a hybrid result: the model processes structured data more consistently than humans while borrowing humans' tacit knowledge secondhand. The obvious objection, temporal leakage, gets four separate mitigations, including a recall test showing the model reproduces past realized values 16× worse than it nowcasts them.

The second half generalizes into what Kazinnik calls an econometric contract, and it is the most portable material in the course. Prediction and estimation are different tasks with different failure conditions: prediction dies from training leakage, estimation dies from systematically correlated measurement error. Neither is diagnosed by accuracy. The prescribed remedy for estimation is a plug-in-plus-validation design — cheap LLM labels at scale, a small gold-standard sample to estimate the bias, and an explicit correction — with clear conditions under which it beats both alternatives, and a blunt instruction to collect validation labels if you have none. The day closes on chronologically consistent models as a tool for *measuring* leakage, and on the reminder that a point forecast is only the first of four things one might want: scenarios, structural scenarios, and calibrated densities are separate, harder asks.

## Relevance to Economics Research

This is the day that most directly protects a referee-proof empirical paper. The **prediction-versus-estimation contract** is a checklist any economist using LLM-generated variables should adopt before writing a line of code: state which task you are doing, enforce no-leakage for prediction, collect validation labels and report bias-corrected results for estimation, document prompts and model versions, and don't use closed models for key inferences. The **debiased estimator** — LLM labels on the full sample plus a small human-coded validation sample used to correct systematic error — is the practical answer to the plug-in temptation, and it is exactly the design a modern referee will ask for.

The leakage material is equally actionable. The documented econ-specific cases (verbatim completion of congressional bill descriptions, exact reproduction of finance headlines) are concrete enough to cite, the **recall test** is a cheap diagnostic anyone can run, and chronologically consistent models turn leakage from an unfalsifiable worry into something with a measurable magnitude. The SPF paper itself opens a research program: if synthetic panels can be built from public biographical data and validated against a real survey, the same machinery extends to consumer expectations, firm surveys, and analyst forecasts — with the important caveat that the AI edge came *from* human input, which bounds how far survey substitution can go. The four-way distinction between point, scenario, structural-scenario, and density forecasting, plus the accuracy-versus-calibration warning, gives a ready evaluation vocabulary for the growing LLM-forecasting literature.

## Related Concepts

- [[concepts/empirical-methods]]
- [[concepts/text-as-data]]
- [[concepts/reproducibility-transparency]]
- [[concepts/research-quality]]
- [[concepts/ai-limitations]]
- [[concepts/open-source-models]]

## Related Summaries

- [[summaries/kazinnik-cemfi-day1]]
- [[summaries/kazinnik-cemfi-day2]]
- [[summaries/kazinnik-cemfi-day4]]
- [[summaries/kazinnik-cemfi-day5]]
- [[summaries/ai-powered-scholarship]]
- [[summaries/applications-generative-ai]]
- [[summaries/aiesi-post-training]]
