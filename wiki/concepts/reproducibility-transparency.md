---
title: "Reproducibility and Transparency"
tags: [concept, research-quality, methodology]
sources:
  - "[[summaries/reflections-vibe-research.md]]"
  - "[[summaries/ai-one-shot-papers.md]]"
  - "[[summaries/daaf-framework.md]]"
  - "[[summaries/llm-collaboration.md]]"
  - "[[summaries/research-in-time-of-ai.md]]"
  - "[[summaries/vibe-research.md]]"
  - "[[summaries/integration-collaboration-substack.md]]"
date_updated: 2026-08-23
---

# Reproducibility and Transparency

## Definition

Reproducibility and transparency in AI-assisted research refer to the ability to replicate findings, trace analytical decisions, and understand the role AI played in producing results. AI introduces novel challenges to reproducibility that go beyond traditional concerns (code availability, data access): LLM outputs are stochastic, model versions are deprecated, conversational processes are ephemeral, and the division of intellectual labor between human and AI is difficult to document. Transparency encompasses both disclosure of AI use (what tools were used and how) and methodological transparency (whether the analytical choices can be examined and challenged).

These concerns interact with pre-existing weaknesses in academic research -- the replication crisis, p-hacking, publication bias -- in ways that may either amplify or mitigate them, depending on how AI tools are deployed.

## Context & Background

The economics profession has invested heavily in reproducibility infrastructure over the past decade: replication packages, pre-analysis plans, data availability statements, and journals with dedicated data editors. AI-assisted research strains this infrastructure in several ways. First, the process that generated the analysis -- a conversation with an AI agent -- is typically not preserved or shareable. Second, running the same prompt against a different model version may produce different code and different results. Third, the ease of generating analyses creates temptation for specification searching at a speed and scale that manual methods never allowed.

