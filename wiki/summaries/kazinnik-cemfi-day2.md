---
title: "Economics with LLMs — Day 2: Natural Language Understanding and Measurement"
tags: [summary, finance-econometrics, text-as-data, measurement-validation, central-bank-communication, open-source-models]
sources:
  - "[[raw/pdfs/kazinnik_cemfi2026_day2.pdf]]"
date_updated: 2026-08-23
date_published: 2026-08-18
---

- **Author/Source**: Sophia Kazinnik (Digital Economy Lab, Stanford University) — *Economics with LLMs*, CEMFI Summer School 2026, Day 2 of 5, August 18, 2026
- **Original**: [https://www.sophiakazinnik.com/cemfi2026/day2.pdf](https://www.sophiakazinnik.com/cemfi2026/day2.pdf)

## Key Ideas

- **The goal is a valid, interpretable regressor.** Not a clever label — a variable that supports meaningful causal or structural inference. The chain is `Observables → Measurement → Latent construct`: we observe words, choices, and prices; we want beliefs, expectations, sentiment, and narratives.
- **"A prompt is a measurement instrument."** For measurement, the prompt does three things: supply the text, define the construct, and specify the allowed output. But the prompt is only part of the method — **the model, sampling settings, context, and output rule are part of the method too**.
- **Case 1 — *Can ChatGPT Decipher Fedspeak?*** (with Anne Hansen). Benchmark: 500 FOMC statement sentences (2010–2020), each independently labeled by 3 RAs on a five-point dovish(−1) → hawkish(+1) scale; "truth" = human consensus. Average disagreement is **U-shaped** — reviewers agree most on "neutral" sentences and disagree most on the extremes.
- **GPT beats every traditional NLP baseline.** Zero-shot GPT-4 achieves MAE 0.31 / accuracy 0.52 versus BERT 0.66 / 0.25, Loughran–McDonald 0.62 / 0.28, Henry 0.55 / 0.35, and NRC 0.81 / 0.11. Fine-tuning on just 400 sentences pushes MAE to 0.23 and accuracy to 0.61 — with the explicit caveat that **the sample is too small**.
- **Metric discipline for multi-class problems**: report MAE/RMSE, macro/weighted F1, and *balanced* accuracy rather than raw accuracy, which is misleading under the class imbalance typical of policy-stance data (191 neutral versus 14 hawkish sentences in the benchmark).
- **Reasoning as a distinguishing capability**: GPT models don't just classify, they justify. Kazinnik benchmarks their explanations against "Bryson," a 24-year-old Fed RA, and finds GPT-4's reasoning closely tracks his — an affordance dictionaries and BERT simply do not have.
- **Scaling qualitative output via DAGs**: LLM reasoning is often causally structured, so extract causal claims into directed acyclic graphs (nodes = economic signals, edges = *supports* / *tempers*), connecting to Andre, Haaland, Roth, Wiederholt & Wohlfart's "Narratives about the Macroeconomy." The deck includes runnable JSON-mode extraction code.
- **"Digital Romers"**: GPT-4 is prompted with Romer & Romer's own instructions and run over FOMC transcripts (1946–2017) and minutes (2017–2023) to identify monetary policy shocks. It recovers most R&R shocks; where it misses, the stated reason is usually **missing evidence that the economy was at full potential** — a legible, auditable failure mode. Romer & Romer (2023) had written that they "thoroughly expect to be made largely redundant by computers eventually, but perhaps not for a few years to come."
- **Case 2 — *Evaluating Local Language Models*** (with Tom Cook, Anne Hansen, Peter McAdam). Motivation is institutional: reproducibility, **data privacy**, cost, and customization matter to central banks, financial firms, and anyone handling PII. Models tested: Vicuna 7B/13B, Wizard-Vicuna-Uncensored 30B, Guanaco 33B/65B, Fin-LLaMA 33B, mostly under 4-bit GPTQ quantization (8× compression, consumer GPUs).
- **Local open models are viable.** On the Financial PhraseBank (75%-agreement subset), all local LLMs clear **75% accuracy** on sentiment, with Vicuna-13B leading. Two novel annotation dimensions are added on 1,000 sentences: **vagueness** (clear versus deliberately convoluted) and **temporality** (past/present/future). Scale helps temporality more than vagueness or sentiment; vagueness suffers from severe label imbalance.
- **Prompting technique interacts with task**: few-shot beats chain-of-thought for financial sentiment, while CoT beats few-shot for hawkish/dovish policy tone. There is no universally best prompting strategy.
- **Topic pipeline for long transcripts**: bank earnings calls (2021–2023Q2, 100+ banks/quarter, ~12,000 words each) are split to utterance level; the LLM emits up to 5 free-text topic labels per passage; labels are embedded (`all-mpnet-base-v2`) and K-means clustered (K≈150) to collapse "Real Estate Market"/"Housing Sector"/"Residential Properties" into one topic. LLM → embedding → clustering scales where fixed taxonomies do not.
- **Substantive finding**: topic similarity across banks **peaks in 2023Q1** (SVB stress) — banks converge on reassuring about common risks; the deposits topic jumps **200%+** in relative frequency; sentiment falls sharply while **clarity stays flat** (banks did not become vaguer under stress). The pattern is read as pooling-on-reassurance in a signaling model: promote in calm periods, reassure in crises.
- **Explainability toolkit**: LIME (perturb inputs, fit a local interpretable model), SHAP (Shapley-value feature contributions, applicable at token level), and partial dependence plots — which Kazinnik pitches directly as *ceteris paribus* for black-box models.
- **The standing caveat**: "Any downstream use of LLM-derived labels requires validation against gold-standard data."

## Summary

Day 2 is the measurement day, and its organizing claim is econometric rather than technical: an LLM label is only useful if it is a valid, interpretable regressor. Kazinnik starts from the classic latent-construct problem — we observe words, choices, and prices but want beliefs, expectations, sentiment, and narratives — and insists that the full measurement procedure (construct definition, prompt, model, sampling settings, context, output rule) be treated as the instrument, documented and validated as one.

The first case study, *Can ChatGPT Decipher Fedspeak?*, supplies the template. A hand-labeled benchmark of 500 FOMC sentences establishes a human consensus "truth," complete with a disagreement structure that is itself informative — reviewers agree on neutral sentences and split on the extremes, which bounds how well any classifier could do. Against that benchmark, zero-shot GPT-4 substantially outperforms BERT and the standard finance dictionaries on every metric, and light fine-tuning improves it further. Two extensions push beyond classification: an explanation audit against a real Fed RA, and a "digital Romers" exercise in which GPT-4 is handed Romer & Romer's own shock-identification instructions and run over eight decades of FOMC transcripts. It finds most of the canonical shocks, and its misses come with articulable reasons. Kazinnik also shows how to make LLM reasoning tractable at scale by extracting it into causal DAGs.

The second case study shifts the question from capability to deployability. For central banks and financial firms handling confidential data, closed APIs are often unusable, so *Evaluating Local Language Models* benchmarks quantized open models on FOMC stance and the Financial PhraseBank. The answer is broadly encouraging — local models clear 75% accuracy on sentiment with prompt refinement — with two useful wrinkles: the best prompting technique depends on the task, and hard constructs like vagueness are limited by annotation quality rather than model size. The application scales to bank earnings calls through an LLM-plus-embeddings-plus-clustering topic pipeline, producing a clean narrative of the 2023 banking stress: topic convergence, a 200%+ spike in deposit talk, falling sentiment, a shift from forward-looking to present-focused language, and clarity that never degrades. The day closes on model-agnostic explainability (LIME, SHAP, PDPs) and a runnable Together.ai exercise labeling PhraseBank sentiment across three open models.

## Relevance to Economics Research

This is the most directly transferable day of the course for empirical economists. It supplies a complete, publishable measurement protocol: define the construct, build a multi-annotator human benchmark, report the *disagreement structure* as a ceiling on achievable performance, evaluate with balanced accuracy and macro-F1 rather than raw accuracy, and benchmark against both traditional NLP (dictionaries, BERT) and a fine-tuned variant. The Fedspeak paper is a template any researcher can port to earnings calls, analyst reports, regulatory filings, or parliamentary debate.

Three ideas have wider reach. The **"digital Romers"** exercise shows how to audit an LLM against a canonical hand-coded series, and its failure analysis — GPT-4 explains *why* it declined to call a shock — is a model for making LLM measurement error interpretable rather than merely quantified. The **local-model results** matter for anyone at a central bank, regulator, or firm where sending confidential text to a closed API is prohibited: the paper is evidence that the privacy-preserving option is no longer a large accuracy sacrifice, which changes what is feasible with supervisory and PII-laden data. And the **LLM → embedding → clustering topic pipeline** is a practical answer to the free-text-label proliferation problem that defeats naive LLM topic modeling, with the 2023Q1 banking-stress results demonstrating that the resulting series carry real economic signal. Finally, PDPs-as-*ceteris paribus* is a useful bridge for economists who want interpretability from black-box classifiers without abandoning them.

## Related Concepts

- [[concepts/text-as-data]]
- [[concepts/empirical-methods]]
- [[concepts/open-source-models]]
- [[concepts/data-privacy]]
- [[concepts/reproducibility-transparency]]
- [[concepts/prompt-engineering]]
- [[concepts/research-quality]]

## Related Summaries

- [[summaries/kazinnik-cemfi-day1]]
- [[summaries/kazinnik-cemfi-day3]]
- [[summaries/kazinnik-cemfi-day4]]
- [[summaries/kazinnik-cemfi-day5]]
- [[summaries/cc-series-14-pnas-replication-1]]
- [[summaries/cc-series-15-pnas-replication-2]]
- [[summaries/applications-generative-ai]]
- [[summaries/aiesi-post-training]]
