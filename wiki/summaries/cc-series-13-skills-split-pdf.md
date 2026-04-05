---
title: "Claude Code Part 13: Skills and the Split-PDF Workflow"
tags: [summary, claude-code-skills, pdf-processing, skills-vs-personas, hallucination-mitigation, context-window]
sources:
  - "[[raw/articles/Claude Code Part 13 Skills and the Split-PDF Workflow.md]]"
date_updated: 2026-04-05
date_published: 2026-02-03
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-part-13-skills-and-the](https://causalinf.substack.com/p/claude-code-part-13-skills-and-the)

- **Key Ideas**
  - A skill is a recipe: a slash command (e.g., /split-pdf) that triggers a pre-written, multi-step workflow stored in a SKILL.md file
  - Skills vs. personas: skills run within the current session for task automation; personas (like Referee 2) require a fresh session for adversarial independence
  - The sweet spot for skills is workflows that are multi-step, repeatable, and fragile (order-dependent)
  - The /split-pdf skill solves two problems: (1) session crashes from "Prompt too long" errors when reading large PDFs, and (2) the shallow-read problem where attention degrades over long documents
  - The skill splits PDFs into 3-4 page chunks using PyPDF2, reads them in batches of 3 splits (~12 pages), and performs targeted extraction across 8 dimensions (research question, audience, method, data, statistical methods, findings, contributions, replication feasibility)
  - Chunked reading reduces correlated hallucination errors because each batch is a fresh engagement with manageable text
  - Session crash destroys all context not written to markdown progress logs -- reinforcing the need for aggressive external memory

- **Summary**

Cunningham introduces the concept of Claude Code skills -- reusable slash commands backed by detailed instruction files -- and distinguishes them from personas like Referee 2. Skills automate multi-step tasks within the current session, while personas require separate sessions to maintain adversarial independence. The key criterion for creating a skill: you find yourself explaining the same complex, order-dependent workflow repeatedly.

The main contribution is the /split-pdf skill, which addresses two practical problems with reading academic papers in Claude Code. First, large PDFs are token-expensive and can crash the session with a "Prompt too long" error, destroying all unsaved context. Second, even when PDFs fit, Claude's attention degrades over long documents, producing confident but subtly wrong summaries (the shallow-read problem). The skill splits a PDF into 3-4 page chunks, reads them in small batches, and performs structured extraction across eight research-relevant dimensions. Cunningham argues that chunked reading reduces hallucination by making errors across batches less correlated. He demonstrates the skill on Gentzkow, Shapiro, and Sinkinson (AER 2014), producing a 320-line structured notes file.

- **Relevance to Economics Research**

The /split-pdf skill directly addresses the economist's need to extract precise details from dense empirical papers -- data sources, variable definitions, sample restrictions, coefficient estimates, and replication feasibility. The structured 8-dimension extraction template is tailored to how applied researchers actually consume papers. The skill also demonstrates how to build reusable tooling around Claude Code, lowering the per-paper cost of literature review and replication assessment.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-limitations]]
  - [[concepts/prompt-engineering]]

- **Related Summaries**
  - [[summaries/cc-series-12-empirical-research]]
  - [[summaries/cc-series-14-pnas-replication-1]]
