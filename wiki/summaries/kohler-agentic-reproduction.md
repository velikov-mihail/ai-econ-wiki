---
title: "Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results"
tags: [summary, academic-research]
sources:
  - "[[raw/papers/Kohler-Zollikofer-Einsiedler-Hoyle-Ash-Read-Paper-Write-Code-Agentic-Reproduction-Social-Science-Results.pdf]]"
date_updated: 2026-04-25
date_published: 2026-04
---

- **Authors**: Benjamin Kohler, David Zollikofer, Alexander Hoyle, Elliott Ash (ETH Zurich); Johanna Einsiedler (University of Basel). Hoyle and Ash share equal supervision.
- **Original**: working paper, ETH Zurich

- **Key Ideas**
  - **The headline question:** can LLM agents reproduce empirical social-science results given **only the paper's text and the original data** --- *no access to the analysis code*? Prior work (Hu et al. 2025; Shah et al. 2026; Xu & Yang 2026) granted agents access to the original code; this paper masks the code and tests whether the methods description alone is sufficient for re-implementation.
  - **Dataset:** 48 papers from the Institute for Replication (I4Replication), which has human-verified each as fully reproducible. Distribution by journal: AJPS (11), EJ (9), AER (8), AEJ:Pol (5), JOP (5), AEJ:AE (3), APSR (3), RESt (2), AEJ:Macro (1), QJE (1). Original code is 54% Stata, 27% R, 0% Python (papers average 5,324 lines). Agents write Python from scratch.
  - **Pipeline (4 steps):** (1) **Extract** structured methods description, original results tables (parsed from PDF rendered as images, GPT-5-mini), and a "blinded" template with cell values masked; (2) **Reimplement** in a sandboxed environment containing only the methods + templates + symlink to data --- the original PDF, code, and results are physically inaccessible, with a two-stage audit (regex + GPT-5.4-mini) verifying compliance and a hardcoding check that flags outputs not derived from genuine computation; (3) **Evaluate** cell-by-cell against the original, assigning letter grades A--F by absolute % deviation (A: 0--2%, B: 2--20%, C: 20--40%, D: 40--60%, E: 60+%, F: missing/sign-flip); (4) **Explain** discrepancies via root-cause analysis (agent error / extractor error / original-paper error / data missing / unknown).
  - **Four agent scaffolds × four LLMs:** Claude Code, Codex CLI, mini-SWE-Agent, OpenCode × GPT-5.4, GPT-5.3 Codex, Claude Opus 4.6, GLM-5.
  - **Headline results.** Best three agents reproduce the **correct sign** of regression coefficients >85% of the time and fall **within the 95% CI** of the original estimate >70% of the time. **Best agent: OpenCode GPT-5.4** --- 91% sign agreement, >80% within the 95% CI.
  - **Scaffold-model interaction matters more than expected.** GPT-5.4 on OpenCode beats GPT-5.4 on Codex CLI and on mini-SWE-Agent. The OpenCode scaffold consumes more tokens, takes longer, and costs more --- the performance gain is partly a function of compute budget, not just model capability.
  - **Most discrepancies are not the agent's fault.** Root cause analysis attributes >75% of divergences to specific, interpretable sources: the **largest share is *original error*** (paper under-specifies or mis-specifies the original code), followed by missing data, then extractor error, then agent error. For the strongest agents, agent error becomes a relatively minor component.
  - **Underspecification examples:** in three cases the paper omits how `democrat support` is coded (`party=100`? `party=200`?), which F-statistic is used (Wald vs. Kleibergen-Paap), or default vs. specific statistical routines. Different agents make different default assumptions; the same human-caused ambiguity can either lead to a discrepancy or be silently resolved depending on which agent.
  - **Pre-training leakage check.** Compare 5 *Economic Journal* papers published before the model knowledge cutoff (Aug 2025) vs. 5 published after, using Claude Code (Opus 4.6) and Codex CLI (GPT-5.4). No statistically significant difference; if anything, post-cutoff is slightly higher. Suggests memorization is *not* the primary driver of reproduction performance.
  - **Re-run stability.** Stable at the table level (>80% of tables show grade spread ≤1 across three runs), but at the coefficient-cell level about *half* of estimates are statistically different from themselves across runs. Headline conclusions are robust to randomness; fine-grained agent-vs-agent comparisons should be interpreted with caution.
  - **Conceptual takeaway:** the paper concludes that the *source of truth* for "what was done" is already the code, not the paper. The paper's job is to explain *why*. The right policy response is not "make agents better" but "require explicit alignment between the narrative and the underlying code" --- agentic systems become a natural mechanism for surfacing inconsistencies between the two.

