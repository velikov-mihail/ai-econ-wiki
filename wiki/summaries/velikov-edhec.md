---
title: "EDHEC Master Class: Using AI for Research"
tags: [summary, academic-research]
sources:
  - "[[raw/articles/EDHEC Master Class — Using AI for Research.md]]"
date_updated: 2026-05-15
date_published: 2026-05
---

- **Author/Source**: Mihail Velikov (Penn State, Smeal College of Business), May 2026 master class at EDHEC (Department of Finance, Economics, and Data Science)
- **Original**: [github.com/velikov-mihail/edhec-master-class](https://github.com/velikov-mihail/edhec-master-class)

## Key Ideas

- 6-hour master class structured as **two paired Beamer decks** (morning concept session + afternoon demo-led session) plus **six self-contained Claude Code demo workspaces** that each run in their own session.
- **Morning deck (`morning.tex`/`morning.pdf`)** — concept session: AI evolution, the agent loop, choosing tools, working with Claude Code, prompting and pitfalls, skills, subagents, hooks.
- **Afternoon deck (`afternoon.tex`/`afternoon.pdf`)** — demo-led session walking through the six demos in order.
- **Demo 1 (`demo1-skill/`)** — building a custom skill (`edhec-summary-stats`) that produces summary statistics from a CSV. Sample data ships with the repo, so the demo is runnable out of the box.
- **Demo 2 (`demo2-voice-skill/`)** — a `voice-extractor` skill that reads a corpus of the user's own published papers and produces a `VOICE.md` style guide for downstream writing tasks.
- **Demo 3 (`demo3-fred-agent/`)** — a hand-coded Think→Act→Observe agent against the FRED API using the Anthropic SDK directly (not through Claude Code). Requires `ANTHROPIC_API_KEY` and `FRED_API_KEY`.
- **Demo 4 (`demo4-referee-skill/`)** — an orchestrator skill that spawns three reviewer subagents in parallel against a working-paper PDF and consolidates their reports into a single referee package.
- **Demo 5 (`demo5-strategic-revision/`)** — Jukka Sihvonen's `strategic-revision` skill: takes a manuscript PDF, an editor letter, and reviewer reports, and produces a DAG-validated revision plan.
- **Demo 6 (`demo6-replication-pipeline/`)** — a mini autonomous CAPM-replication pipeline built around a state machine + JSON-schema validation + a verifier subagent. Requires WRDS credentials.
- Each demo folder has its own `CLAUDE.md` and skill/agent definitions under `.claude/`; the `SKILL.md` files are the fastest way to understand what each demo does.
- Compiled PDFs of both decks are committed alongside the LaTeX sources, so the materials are readable without a TeX install.
- Materials are released for educational use; third-party content (working papers, reviewer reports, proprietary data) is **not** included — users drop their own inputs into the relevant `sample-papers/`, `manuscript/`, `reviews/` folders before running.

## Summary

The EDHEC master class is Velikov's second public AI-for-research teaching artifact in 2026 (after the Smeal Community-of-Practice talk — see [[summaries/velikov-smeal-cop]]) and is the most hands-on of the two: a full day split between conceptual scaffolding (morning) and six runnable Claude Code workspaces (afternoon). Where the Smeal talk is a 50-minute synthesis aimed at faculty deciding whether to start, the EDHEC class is aimed at researchers who have already decided to start and now need a concrete on-ramp covering custom skills, hand-coded SDK agents, multi-agent referee pipelines, and a full autonomous replication loop.

The six demos are deliberately ordered from cheapest to most ambitious. Demo 1 builds the simplest possible skill (summary statistics from a CSV); Demo 2 extends the same idea to voice extraction from a paper corpus — both showing that "skills" are just folders with a `SKILL.md`. Demo 3 drops into raw Anthropic SDK code to show what the Claude Code harness is actually doing under the hood (the think–act–observe loop against FRED, the same example used in the Smeal deck). Demos 4 and 5 introduce subagent orchestration — Demo 4 (three parallel reviewer subagents) is Velikov's own; Demo 5 is Jukka Sihvonen's `strategic-revision` skill, included with attribution. Demo 6 is the capstone: a CAPM-replication pipeline with state-machine control flow, JSON-schema validation, and a verifier subagent — an end-to-end miniature of the design discipline formalized in [[summaries/zeropaper-paper]].

The repo's deliberate omission of third-party content (working papers, reviewer reports, proprietary data) is the practical answer to the licensing and confidentiality concerns that have dominated recent autonomous-research discourse. Users bring their own inputs; the demos provide the agent infrastructure.

## Relevance to Economics Research

The EDHEC class is the most operational teaching artifact in this wiki: a single repository where an empirical-finance researcher can clone, install, and run a graded sequence from "first custom skill" through "autonomous CAPM replication pipeline" in one day. Three things matter for economists evaluating it:

1. **Demos 1–2 lower the barrier to custom skills.** The `edhec-summary-stats` and `voice-extractor` skills are short enough to read in one sitting, which is the most direct way to demystify the `SKILL.md` format. After Demo 2, researchers should be able to write their own skills against their own paper corpora.
2. **Demo 3 makes the harness/SDK distinction concrete.** Most researchers encounter Claude Code first and never see the underlying API. Building a ~100-line FRED agent directly against the Anthropic SDK is the cleanest way to show that the "intelligence" lives in the prompts and tool definitions, not in the harness. This is the same FRED example Korinek used (see [[summaries/applications-generative-ai]]).
3. **Demos 4–6 are a graded ladder into multi-agent and autonomous systems.** Demo 4 (parallel referees) is the lightest multi-agent pattern; Demo 5 (DAG-validated revision plan) introduces structured artifact validation; Demo 6 (autonomous CAPM replication with state-machine + verifier) is the smallest faithful implementation of the [[summaries/zeropaper-paper|ZeroPaper-style]] design discipline a researcher can productively study end-to-end.

For finance researchers in particular, Demo 6's WRDS-credentialed CAPM pipeline is directly portable: replace CAPM with any other asset-pricing replication and the same state-machine + verifier scaffold applies.

## Related Concepts

- [[concepts/claude-code-skills]]
- [[concepts/ai-agents]]
- [[concepts/agentic-workflows]]
- [[concepts/multi-agent-systems]]
- [[concepts/claude-md-files]]
- [[concepts/automated-research]]
- [[concepts/ai-peer-review]]
- [[concepts/wrds-data-access]]

## Related Summaries

- [[summaries/velikov-smeal-cop]] — Velikov's earlier April 2026 Smeal CoP talk; conceptual scaffolding for this hands-on master class
- [[summaries/ai-powered-scholarship]] — Novy-Marx & Velikov's mass-produced finance-paper pipeline
- [[summaries/zeropaper-template]] — Lopez-Lira's clonable autonomous-pipeline template; the production-scale analog of Demo 6
- [[summaries/zeropaper-paper]] — design discipline behind autonomous-research pipelines; informs Demo 6's state-machine + verifier scaffold
- [[summaries/claude-wrds-tools]] — Orlowski's Claude Code WRDS toolkit; complementary to Demo 6's WRDS pipeline
- [[summaries/refine-ink-golub]] — Golub & Brunnermeier's AI-powered referee report tool; conceptual sibling of Demo 4
- [[summaries/haaland-reviewer]] — Haaland's reproducible multi-agent reviewer; another sibling of Demo 4
- [[summaries/teaching-ai-your-voice]] — voice-file workflows; conceptual sibling of Demo 2
- [[summaries/brownbag-claude-skills]] — Spina's practical introduction to Claude Code skills for academic researchers
- [[summaries/panjwani-codex-course]] — Panjwani's parallel hands-on course for OpenAI Codex
