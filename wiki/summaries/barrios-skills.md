---
title: "Barrios Skills — AI Workflows for Academic Research (Barrios)"
tags: [summary, claude-code-skills, mcp, wrds, accounting, finance, writing]
sources:
  - "[[raw/articles/Barrios Skills — AI workflows for academic research.md]]"
date_updated: 2026-09-30
date_published: 2026-09
---

- **Author/Source**: John Manuel Barrios, project page on his personal site with a companion GitHub repository (undated; clipped September 2026)
- **Original**: [https://johnmbarrios.com/barrios-skills/](https://johnmbarrios.com/barrios-skills/) · repo: [github.com/Barrios88/barrios-skills](https://github.com/Barrios88/barrios-skills)

- **Key Ideas**
  - **A curated library of agent skills and MCP servers for economists and accountants**, aimed at empirical accounting and finance research: WRDS panels, SEC filings, and fixed-effects regressions.
  - **A clean split between two kinds of extension:**
    - **Skills (`skills/`)** are *agent instructions*: markdown workflows the agent reads, with no credentials. You copy a folder into the agent's skills directory (the docs use Cursor's `~/.cursor/skills/`; the same `SKILL.md` format works in Claude Code), and the agent loads it when your request matches the description.
    - **MCP (`mcp/`)** provides *live data connections*: servers the agent calls as tools, which need `pip install`/`uvx`, an MCP config entry, and credentials.
  - **Econometrics skills**: `stata-regression` (publication-ready tables); `wrds` (agent-ready SQL patterns for Compustat, CRSP, TRACE, TAQ, ExecuComp, ISS, Capital IQ, and Form 4, including TRACE cleaning, FISD merges, NBBO construction, and effective spreads); and `pyfixest` (the Python counterpart to `reghdfe`/`fixest` for high-dimensional FE, cluster-robust SEs, and modern DiD via `did2s` and Sun–Abraham).
  - **`sec-edgar` enforces research hygiene**: CIK discipline, SEC User-Agent rules, and "sample inspection before claiming results." Use the EDGAR MCP for live lookups and WRDS for panel Compustat/CRSP merges.
  - **Writing skills**: `econ-write` drafts in a Cochrane/McCloskey/Shapiro style (triangular introductions, concrete magnitudes, identification-first structure). `econ-humanizer-plus` removes AI tells in econ prose. It deletes boilerplate phrases ("the remainder of this paper is organized as follows"), bans words ("delve," "landscape," "leverage" as a verb, "robust" outside statistics, "shed light on"), and varies sentence length (8–12 and 15–25 words). It also **explicitly permits em-dashes and parentheticals**, because over-sanitized prose is itself an AI tell.
  - **`econ-lit-search`** searches a local, curated corpus of about 51k economics papers (NBER working papers and JEL-coded journals) with full text, abstracts, snippets, and citation sorting. It is deliberately kept separate from OpenAlex: the user chooses, and the skill does not auto-combine them.
  - **Data MCPs**: a vendored `wrds-mcp` (`wrds_run_sql` read-only, `wrds_get_compustat`), `sec-edgar-mcp` (10-K/10-Q/8-K, XBRL, Forms 3/4/5), OpenEcon (FRED, World Bank, IMF, and more), plus FRED-only and Stata-MCP options.

- **Summary**

Barrios Skills is a practical, domain-specific extension pack for empirical accounting and finance research. Its main teaching point is the distinction between **skills**, which are portable markdown procedures that tell an agent *how* to do something and carry no credentials, and **MCP servers**, which are credentialed live connections that let an agent *reach* data. A researcher can install only the skills and keep full control over data access, or add MCPs for WRDS, EDGAR, and macro sources when live querying is worth the setup and the credential exposure.

The skills encode field conventions that general-purpose agents usually get wrong: WRDS table quirks and merge keys, CIK-based firm identification, TRACE cleaning, high-dimensional FE syntax, and the prose norms of top finance and accounting journals. Several of them build in verification habits, such as `sec-edgar`'s instruction to inspect the sample before claiming results, and the literature skill's refusal to silently mix sources.

- **Relevance to Economics Research**

For accounting and empirical finance researchers, this is one of the most directly usable toolkits in the wiki. It covers the full path from WRDS/EDGAR data pulls through `pyfixest` or Stata estimation to journal-style prose. It complements the [[summaries/claude-wrds-public|Claude WRDS Toolkit]] and [[summaries/claude-wrds-tools|WRDS tools]] and extends the [[summaries/edgar-filings|EDGAR]] workflow. The skills-vs-MCP framing is a good mental model to teach: skills are free and safe to share, while MCPs carry credentials and privacy considerations (see [[summaries/privacy-setup]]). The `econ-humanizer-plus` rule list is also a useful concrete reference for anyone building a writing-voice skill.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/mcp-protocol]]
  - [[concepts/wrds-data-access]]
  - [[concepts/skills-vs-agents]]
  - [[concepts/ai-writing]]
  - [[concepts/literature-review-ai]]
  - [[concepts/data-access]]

- **Related Summaries**
  - [[summaries/claude-wrds-public]] — Liu/Orłowski subagents + skills for WRDS
  - [[summaries/claude-wrds-tools]]
  - [[summaries/edgar-filings]]
  - [[summaries/mcp-setup]]
  - [[summaries/dickerson-ai-asset-pricing]]
  - [[summaries/skill-library]]
  - [[summaries/ai-research-feedback-skills]] — Bäckman's research-review skill collection
  - [[summaries/teaching-ai-your-voice]] — Blattman on preserving authorial style