- **Summary**

Kohler et al. provide the first systematic benchmark of agentic reproduction *without* access to the original analysis code. The setup is rigorously designed to prevent leakage: agents see only an extracted methods description, blinded result-table templates, and a symlink to the data; the original PDF and code live on the same machine but outside the agent's sandbox, with a regex audit and an LLM-judge audit verifying compliance. A separate hardcoding audit flags any output that wasn't produced by genuine computation.

The empirical headline is encouraging for the agentic-reproducibility agenda: the best agent (OpenCode + GPT-5.4) recovers the correct sign 91% of the time and lands inside the 95% CI of the original estimate >80% of the time, across 48 published papers in top economics and political science journals. Three of the four scaffold-model combinations cluster in the 78--85% range for sign agreement, well above the 68% naive "guess positive" baseline.

The most consequential finding is in the error attribution. **The dominant failure mode is not the agent --- it's the paper.** Original-paper underspecification is the largest single source of divergence. Different agents handle the same ambiguity differently, so observed agent-quality differences partly reflect each agent's tendency to make implicit assumptions that happen to align with the original implementation. This reframes the path forward: progress comes from clearer methods documentation as much as from better agents.

The pre-training leakage analysis directly addresses an obvious objection. If the agents are succeeding because they memorized the papers in pre-training, the result tells us nothing about reproducibility. The pre/post-cutoff comparison shows no difference, supporting the interpretation that the agents are genuinely re-implementing, not retrieving. The original code is also mostly Stata/R; the agents write Python. Memorization-via-translation across languages would be unusually demanding.

The re-run stability analysis is a useful caveat against over-interpreting fine-grained agent comparisons: while the *table-level* conclusions are stable, *coefficient-level* estimates are noisy enough that ~half the time an agent's two independent reproductions of the same cell are statistically different from each other.

The conclusion shifts the framing. The "paper as source of truth" model is wrong even for human reproducibility; the code is the operational source of truth, and the paper explains motivation. Agents can serve as a verification tool that surfaces gaps between the two.

- **Relevance to Economics Research**

Direct and high. This is the most rigorous evidence to date on the *current* feasibility of agentic reproduction in empirical economics:

1. **Concrete capability ceiling.** OpenCode GPT-5.4 hits >80% within-95%-CI on top-journal papers without the code. That number is high enough to make agentic reproduction a real check on submissions, not a curiosity. It's also low enough that "agents can replace human replication" is overstated.

2. **The bottleneck is methods documentation, not models.** This argues for a journal-level intervention: explicit, structured methods sections, perhaps with executable specifications. Hall makes a similar argument in [[summaries/ai-10x-research]] on the journal-policy side; this paper provides the underlying empirical data point.

3. **Operational design of agentic-reproducibility pipelines.** The four-step Extract / Reimplement / Evaluate / Explain pipeline, the two-stage audit, and the deterministic letter-grade evaluation are reusable design patterns. The hardcoding-detection audit is non-trivial and worth borrowing for any agent-eval setup.

4. **For finance specifically:** the 48-paper dataset includes AER, EJ, RESt, AEJ:Pol, AEJ:AE, AEJ:Macro, QJE --- substantial overlap with empirical asset pricing and macro-finance. Stata/R-to-Python re-implementation maps directly onto the workflow Mihail and many empirical-finance researchers face when migrating MATLAB/Stata code to Python. The methods-description-as-bottleneck finding is directly actionable: write methods sections with the assumption that an agent will read them.

5. **Pairs with Andrew Chen's [[summaries/ralph-wiggum-asset-pricing|Ralph Wiggum loop]]** as the negative-space test: Chen used agents to *write* a paper from scratch; Kohler et al. test whether agents can *reproduce* a published paper's results. Together they bracket the agent-empirical-research feasibility envelope at this generation of models.

- **Related Concepts**
  - [[concepts/automated-research]]
  - [[concepts/ai-peer-review]]
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-research-tools]]

- **Related Summaries**
  - [[summaries/ai-10x-research]]
  - [[summaries/ralph-wiggum-asset-pricing]]
  - [[summaries/refine-ink-golub]]
  - [[summaries/coarse-ink]]
  - [[summaries/ai-powered-scholarship]]
  - [[summaries/cc-series-44-four-criteria-referee]]
  - [[summaries/agentic-everything]]
