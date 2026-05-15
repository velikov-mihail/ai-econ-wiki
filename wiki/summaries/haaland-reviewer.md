---
title: "Reviewer: A Reproducible Multi-Agent Reviewer for Economics Papers"
tags: [summary, academic-research, peer-review, codex, multi-agent]
sources:
  - "[[raw/articles/Reviewer.md]]"
date_updated: 2026-05-15
date_published: 2026
---

- **Author/Source**: Ingar Haaland (NHH / CESifo), GitHub
- **Original**: [https://github.com/Ingar30/reviewer](https://github.com/Ingar30/reviewer)

- **Key Ideas**
  - **Multi-agent reviewer for academic economics papers**, run via Codex CLI. Pure workflow machinery — preprocessing scripts, reviewer prompts, schemas, validators, normalizers, editor assembly, and tests. Source PDFs and generated review outputs stay local and private.
  - Single command entry point: `python scripts/review_paper.py --pdf "inputs/<paper_id>.pdf"` runs the full pipeline.
  - **10-step pipeline**: (1) PDF preprocessing → structured artifacts under `work/<paper_id>/parsed/`; (2) render run-specific prompts; (3) parser-quality preflight before substantive review; (4) optional experimental parser repair LLM agent when preflight reports high/medium-severity parser artifacts; (5) dynamic reviewer selection (always running mandatory reviewers + optional ones); (6) schema and semantic validation of every reviewer JSON output; (7) normalization and deduplication into an editor bundle; (8) editor input assembly; (9) editor writes `outputs/<paper_id>/report.md`; (10) structural and traceability smoke-checks on the final report.
  - **Reviewer configuration** lives in `config/reviewers.json` — each entry declares name, prompt template, output filename, finding ID prefix, whether search is required, normalization role, and stage (`preflight` or `review`).
  - Codex-native: `AGENTS.md` carries workflow and safety instructions; `.codex/config.toml` carries project defaults; `.agents/skills/paper-reviewer/SKILL.md` carries the reusable workflow playbook.
  - Explicit privacy hygiene: source PDFs, parsed artifacts, reviewer logs, and final reports are gitignored. A pre-push scanner (`scripts/check_tracked_sensitive_names.py`) catches accidental commits of sensitive variable names.
  - Open development model — public machinery, private papers. Forks extend via reviewer entries, prompt templates, and matching validation/normalization tests.

- **Summary**

Haaland's Reviewer is the cleanest open-source implementation of the multi-agent peer-review pattern aimed specifically at economics papers. The architecture choices are conservative and well-engineered: schema-validated JSON for every reviewer output, deterministic normalization and deduplication, an explicit editor stage that assembles the final report from the normalized bundle, and structural smoke-checks at the end. The optional parser-repair agent is an interesting touch — when the PDF parser produces artifacts that would otherwise corrupt reviewer outputs, an LLM agent is dispatched specifically to repair the parsed text before review begins, rather than letting downstream reviewers reason over garbage.

The privacy model is a deliberate departure from most AI-paper-review projects: only the workflow machinery is public; no source PDFs, parsed artifacts, reviewer JSON, or generated reports are committed. Pre-push scanners catch sensitive-variable-name leakage. This makes the repo safely forkable by other researchers without exposing their private review work.

- **Relevance to Economics Research**

Directly applicable. Reviewer is the most economics-specific public peer-review pipeline currently available, with a maintainer who is an active empirical economist. Three pieces are especially worth borrowing: (1) the **schema-validated reviewer outputs** pattern — every reviewer must emit a JSON object that passes both schema and semantic checks, eliminating "the LLM rambled and I have to parse free text" downstream; (2) the **mandatory + optional reviewers** dispatcher with dynamic selection per paper; (3) the **privacy-first repository hygiene** model (public machinery, private artifacts, pre-push scanners) which solves a real publishing problem for academics who want to share AI-tooling without sharing draft manuscripts. Worth comparing directly with [[ars-claude-code|ARS]] (more elaborate, Claude-Code-native, IS/management-oriented) and [[coarse-ink|coarse.ink]] (lighter, single-pass, ~$2/review).

- **Related Concepts**
  - [[concepts/ai-peer-review]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/data-privacy]]
  - [[concepts/automated-research]]

- **Related Summaries**
  - [[summaries/ars-claude-code]]
  - [[summaries/coarse-ink]]
  - [[summaries/katmer-code]]
  - [[summaries/point-by-point]]
  - [[summaries/cc-series-44-four-criteria-referee]]
