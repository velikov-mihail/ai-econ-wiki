---
title: "Claude Code Part 12: How I Use Claude Code for Empirical Research"
tags: [summary, academic-research, referee-2, cross-language-replication, socratic-method, verification, mixtape-tools]
sources:
  - "[[raw/articles/Claude Code Part 12 How I Use Claude Code for Empirical Research.md]]"
date_updated: 2026-04-05
date_published: 2026-02-02
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-part-12-how-i-use-claude](https://causalinf.substack.com/p/claude-code-part-12-how-i-use-claude)

- **Key Ideas**
  - Treat Claude Code as a thinking partner, not a code monkey -- the hard part of empirical research is deciding what to do, not writing code
  - Claude has amnesia between sessions; build external memory via CLAUDE.md, README files, and session logs so context persists
  - Use Socratic questioning ("Guess what I'm about to ask you") to maintain alignment and catch misunderstandings before they become wrong turns
  - Verification through visualization: never trust numbers alone; request figures constantly because errors are visible in pictures but invisible in tables
  - The Referee 2 protocol: open a fresh Claude Code terminal, paste adversarial reviewer instructions, and run a five-audit review that produces a formal referee report -- Referee 2 never modifies author code
  - Cross-language replication (R, Stata, Python) exploits the assumption that hallucination errors are orthogonal across languages; matching results to 6+ decimal places builds confidence
  - The MixtapeTools repo collects workflow philosophy, CLAUDE.md templates, Referee 2 protocol, and rhetoric-of-decks materials

- **Summary**

Cunningham introduces his MixtapeTools repository and explains the philosophy behind his Claude Code workflow for empirical research. The core idea is that Claude Code should be a thinking partner rather than an order-taker. He structures this around several principles: building persistent external memory through markdown files to combat Claude's session amnesia; using Socratic dialogue to keep Claude aligned with the researcher's intent; and demanding constant visualization to catch errors that numbers alone would hide.

The centerpiece is the Referee 2 protocol -- a formal adversarial review process where a separate Claude Code instance (with no memory of the original session) audits the project across five dimensions, writes a referee report with Major and Minor Concerns, and the researcher responds with revisions. The critical rule is that Referee 2 never touches author code; it creates independent replication scripts. Cross-language replication (running the same analysis in R, Stata, and Python) provides a further check, based on the insight that coding bugs across different languages are unlikely to be correlated.

Cunningham emphasizes that research is not product development: "almost right" results are unacceptable because they always signal a mistake somewhere. The post also introduces the "rhetoric of decks" philosophy, where slides follow MB/MC equivalence and titles are assertions rather than labels.

- **Relevance to Economics Research**

This post is a direct workflow guide for applied economists. The Referee 2 protocol addresses a fundamental problem in computational research -- that self-review is unreliable -- by mimicking the journal review process. Cross-language replication is particularly relevant for economists who routinely work across Stata, R, and Python. The external-memory pattern solves the practical challenge of maintaining continuity across long research projects with AI assistants.

- **Related Concepts**
  - [[concepts/ai-agent-workflows]]
  - [[concepts/verification-validation]]
  - [[concepts/prompt-engineering]]
  - [[concepts/multi-agent-patterns]]

- **Related Summaries**
  - [[summaries/cc-series-10-lecture-decks]]
  - [[summaries/cc-series-13-skills-split-pdf]]
  - [[summaries/cc-series-14-pnas-replication-1]]
