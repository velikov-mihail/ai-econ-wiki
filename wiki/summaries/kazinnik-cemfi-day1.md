---
title: "Economics with LLMs — Day 1: Foundations, Applications, and Agentic Tools"
tags: [summary, finance-econometrics, text-as-data, llm-foundations, agentic-workflows, teaching]
sources:
  - "[[raw/pdfs/kazinnik_cemfi2026_day1.pdf]]"
date_updated: 2026-08-23
date_published: 2026-08-17
---

- **Author/Source**: Sophia Kazinnik (Digital Economy Lab, Stanford University) — *Economics with LLMs: Measuring, Forecasting, and Simulating Economic Behavior*, CEMFI Summer School 2026, Day 1 of 5, August 17, 2026
- **Original**: [https://www.sophiakazinnik.com/cemfi2026/day1.pdf](https://www.sophiakazinnik.com/cemfi2026/day1.pdf)

## Key Ideas

- **The LLM is an instrument, not an oracle.** LLMs turn unstructured data into variables, forecasts, simulations, or decisions — but they are not neutral, because they were trained on the same texts, institutions, and behaviors economists want to study. The operative questions are *when* outputs are useful and *how we can tell when they are wrong*.
- **A lineage of economic instruments**, each with its own failure mode: national accounts (1930s–40s) made "the economy" measurable — *what counts*; the sample survey (1940s–50s) made households observable — *who gets asked*; microdata plus computing (1980s–2000s) let economists test many more relationships — *what can we believe*; the language model (2020s) makes **the latent measurable** — *what happens when the tool itself responds*.
- **Why unstructured data**: high-signal (central bank communication, 10-K/10-Q, analyst reports, earnings calls, news, reviews, satellite imagery), timely (arrives before structured data — useful for nowcasting and risk monitoring), and prevalent (80–90% of all data generated worldwide). Kazinnik traces the tradition to Friedman & Schwartz reading qualitative sources by hand for *A Monetary History* (1963).
- **Technical primer**: ML → deep learning → transformers, built up through classifiers, MLPs, backpropagation (Rumelhart, Hinton & Williams 1986), self-supervised next-token prediction, RNN sequential processing versus transformer parallel self-attention, and the 2017–2020 arc from BERT (340M parameters) to GPT-3 (175B).
- **The buzzword pipeline as one object**: Model choice → Architecture → Pre-training → Post-training → Inference → Evaluation. Crucially, **provider choices** (architecture, training data, pre/post-training, safety rules) are distinct from **researcher choices** (model selection, prompt, context, tools, sampling settings, validation) — the latter set *is* the research design.
- **Inference-time design levers**, each with a research-design consequence: system versus user prompt hierarchy; the context window ("like replying to an email after reading only the material currently in front of you"); temperature and top-p (*"sampling settings affect reproducibility"* — use low randomness for classification and reproducible measurement); tool use; and RAG (retrieve 2007 FOMC transcripts rather than asking the model what the FOMC thought about inflation in 2007).
- **"Open" is not one thing** for research purposes: open-weight (inspect/run/adapt, but usage may be restricted) versus open-source (freedom to modify and redistribute — better for reproducibility) versus closed frontier (stronger performance, less control). Check weights, license, data access, and whether others can reproduce your setup.
- **The jagged frontier** (Dell'Acqua et al. 2023): don't ask whether "AI works" in general; test which *subtasks* are inside or outside the frontier and add verification for those outside. **The right unit of analysis is often the subtask, not the whole workflow.**
- **Five levels of agentic research**: (1) browser chat with manual copy/paste, (2) agentic editor inside an IDE, (3) terminal agent that reads the project and iterates, (4) agent with tools (databases, APIs, browsers, private files), (5) long-running agent with logs, tests, and review checkpoints — citing Goldsmith-Pinkham and Panjwani.
- **External memory makes agents useful**: project guides for conventions and directory maps, reusable skills for longer workflows (replication checks, PDF splitting, figure audits, slide building), and session logs that keep the research path inspectable. "The best agent setup looks less like a prompt trick and more like a reproducible research system."
- **Agentic risks**: prompt injection, tool overreach (technically valid, substantively wrong actions), data exposure, non-reproducibility (cloud agents and closed models drift over time), and **false delegation** — the agent completes the visible task while missing the research objective.
- **The course's practical rule**: *"Use agents for labor. Use economics for judgment."* Let the model draft, search, code, label, and summarize; the researcher owns the estimand, validation design, and interpretation; **treat all generated data as "measured with error" until proven otherwise.**
- **There is no single "LLM accuracy."** The validation test depends on the use: measurement → agreement with a credible human or external benchmark; prediction → held-out outcomes; simulation → reproduces behavior observed in real people; action → the workflow completes correctly and safely. In every case: test on data not used to design the prompt, compare against a meaningful baseline, check sensitivity to reasonable design choices.
- **An LLM call is part of the research design.** Minimum reproducibility record: model and provider, date/model version, system prompt, user prompt, context or documents supplied, sampling settings, tools available, number of runs/retries, and how the output became your final variable.

## Summary

Day 1 opens a five-day CEMFI course whose arc runs foundations → measurement → forecasting → simulation → LLMs as economic subjects. Kazinnik frames the whole week around a single stance: the LLM is the newest in a lineage of economic instruments, and like national accounts and the sample survey before it, it brings both a new class of measurable objects and a new way to get things wrong. What is new this time is that *the tool itself responds* — the instrument is trained on the same corpora, institutions, and behaviors under study, so the usual arms-length separation between instrument and object breaks down.

The first block is an unusually clean technical primer for economists — classifiers, MLPs, backpropagation, self-supervised next-token prediction, RNNs versus transformers, tokenization, embeddings — but every concept is landed on a research-design implication rather than left as background. Tokenization matters because cost and context windows are measured in tokens. Sampling settings matter because they determine reproducibility. Post-training matters because it is a provider choice the researcher inherits rather than controls. The organizing distinction is provider choices versus researcher choices, and Kazinnik's point is that the researcher's set — model, prompt, context, tools, sampling, validation — constitutes the research design and must be documented as such.

The second block turns to agentic tools. Kazinnik lays out a five-level ladder from browser chat to long-running agent, argues that external memory (project guides, reusable skills, session logs) is what converts an agent from a prompt trick into a reproducible research system, and sketches a five-step research agent workflow: orient, assemble, implement, stress-test, package. She is equally explicit about risk, naming prompt injection, tool overreach, data exposure, non-reproducibility from drifting cloud models, and false delegation. The day closes on validation. There is no scalar "LLM accuracy" — the right test depends on whether the output is a measure, a prediction, a simulation, or an action — and on a reproducibility checklist detailed enough that another researcher could reconstruct the call. Students are asked to pick a "moonshot" research question on day one and build it across the week.

## Relevance to Economics Research

This is a rare deck that treats LLM mechanics and econometric practice as a single subject rather than two adjacent ones. Three things make it directly usable. First, the **provider-versus-researcher choice split** gives a clean answer to "what part of this is my research design?" — and the accompanying reproducibility checklist (model version, system prompt, sampling settings, tool access, number of runs, output-to-variable mapping) is immediately adoptable as a data appendix standard for any paper using an LLM. Second, the **four-way validation taxonomy** — measurement, prediction, simulation, action — prevents the common error of importing a benchmark from one use case into another, and it sets up the rest of the course, where each remaining day takes one branch. Third, the **"use agents for labor, use economics for judgment"** rule, together with "treat all generated data as measured with error until proven otherwise," is the cleanest available statement of how to keep an identification strategy intact while delegating execution. The jagged-frontier framing (evaluate subtasks, not workflows) and the false-delegation risk are the two ideas most likely to change how a reader actually supervises an agent.

## Related Concepts

- [[concepts/text-as-data]]
- [[concepts/llm-reasoning]]
- [[concepts/jagged-frontier]]
- [[concepts/retrieval-augmented-generation]]
- [[concepts/reproducibility-transparency]]
- [[concepts/agentic-workflows]]
- [[concepts/human-in-the-loop]]
- [[concepts/open-source-models]]

## Related Summaries

- [[summaries/kazinnik-cemfi-day2]]
- [[summaries/kazinnik-cemfi-day3]]
- [[summaries/kazinnik-cemfi-day4]]
- [[summaries/kazinnik-cemfi-day5]]
- [[summaries/aiesi-post-training]]
- [[summaries/korinek-2023]]
- [[summaries/getting-started-economists]]
- [[summaries/shape-of-ai]]
