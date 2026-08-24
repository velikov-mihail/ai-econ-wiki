---
title: "Claude Code for Academics: APSA 2026 Presentation (Spina)"
tags: [summary, academic-research, claude-code, foundations-setup, claude-md-files, ai-agents]
sources:
  - "[[raw/pdfs/Alessandro_APSA_Part1_2026.pdf]]"
date_updated: 2026-06-20
date_published: 2026-06-20
---

- **Author/Source**: Alessandro Spina, University of Technology Sydney (UTS Finance) — 3rd APSA Workshop on Quantitative Methods 2026
- **Original**: [https://www.alessandro-spina.com/claude-code/](https://www.alessandro-spina.com/claude-code/)

## Key Ideas

- Claude Code = LLM + Tools running inside your project folder: reads files → runs commands → produces output. Framed as a dedicated "RA" rather than a chatbot.
- **The Amnesia Problem**: Claude Code forgets everything between sessions. Solution: build external memory in markdown files — `CLAUDE.md` (ground rules, key decisions), `README.md` (directory map), `session_log.md` (what was done and why, one file per session named by date).
- **The Context Window Problem**: Quality degrades as the context fills; use `/compact` proactively, run one task per session.
- **Project scaffold**: CLAUDE.md (ground rules), README.md, DATA.md (source, license, AI-upload safety per dataset), SCRIPT REGISTRY.md (one line per script: inputs, outputs, question answered), PINBOARD.md (to-dos, ideas, data issues).
- **The Cunningham Conjecture**: Cross-language replication (R = Stata = Python to 6 decimal places) as a verification strategy. The DGP for coding errors is orthogonal across languages, so mismatches reveal bugs that single-language review misses.
- **Skills** are reusable instruction files (markdown); **Slash commands** are explicitly invoked one-shot actions. Skills say "whenever this topic comes up, apply these conventions"; commands say "do this now."
- Examples of skills built: `/spin-up` (brief Claude at session start), `/wrap-up` (save session log), `/code-sweep` (audit code vs. paper), `/paper-editor` (seven-audit editorial review), `/data-profiler`, `/glossary`, `/pinboard`.
- **Failure modes and defenses**: fake citations → local PDFs only; wrong estimator → cross-language verification; sycophancy → adversarial personas and agent teams.
- **Safety**: scope access to one project folder; CLAUDE.md specifies what Claude can/cannot do; start in Plan mode (never YOLO mode); use settings.json allow/deny rules; version control via Git/Dropbox. Run Claude in a Docker container (Goldsmith-Pinkham's `claude-container`) to prevent any file access leakage.
- **Data privacy**: only files Claude actively reads enter the API context. Use Claude Code for code (referencing file paths), not raw data. Document AI-upload status per dataset in DATA.md.
- **The bottleneck is you**: Claude generates output faster than you can verify. One task at a time; read everything before re-prompting.
- Four habits for effective AI use: (1) Start in Plan mode, (2) Define terms (ask Claude to explain jargon in its own words — "translation errors" not hallucinations), (3) Be specific, (4) Separate action from judgment (AI drafts; you decide what is true).
- ROI framing: use AI when (labor saved + verification cost + privacy risk + maintenance cost) < setup cost. High-ROI: data cleaning, figures, code auditing, slide formatting. Low-ROI: novel theoretical arguments, one-off tasks faster to do by hand.

## Summary

Spina's APSA 2026 presentation is a comprehensive, practically grounded introduction to Claude Code for academic economists and social scientists. Delivered at the 3rd APSA Workshop on Quantitative Methods, it builds from first principles — what an AI agent actually is, and why it's different from a chatbot — through full project scaffolding, skill construction, safety protocols, and honest assessment of failure modes and bottlenecks.

The presentation is distinguished by its focus on *systems thinking* rather than one-off prompts: the project scaffold (CLAUDE.md, DATA.md, session logs, script registry, PINBOARD.md) creates external memory that survives the amnesia problem across sessions. The Cunningham Conjecture on cross-language replication offers a practical falsification strategy for AI-generated code. The slide deck was itself built with Claude Code — Spina wrote the bullet points, Claude wrote the LaTeX, iterating together — making it a meta-example of the workflow it describes.

Honest downsides are named directly: the bottleneck is the researcher's attention, not Claude's speed; cognitive switching costs make parallel sessions hard to read carefully; and workflow optimization can become a productivity trap. The final framing — "the mechanical work gets faster; the thinking takes the same time it always did" — is one of the clearest articulations of the human-AI collaboration balance in this wiki.

## Relevance to Economics Research

This is one of the best single-resource overviews of Claude Code for academic economists, particularly for those in empirical fields (political science, economics). It directly addresses the core concerns of applied researchers: data privacy, replication and verification, avoiding fake citations, maintaining reproducible project structure, and the ROI calculation for adopting AI tools. The session-log and script-registry recommendations are immediately actionable. The Cunningham Conjecture cross-language verification strategy deserves wide adoption.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/claude-md-files]]
- [[concepts/agentic-workflows]]
- [[concepts/ai-limitations]]
- [[concepts/data-privacy]]
- [[concepts/human-in-the-loop]]
- [[concepts/cross-language-replication]]

## Related Summaries

- [[summaries/spina-paper|Claude Code for Academics (earlier version)]]
- [[summaries/brownbag-claude-skills|Brownbag: Claude Code Skills (Spina)]]
- [[summaries/getting-started-economists|Getting Started: Claude Code for Economists (Goldsmith-Pinkham)]]
- [[summaries/cc-series-12-empirical-research|How I Use Claude Code for Empirical Research (Cunningham)]]
- [[summaries/cc-series-24-agents-auditing-did|Multiple Agents Auditing Your DiD Code (Cunningham)]]
