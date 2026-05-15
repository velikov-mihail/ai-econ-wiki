---
title: "ZeroPaper: Enhanced AI-Assisted Research Template with Agentic Capabilities"
tags:
- summary
- finance-econometrics
- automated-research
- finance-research
- AI-pipeline
sources:
- '[[raw/articles/ZeroPaper - Enhanced AI-assisted research template with agentic capabilities.md]]'
date_updated: 2026-05-15
date_published: 2026-05-01
---

- **Author/Source**: Alejandro Lopez-Lira (GitHub: `alejandroll10/zeropaper`, 2026-05-01)
- **Original**: [https://github.com/alejandroll10/zeropaper](https://github.com/alejandroll10/zeropaper)

## Key Ideas

- ZeroPaper is now released as an open template: clone the repo once, run `setup.sh` to scaffold a project, then say "Run the pipeline" inside Claude Code, OpenAI Codex CLI, or Gemini CLI. The pipeline runs autonomously through problem discovery → idea generation → theory → math verification → paper writing → simulated referee review.
- A single Claude Code Max-tier subscription (~$200/month) supports roughly **100 papers/month**, putting the amortized cost at ~$2 per paper. Pay-per-token API access works but is ~1000× more expensive at current rates (~$2,000/paper) because of heavy subagent dispatch.
- Variants target different journals: `--variant finance` (JF, JFE, RFS) and `--variant macro` (AER, Econometrica, QJE, JPE, ReStud, JME). Extensions are additive: `--ext empirical` adds CRSP/Compustat/FRED/Ken French/Chen-Zimmerman/WRDS data agents; `--ext theory_llm` adds LLM-experiment agents via UF NaviGator.
- Pipeline has 10 numbered stages and 6 adversarial gates: every substantive advance is gated by a fresh-context agent that has not seen the generator's reasoning, with at least two evaluators at math gates and three simulated referees at the publication gate.
- Roughly 30 specialized agents: `literature-scout`, `idea-generator`, `idea-reviewer`, `idea-prototyper`, `theory-generator`, `math-auditor`, `math-auditor-freeform`, `novelty-checker`, `theory-explorer`, `self-attacker`, `scorer`, `paper-writer`, `referee`, `style`, six `polish-*` agents (consistency/formula/numerics/institutions/equilibria/bibliography), `bib-verifier`, `scribe`, and (with extensions) `empiricist`, `empirics-auditor`, `experiment-designer`, `experiment-reviewer`.
- Additional modes: `--manual` ships the agents as a standalone research toolkit without the autonomous loop, `--seed` lets you drop existing notes/drafts into `output/seed/` and have the pipeline triage entry, `--light` swaps Sonnet in for all subagents to cut cost.
- License is restrictive even for open release: submission of any pipeline-produced work to a journal/preprint/conference requires **prior written notice** (60-day fallback), AI-disclosure is mandatory, watermarks are non-cosmetic and removal terminates the license, and commercial use is prohibited without a separate license. Share-alike applies to derivatives.
- Safety defaults sandbox bash to the project folder, block SSH/AWS credential reads, and (on Linux) enforce restrictions via `bubblewrap`; on macOS Seatbelt is used.

## Summary

This release moves ZeroPaper from a private collaboration-by-invitation system (see [[summaries/automated-research-finance]]) to a publicly clonable template. The same pipeline that produced the 22-paper gallery (see [[summaries/zeropaper-gallery]]) is now scaffoldable in a single shell command, and crucially is **runtime-portable**: the same pipeline state is consumed identically by Claude Code, OpenAI Codex CLI, and Gemini CLI through three parallel orchestration docs (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`). A session can be interrupted in one runtime and resumed in another.

The architectural commitments visible in the README are the practical surface of the design principles developed in the [[summaries/zeropaper-paper|companion paper]]: state lives in a compact JSON file that every stage reads and writes (not in conversation history); the orchestrator only routes — actual work is dispatched to fresh-context subagents; every gate runs adversarial verifiers with distinct framings; and termination is mechanical, not at the orchestrator's discretion. The dashboard at `localhost:8000/dashboard.html` exposes stage transitions and gate verdicts live, and the pipeline commits to git at every transition, giving researchers an auditable trail.

For an empirical-finance user, the most consequential piece is the `--ext empirical` extension, which bundles skills for SEC EDGAR, FRED, Ken French, Chen-Zimmerman's Open Source Asset Pricing signals, mutual-fund holdings, flexible empirical specification mining, and full WRDS access (CRSP, Compustat, IBES, options, insider trading). This is the same data perimeter Lopez-Lira used to generate the gallery papers, now exposed for arbitrary new projects.

## Relevance to Economics Research

ZeroPaper is the first widely accessible autonomous-research pipeline targeting top finance and macro journals where the entire toolchain is documented, runnable on consumer-tier AI subscriptions, and tested against published-paper benchmarks. Three points matter for economists evaluating these systems:

1. **Cost structure is no longer the binding constraint.** At ~$2/paper amortized on a $200/month subscription, the marginal cost of an additional pipeline run is effectively zero. This shifts the bottleneck from compute budget to idea quality, research-question novelty, and human review capacity — exactly the substitution the [[summaries/thread-arindube]] post predicts.
2. **The license terms preview the publishing-side fight.** Mandatory submission notice, AI-disclosure, and non-removable watermarks operationalize the disclosure regime that journals will need if they want to track AI-produced submissions. Researchers using ZeroPaper inherit these obligations whether or not their target journal has a policy yet.
3. **The runtime-portability claim is testable.** Because the same state JSON drives all three CLIs, ZeroPaper provides a controlled setting for measuring how much of "AI research quality" depends on model choice vs. orchestration. This connects to [[concepts/multi-agent-systems]] and to the design-principle arguments in the [[summaries/zeropaper-paper|companion paper]].

For users of [[summaries/ai-powered-scholarship]], [[summaries/dickerson-ai-asset-pricing]], [[summaries/ralph-wiggum-asset-pricing]], and [[summaries/project-ape]], this is the most direct head-to-head reference implementation now available for finance research pipelines.

## Related Concepts

- [[concepts/automated-research]]
- [[concepts/multi-agent-systems]]
- [[concepts/ai-agents]]
- [[concepts/claude-code]]
- [[concepts/wrds-data-access]]
- [[concepts/reproducibility-transparency]]

## Related Summaries

- [[summaries/zeropaper-paper]] — companion paper formalizing the ten premises and six design principles behind this pipeline
- [[summaries/automated-research-finance]] — the original collaboration call before the public template
- [[summaries/zeropaper-gallery]] — 22 finance papers actually produced by this pipeline
- [[summaries/stress-test-research-pipeline]] — Lopez-Lira's upstream idea-evaluation tool
- [[summaries/ai-powered-scholarship]] — Novy-Marx & Velikov's parallel finance-paper pipeline
- [[summaries/dickerson-ai-asset-pricing]] — Dickerson's multi-agent asset pricing repo
- [[summaries/ralph-wiggum-asset-pricing]] — Chen's open-source Ralph loop framework
- [[summaries/project-ape]] — Social Catalyst Lab's automated policy-evaluation pipeline
- [[summaries/applications-generative-ai]] — Korinek's taxonomy of generative-AI uses in economics
