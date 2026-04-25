---
title: "ralph-wiggum-asset-pricing: Open-Source Loop for Generating Asset Pricing Papers"
tags: [summary, finance-econometrics]
sources:
  - "[[raw/articles/chenandrewyralph-wiggum-asset-pricing.md]]"
date_updated: 2026-04-25
date_published: 2026-04
---

- **Author/Source**: Andrew Y. Chen (Federal Reserve Board), GitHub repo
- **Original**: [https://github.com/chenandrewy/ralph-wiggum-asset-pricing](https://github.com/chenandrewy/ralph-wiggum-asset-pricing)

- **Key Ideas**
  - Open-source framework that generalizes the workflow used to generate "Hedging the Singularity" (see [[summaries/prompts-to-paper]]). Implements Geoff Huntley's "Ralph Wiggum loop": plan → improve → test → repeat, with a human staying *on* the loop rather than *in* it.
  - Each iteration: `ralph/author-plan.py` reads test results + `spec/paper-spec.md` and writes `ralph-garage/improvement-plan.md`; `ralph/author-improve.py` executes the plan; `tests/*.py` evaluates; failures send the loop back to step 1.
  - **Branch model:** humans work on `main`, Ralph works only on `ralph/run`, with each iteration being a single `rloop-NN:` commit. This makes stopping, resuming, and discarding stretches cheap. `go-ralph-go.sh` from `main` starts/extends a stretch; from `ralph/run` it resumes.
  - **YOLO mode:** Ralph invokes Claude with `--dangerously-skip-permissions` and Codex with `--sandbox danger-full-access`. The recommended sandbox is the included dev container (Docker), which isolates the YOLO agents and provides bash, git, Python, R, LaTeX (`pdflatex`, `biber`), Poppler, and the agent CLIs.
  - Multi-agent support via three module-level constants per script (`AGENT`, `MODEL`, `EFFORT`); checked-in defaults are Claude. Each test/referee can use its own agent/model/effort tier.
  - **Test taxonomy** (the full 25-test version on `ralph/run-final` for "Hedging the Singularity"): `element-*` (required content present), `factcheck-*` (claims match code/lit/each other), `spec-*` (paper matches spec), `theory-*` (clarity, no deadweight, intro pay-off), `visual-*` (figures render), `writing-*` (intro and intuition prose). Plus a `build-latex` infrastructure test.
  - Ships with a *blank* template; users replace `spec/paper-spec.md` and `spec/economic-background.md` with their own paper. Optionally `bash check-ralph-direction.sh` to have AIs generate candidate starting points first.
  - `tests/` for the asset-pricing theory paper is a small subset; for empirical papers Chen points to `HumanxAI-ChenAY`'s test set, with families like `factcheck-econ`, `story-narrative`, `story-exhibit-coherence`, `transparency-calibration`, `visual-tables`. Treat them as source material to port, not files to copy.
  - **Cost reference point:** "Hedging the Singularity" with all 25 tests burned through two $200/month Claude Code subscriptions end-to-end. The default `main` test set is much lighter.
  - WRDS credentials handled via host-side `python .credentials/setup.py`, exposed inside the dev container as `WRDS_USERNAME` / `WRDS_PASSWORD` environment variables.

- **Summary**

This repo is the productionized, generalizable version of the workflow Chen used in "Hedging the Singularity." Where [[summaries/prompts-to-paper|Prompts-to-Paper]] is a frozen archive of the prompts that produced one paper, `ralph-wiggum-asset-pricing` is a reusable scaffold: clone it, replace the spec and tests, hit `bash go-ralph-go.sh`, and the agents will iterate on a paper draft until your tests pass.

The interesting design choices are about controlling agent behavior at scale. The two-branch model (`main` for humans, `ralph/run` for the agent) treats agent output as cheap and disposable: a stretch that goes badly is a `git branch -D ralph/run` away from being undone. Tests are first-class: failures drive the loop, so the test suite is essentially the spec for the paper's quality bar. The honesty about cost (two $200/month subscriptions for one paper) is unusual and useful as a planning anchor.

Chen's preface to "Hedging the Singularity" (linked from the README) reports that an attempted "human as Clockmaker" mode --- setting everything up correctly upfront and then leaving Ralph alone --- did not work. The lesson seems to be that paper-quality output still requires active human steering of the spec, the test mix, and the prose direction. This complements (and tempers) the headline claim from prompts-to-paper.

- **Relevance to Economics Research**

Highly relevant for finance/economics researchers who want to experiment with paper-generation pipelines. Three things make this concrete in a way most "AI for research" discussions aren't: (1) full source for the loop, the prompts, and the test suite is published; (2) the recommended cost ($200/mo × 2 subscriptions) is a real number to plan against; (3) the test taxonomy is reusable scaffolding even if you never run the full loop --- adopting just the `factcheck-code`, `factcheck-lit`, and `spec-paper` tests as a CI step on a human-written paper is a low-cost experiment.

For asset-pricing/empirical-finance work specifically, the pointer to `HumanxAI-ChenAY`'s test families (`factcheck-econ`, `story-narrative`, `transparency-calibration`, `visual-tables`) is more relevant than the bundled theory tests --- those are the failure modes empirical finance papers actually have.

- **Related Concepts**
  - [[concepts/automated-research]]
  - [[concepts/agentic-workflows]]
  - [[concepts/human-ai-collaboration]]
  - [[concepts/ai-research-tools]]

- **Related Summaries**
  - [[summaries/prompts-to-paper]]
  - [[summaries/ai-powered-scholarship]]
  - [[summaries/dickerson-ai-asset-pricing]]
  - [[summaries/automated-research-finance]]
  - [[summaries/ai-one-shot-papers]]
