---
title: "ai-asset-pricing: Empirical Asset Pricing Tools (Dickerson)"
tags: [summary, finance-econometrics]
sources:
  - "[[raw/articles/ai-asset-pricing Empirical Asset Pricing Tools.md]]"
date_updated: 2026-04-25
date_published: 2026-04-18
---

- **Author/Source**: Alexander M. Dickerson, GitHub repo
- **Original**: [https://github.com/Alexander-M-Dickerson/ai-asset-pricing](https://github.com/Alexander-M-Dickerson/ai-asset-pricing)

- **Key Ideas**
  - A multi-agent-friendly empirical asset pricing research repo: clone it, ask Claude Code (`/onboard`), Codex, or Gemini CLI to onboard, and you reach a research-ready WRDS workflow without hand-editing machine-specific config inside the shared tree.
  - Three parallel adapters cover the major coding agents: `CLAUDE.md` (Claude), `AGENTS.md` (Codex), `GEMINI.md` (Gemini CLI), all routing through a shared `tools/bootstrap.py` audit/apply engine. The shared cold-start scripts are `tools/onboard.ps1` (PowerShell) and `tools/onboard.sh` (bash).
  - Coverage spans the full empirical-asset-pricing stack: WRDS data extraction, factor-model setup and reusable automation, a `fintools/` shared utility package, the `PyBondLab` portfolio-construction package, and LaTeX paper scaffolding/auditing/compilation.
  - **Local state is kept *outside* the repo** in a per-user OS-specific directory (canonical files: `local_env.md`, `claude.local.md`, `settings.local.json`). This is explicitly designed to make the repo safe in a shared Dropbox/OneDrive working tree --- machine-local paths don't sync across users. Repo-root compatibility shims (`CLAUDE.local.md`, `.claude/settings.local.json`) are legacy and only generated on request.
  - WRDS access is optional. The agent asks once at onboarding; without WRDS, the repo still supports skills/rules/agents, `fintools`, `PyBondLab` install with bundled-data smoke tests, and LaTeX boilerplate.
  - Manual WRDS bootstrap files are documented: `~/.pg_service.conf`, `~/.pgpass` (with `chmod 600`), and `~/.ssh/config` `Host wrds` entry for SSH/TAQ workflows.
  - Acknowledges Piotr Orlowski's `claude-wrds-public` agents and Scott Cunningham's `MixtapeTools` as starting points, both heavily augmented.

- **Summary**

Dickerson's `ai-asset-pricing` repo is best understood as a *template* for setting up a Claude-Code-friendly empirical asset pricing project, with parallel support for Codex and Gemini CLI. The design choices reflect lessons that show up across this wiki: agent context lives in markdown (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`), reusable workflow content lives in plain markdown under `.claude/agents/`, `.claude/skills/`, `.claude/rules/` so it can be reused across tools, and a single shared `bootstrap.py` engine handles the actual Python-environment setup so the per-tool adapters stay thin.

The most consequential design decision for finance researchers working in shared file systems (Dropbox/OneDrive) is that canonical local state is held *outside* the repo. This avoids the well-known footgun where a coauthor opens the repo on a different machine and Claude reads stale paths from a synced `.claude/settings.local.json`.

The functional surface includes WRDS-oriented data work, factor-model research scaffolding, `PyBondLab` for portfolio construction, and LaTeX writing infrastructure. Onboarding is `tools/bootstrap.py audit` → execute the emitted `bootstrap_plan` → `apply` → re-`audit`, with cross-platform entry points (`onboard.ps1` / `onboard.sh`).

- **Relevance to Economics Research**

Direct and high. This is a working reference implementation of "what a Claude-Code-ready empirical finance project looks like" --- the AssayingAnomalies/finance-research analog. Anything I (or anyone running an empirical asset-pricing project on WRDS) would build looks structurally similar to this. Specific patterns worth borrowing: external local-state files for Dropbox safety; parallel adapters for Claude/Codex/Gemini so the project isn't locked to one vendor; `bootstrap.py audit/apply` as the shared environment-setup engine; the conditional WRDS prompt at onboarding so the repo also works for collaborators without WRDS.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/claude-md-files]]
  - [[concepts/claude-code-skills]]
  - [[concepts/ai-research-tools]]

- **Related Summaries**
  - [[summaries/awesome-econ-ai]]
  - [[summaries/spina-paper]]
  - [[summaries/cherny-code]]
  - [[summaries/ai-powered-scholarship]]