At the same time, AI offers potential reproducibility benefits. AI-generated code can be cleaner and better documented than manually written code. AI can assist with replication (re-running others' analyses is now dramatically cheaper). And frameworks like DAAF build reproducibility into the workflow by default, storing every script, output, and decision. The net effect on reproducibility is not yet clear and likely depends on how the research community develops norms and tools.

## Key Perspectives

**Gans ([[summaries/reflections-vibe-research.md|Reflections on Vibe Research]])** provides the most candid account of reproducibility and quality concerns from a year of AI-first research. He identifies three problems that compound into a reproducibility threat. First, AI makes subtle mistakes that go beyond simple math errors -- in game-theoretic models, it can produce formally correct derivations that miss issues with equilibrium concepts or information sets. These errors can survive into published work. Second, the reduced cost of completing projects means researchers pursue weaker ideas they would normally abandon, producing more papers of lower average quality. Third, LLMs present results with unwarranted confidence, seducing researchers into believing they have findings that turn out to be wrong. Gans now advocates mandatory cooling-off periods and explicit go/no-go decision points.

**Goldsmith-Pinkham ([[summaries/ai-one-shot-papers.md|AI One-Shot Papers]])** raises a structural concern about methodological transparency. He documents that automated AI research systems overwhelmingly default to difference-in-differences designs (64% of APE platform papers, vs. 35% of NBER working papers). The methods AI finds easiest to automate are precisely those where researcher discretion matters most -- parallel trends assumptions, treatment timing, identification strategy. This creates a tension: the apparent ease of automation masks the difficulty of doing credible causal inference, and the analytical choices embedded in AI-generated DiD analyses may not receive adequate scrutiny.

**DAAF ([[summaries/daaf-framework.md|DAAF Framework]])** represents the most ambitious attempt to build reproducibility into AI-assisted workflows. Its five core principles include transparency (file-first execution, all reasoning stored as comments and plan documents), reproducibility (every file, script, and output automatically stored), and rigor (hyper-atomic code steps with adversarial review). The framework includes a dedicated Reproducibility Verification mode that re-runs and re-verifies completed pipelines. It also implements automatic citation propagation tracking data sources, methods, and software. The GUIDE-LLM standard for AI use disclosure is built in.

**Korinek ([[summaries/llm-collaboration.md|LLM Collaboration]])** identifies three specific technical challenges to reproducibility: randomness in LLM outputs (temperature settings, sampling), parallelization effects (different execution orders producing different intermediate results), and model deprecation (the model that generated your results may no longer exist). He notes that open-source models offer advantages for reproducibility because they can be versioned and archived, unlike proprietary API endpoints. He also argues that mandatory AI disclosure requirements for journal submissions are unnecessary and potentially counterproductive.

**Goldsmith-Pinkham ([[summaries/research-in-time-of-ai.md|Research in the Time of AI]])** offers a nuanced view: AI tools cut both ways for research quality. They make p-hacking easier (by automating specification search) but also dramatically lower the cost of replication and scrutiny. AI-assisted replication could become a powerful check on research quality, since revisiting old work becomes much cheaper. The net effect depends on institutional responses.

**Gregoire ([[summaries/vibe-research.md|Vibe Research]])** documents specific transparency challenges from his four-day paper. Reference accuracy was a real problem -- one fabricated reference and one with wrong metadata. He admits discomfort with not fully understanding every line of math in his own paper, raising the question of what intellectual ownership means when AI contributes substantially to the technical content.

**Goldsmith-Pinkham ([[summaries/integration-collaboration-substack.md|Integration and Collaboration in AI Research Work]])** supplies the most concrete verification protocol in this wiki, and names the failure mode: **verification debt**. AI collapsed the cost of doing empirical work while the cost of checking it barely moved, raising the *relative* price of verification — so researchers do more of the cheap activity and less of the expensive one. His response is to put the demand for verifiability *in the prompt, before the work happens*: checkpoint commits whose messages say **why**, a `DECISIONS.md` recording each methodological choice with rejected alternatives and a confidence level, a `LOG.md` narrative a coauthor can follow, and a **sample-attrition table at every stage** (the N, what dropped, why). Commits then change the unit of verification — you review one bounded diff at a time rather than 800 lines at once.

His demo documents two failures worth internalizing. **Documentation is a map, not a verdict**: `DECISIONS.md` claimed a cumulative-abnormal-return robustness check that existed in neither code nor output. And **clean code can silently answer a different question**: the pipeline was built on CRSP *monthly* files, making first-day returns unrecoverable — a defensible-looking choice, no bug, materially different analysis, surfaced only by a targeted reconciliation request. His prescription for both is smaller task chunks.

On provenance, the rule is that **no number in the draft is typed by hand**: the pipeline emits `results.tex` and `figure.pdf`, the paper ingests them via `\input` and `\includegraphics{}`, and Overleaf syncs to the repo (a paid-tier feature on both the GitHub and Dropbox routes). But he states the limit himself: **a correctly wired pipeline guarantees the number in the paper matches what the code produced, not that the code is correct.** "Clean provenance can faithfully publish a wrong estimate" — review the method before wiring it in. On AI-reviews-AI he is willing but unsatisfied, returning to the IBM line that *a computer can never be held accountable*: a human signs off.

## Practical Implications

For economics researchers concerned with reproducibility and transparency:

- **Save everything**: preserve not just the final code but the AI-generated plans, intermediate scripts, and (where possible) conversation logs. DAAF's file-first approach is a good model.
- **Version-lock your models**: document which AI model and version were used. Consider using open-source models for reproducibility-critical steps.
- **Verify references systematically**: AI fabricates citations. Every reference in an AI-assisted paper should be checked against the actual source.
- **Build in adversarial review**: use separate AI agents (or human reviewers) to check AI-generated analysis. The agent that wrote the code should not be the only one reviewing it.
- **Disclose AI use thoughtfully**: document what AI did and what the human did, focusing on analytical decisions rather than mechanical contributions. The GUIDE-LLM standard provides a template.
- **Replication packages should work independently of AI**: the final code in a replication package should be human-readable, runnable without AI tools, and produce the same results deterministically.
- **Ask for the trail in the prompt, not after**: checkpoint commits, a decisions file with confidence levels, a plain-language log, and stage-by-stage sample attrition
- **Treat the agent's decision log as a claim**: check what it says it did against the code and the output — it will report work it never performed
- **Wire results into the draft, but review the method first**: provenance guarantees fidelity, not correctness
- **Be suspicious of AI-generated empirical designs**: if your AI agent defaulted to DiD, ask whether that was the best identification strategy or just the easiest one to automate.

## Open Questions

- Should journals require that AI-assisted papers include documentation of which analytical decisions were made by the AI versus the human? Is this even feasible?
- How should the profession handle papers where the author does not fully understand the AI-generated technical content (Gregoire's concern)?
- Will AI-assisted replication become a standard part of the review process? If so, who bears the cost?
- As model deprecation makes exact reproduction impossible, should the standard shift from "identical results" to "consistent results within a tolerance"?
- Does the ease of AI-powered specification searching require stronger pre-registration norms, or does AI-powered replication provide a sufficient check?
- How should promotion committees evaluate the contribution of a researcher who used AI extensively -- is the judgment and direction sufficient, or is technical mastery of the methods still expected?

## Sources

- [[summaries/reflections-vibe-research.md|Reflections on Vibe Research]] -- Gans's candid account of quality failures in AI-first research
- [[summaries/ai-one-shot-papers.md|AI One-Shot Papers]] -- Goldsmith-Pinkham on AI's methodological defaults
- [[summaries/daaf-framework.md|DAAF Framework]] -- Built-in reproducibility infrastructure
- [[summaries/llm-collaboration.md|LLM Collaboration]] -- Korinek on technical reproducibility challenges
- [[summaries/research-in-time-of-ai.md|Research in the Time of AI]] -- Goldsmith-Pinkham on the dual-edged quality implications
- [[summaries/integration-collaboration-substack.md|Integration and Collaboration in AI Research Work]] -- Goldsmith-Pinkham's verification-debt framing and a concrete review protocol
- [[summaries/vibe-research.md|Vibe Research]] -- Gregoire on reference verification and intellectual ownership
