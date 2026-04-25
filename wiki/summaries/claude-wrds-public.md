---
title: "Claude Code WRDS Toolkit (Liu fork of Orłowski's claude-wrds-public)"
tags: [summary, finance-econometrics]
sources:
  - "[[raw/articles/Claude WRDS skills.md]]"
date_updated: 2026-04-25
date_published: 2026-04
---

- **Author/Source**: Siyang Liu, GitHub repo (fork of Piotr Orłowski's `claude-wrds-public`, with added IBES, Compustat, and Fama-French expert agents)
- **Original**: [https://github.com/lsy617004926/claude-wrds-public](https://github.com/lsy617004926/claude-wrds-public)
- **Upstream**: [https://github.com/piotrek-orlowski/claude-wrds-public](https://github.com/piotrek-orlowski/claude-wrds-public)

- **Key Ideas**
  - A drop-in set of **Claude Code subagents and skills** for autonomous WRDS work: copy `agents/`, `skills/`, and `settings.json` into `~/.claude/`, append the bundled `CLAUDE.md` to your global `CLAUDE.md`, and Claude can query CRSP, Compustat, IBES, OptionMetrics, Fama-French, and TAQ from your terminal without the user writing SQL.
  - **Seven specialist agents:** `crsp-wrds-expert`, `compustat-wrds-expert`, `ff-wrds-expert`, `ibes-wrds-expert`, `optionmetrics-wrds-expert`, `taq-wrds-expert`, plus a `wrds-query-orchestrator` that coordinates multi-database queries (CRSP↔Compustat via `crsp.ccmxpf_lnkhist`, OptionMetrics↔CRSP via `wrdsapps.opcrsphist`, TAQ↔CRSP via `wrdsapps.taqmclink`).
  - **Three skills:** `wrds-psql` (connection patterns and single-line-command formatting rules), `wrds-ssh` (SSH connection, SAS batch submission, file transfer), and `wrds-schema` (a pre-loader skill --- `/wrds-schema crsp optionm` returns a compact reference card with table names, column types, date ranges, and known gotchas).
  - **Permissions are pre-approved** via `settings.json` for `Bash(psql service=wrds*)`, `Bash(ssh wrds*)`, `Bash(scp * wrds:*)`, `Bash(scp wrds:*)`. Without these, every WRDS call triggers a permission prompt.
  - **Setup files** required outside the repo: `~/.pg_service.conf` (host/port/dbname/user for `wrds`), `~/.pgpass` (with `chmod 600`), `~/.ssh/config` (`Host wrds` entry pointing at `wrds-cloud-sshkey.wharton.upenn.edu`), and a one-time `~/scratch` symlink (`ssh wrds 'ln -sf /scratch/$(basename $(dirname $HOME))/$(whoami) ~/scratch'`) so all agents can refer to scratch via a portable path.
  - **TAQ is special:** too large for direct PostgreSQL, so `taq-wrds-expert` writes a SAS program locally, `scp`s it to WRDS, submits via `qsas`, polls `qstat`, tails the log, and downloads the CSV. `-sync y` does not work on WRDS Cloud --- jobs are asynchronous only. TAQ scratch files auto-delete after 48 hours.
  - **OptionMetrics tables are yearly** (`optionm.opprcd2024`, not `optionm.opprcd`) --- a common pitfall the `optionmetrics-wrds-expert` is configured for.
  - Several **design decisions** worth borrowing for any WRDS-Claude setup: (1) use `psql service=wrds` instead of `$WRDS_USERNAME` shell variables, because shell substitutions trigger manual approval prompts every time; (2) enforce single-line psql commands (multi-line `\` continuation also triggers prompts); (3) use `psycopg2.connect("service=wrds")` from Python rather than the `wrds` pip package, which uses interactive auth prompts that don't work in non-interactive agent contexts; (4) add SSH `ControlMaster`/`ControlPersist 4h` if Duo MFA is prompting on every TAQ-workflow step.

- **Summary**

This is the canonical Claude-Code-friendly WRDS configuration --- the upstream that Dickerson's `ai-asset-pricing` repo (see [[summaries/dickerson-ai-asset-pricing]]) acknowledges as a starting point. The architecture is clean: per-database expert agents that know each schema's gotchas, lightweight skills that enforce shell-safe command patterns, and an orchestrator that handles multi-database link tables. The user just describes what they want ("Get me daily returns for AAPL and MSFT for 2024") and Claude routes the request through the appropriate agent → skill → SQL/SSH chain.

The most consequential design choices are about *avoiding permission-prompt thrash*. The `pg_service.conf` pattern, single-line `psql` enforcement, and pre-baked allow-listed Bash patterns all exist because shell-level dynamism (variables, multi-line continuations, command substitutions) interrupts agentic workflows with approval prompts that compound badly across long pipelines. This is a useful general pattern for anyone designing Claude tooling around any external service: the static, literal command form is the agentic-friendly form.

The Liu fork's contribution beyond Orłowski's original is the IBES, Compustat, and FF expert agents, plus the `wrds-query-orchestrator`. Liu's repo is the right starting point for someone setting up empirical asset-pricing or accounting work end-to-end.

- **Relevance to Economics Research**

Direct and very high for this user. Mihail's primary data access is the WRDS Python package; this toolkit is the agentic-Claude analogue and would slot into any AssayingAnomalies-style setup. The IBES, Compustat, FF, and CRSP agents cover the cross-section-of-expected-returns workhorse stack. TAQ support via SSH+SAS matches Mihail's existing trading-cost / microstructure projects, and the asynchronous-only constraint plus the 48-hour scratch expiry are real operational details that would otherwise need to be discovered the hard way.

The borrowable patterns even for someone not adopting the toolkit wholesale: pre-approved-permissions in `settings.json`, the `~/scratch` symlink for portable paths across users, `pg_service.conf` over shell-substitution, and the explicit "use `psycopg2.connect("service=wrds")` not the `wrds` pip package in agent contexts" are durable lessons for setting up any Claude-driven empirical finance project.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/claude-md-files]]
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-research-tools]]

- **Related Summaries**
  - [[summaries/claude-wrds-tools]]
  - [[summaries/dickerson-ai-asset-pricing]]
  - [[summaries/awesome-econ-ai]]
  - [[summaries/spina-paper]]
  - [[summaries/brownbag-claude-skills]]
  - [[summaries/cherny-code]]
