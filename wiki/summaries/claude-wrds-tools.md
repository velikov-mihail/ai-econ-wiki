---
title: "Claude Code WRDS Toolkit (piotrek-orlowski/claude-wrds-public)"
tags: [summary, WRDS, CRSP, Compustat, OptionMetrics, TAQ, claude-code, agents, skills]
sources:
  - "[[raw/articles/piotrek-orlowskiclaude-wrds-public.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Piotrek Orlowski (GitHub: piotrek-orlowski). Repository: claude-wrds-public.

## Key Ideas

- The toolkit provides a set of Claude Code agents, skills, and configuration files that let Claude autonomously query WRDS databases (CRSP, Compustat, OptionMetrics, TAQ) directly from the terminal using natural language.
- **Specialist agents** handle different databases: `crsp-wrds-expert` for stock data, `optionmetrics-wrds-expert` for options, `taq-wrds-expert` for high-frequency data, and a `wrds-query-orchestrator` for cross-database queries.
- **Skills** encode connection patterns and best practices: the `wrds-psql` skill enforces single-line psql commands to avoid shell-expansion approval prompts; the `wrds-ssh` skill handles SSH connections and SAS job submission for TAQ.
- TAQ data is handled fundamentally differently (SSH + SAS batch jobs on the WRDS grid) because it is too large for direct PostgreSQL queries.
- Cross-database linking is built in: OptionMetrics to CRSP via `wrdsapps.opcrsphist`, CRSP to Compustat via `crsp.ccmxpf_lnkhist`, TAQ to CRSP via `wrdsapps.taqmclink`.
- Design decisions favor automation-friendliness: `pg_service.conf` avoids shell variable expansion prompts; a `~/scratch` symlink makes paths portable across institutions; the `wrds` Python pip package is avoided because its interactive authentication breaks non-interactive Claude Code sessions.
- Schema pre-loading (`/wrds-schema`) avoids exploratory round-trips by front-loading table names, column types, date ranges, and known gotchas.

## Summary

This GitHub repository provides a complete toolkit for integrating Claude Code with WRDS, the primary data platform used by academic finance and economics researchers. The toolkit is organized into three layers: specialist agents that know the schema and best practices for individual databases, skills that encode connection patterns and formatting rules, and a settings file that pre-approves common WRDS commands (psql, ssh, scp) so Claude can operate without repeated permission prompts.

Setup involves configuring PostgreSQL service and password files for direct database access, SSH keys for WRDS cloud access (required for TAQ), and a scratch space symlink for portable file paths. Once configured, users simply describe what data they need in natural language -- "Get me daily returns for AAPL and MSFT for 2024" or "Merge CRSP monthly returns with Compustat annual fundamentals" -- and Claude delegates to the appropriate specialist agent. For cross-database queries, the orchestrator agent coordinates between specialists and composes the appropriate link tables.

The TAQ workflow is notably different: the agent writes SAS programs locally, uploads them to WRDS via SCP, submits them as asynchronous batch jobs via SSH, polls for completion, and downloads results. The README documents several TAQ-specific gotchas, including variable naming inconsistencies (SYM_ROOT vs. SYMBOL_ROOT), the lack of synchronous job submission, and the 48-hour scratch file auto-deletion policy. The toolkit also addresses practical issues like Duo two-factor authentication (recommending SSH connection multiplexing to avoid repeated prompts) and OptionMetrics yearly table naming conventions.

## Relevance to Economics Research

This toolkit directly addresses the data access bottleneck in empirical finance research. WRDS is the standard data source for academic work involving CRSP stock returns, Compustat fundamentals, OptionMetrics implied volatilities, and TAQ high-frequency data. By enabling natural language queries against these databases through Claude Code, the toolkit eliminates much of the boilerplate SQL writing, schema lookup, and cross-database linking that consumes researcher time. It is particularly relevant for researchers who regularly merge across CRSP, Compustat, and OptionMetrics, or who need to extract data from TAQ's large-scale high-frequency archives.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/agents-and-skills]]
- [[concepts/data-pipelines]]
- [[concepts/agentic-coding]]
- [[concepts/wrds-data-access]]

## Related Summaries

- [[summaries/data-analysis-economists]]
- [[summaries/getting-started-economists]]
