---
title: "Academic Research Skills for Claude Code (ARS)"
tags: [summary, claude-code-skills, academic-pipeline, peer-review]
sources:
  - "[[raw/articles/Academic Research Skills for Claude Code.md]]"
date_updated: 2026-05-15
date_published: 2026-05-05
---

- **Author/Source**: Edward Cheng-I Wu (吳政宜), GitHub
- **Original**: [https://github.com/Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

- **Key Ideas**
  - **ARS** is a Claude Code plugin suite of ~25 modes across four skills covering the full pipeline from research question to peer-reviewed paper: Deep Research (13 agents, 7 modes), Academic Paper (12 agents, 10 modes), Academic Paper Reviewer (7 agents, 6 modes), and Academic Pipeline (10-stage orchestrator).
  - Built explicitly as **human-in-the-loop**, motivated by Lu et al. (2026, Nature) on autonomous AI Scientist failure modes — implementation bugs, hallucinated results, shortcut reliance, frame-lock, methodology fabrication, citation hallucination.
  - **Integrity gates at Stages 2.5 and 4.5** run a 7-mode blocking checklist for AI failure modes; cannot be skipped. Tier 0 Semantic Scholar API verification catches fabricated references before review.
  - **Anti-sycophancy mechanisms**: Devil's Advocate Concession Threshold Protocol (must score rebuttals 1–5 before conceding; concession only at ≥4); Socratic Mentor intent detection (exploratory vs. goal-oriented modes); dialogue health indicator self-checks every 5 turns.
  - **Style Calibration** learns voice from 3+ past papers; Writing Quality Check flags AI-tell patterns (25 high-frequency terms, em-dash overuse, throat-clearing openers, Rule of Three, uniform paragraph rhythm). Stated framing: better writing, not detection evasion.
  - Cost estimate ~$4–6 for a 15k-word paper through the full pipeline. Output: Markdown → DOCX (Pandoc) → LaTeX (APA 7.0 `apa7` class / IEEE / Chicago) → PDF (tectonic).
  - One-line plugin install: `/plugin marketplace add Imbad0202/academic-research-skills` then `/plugin install academic-research-skills`. Supports English and Traditional Chinese natively; intent-based mode activation works in any language.

- **Summary**

ARS is one of the most architecturally elaborate Claude Code skill bundles for academic writing currently public, drawing on three specific papers in its design: Lu et al. (2026, *Nature* 651:914–919) on the AI Scientist's failure modes, PaperOrchestra (Song et al., 2026, Google) for Semantic Scholar verification and anti-leakage, and Wang & Zhang (2026, IJETHE 23:11) on collaboration depth. The pipeline runs ten stages (Research → Plan → Write → Integrity 2.5 → Review → Re-review → Revise → Integrity 4.5 → Finalize → Process Summary) with mandatory user-confirmation checkpoints and an append-only "Material Passport" carrying provenance across stages.

The author treats peer review as a multi-agent panel: an Editor-in-Chief, three dynamic reviewers, and a Devil's Advocate score the manuscript on 0–100 rubrics mapped to standard decisions (≥80 Accept, 65–79 Minor, 50–64 Major, <50 Reject). A Calibration mode measures the reviewer's own FNR/FPR against a user-supplied gold set. The release notes are remarkable for their forensic honesty: v2.7 records a post-publication WebSearch audit of 68 references that found a **31% error rate that had survived three rounds of integrity checks**, which became the case for adding external verification by default. v3.7 adds plugin packaging, model routing (`opus` for full pipeline and revision-coach modes, `sonnet` elsewhere, no Haiku), and slash-command shortcuts (`/ars-plan`, `/ars-lit-review`, etc.).

- **Relevance to Economics Research**

ARS is one of the clearest worked examples of a research workflow that takes AI failure modes (especially citation hallucination, frame-lock, and sycophancy) seriously enough to engineer specific countermeasures into the toolchain. For economists, the directly useful pieces are: (1) the integrity-gate pattern (verify references with an API, not the LLM's memory) which generalizes to any empirical replication workflow; (2) the Devil's Advocate concession protocol, which is a concrete answer to the recurring complaint that LLM reviewers cave under pushback; (3) the journal taxonomy in `top_journals_by_field.md` (incorporating the AIS Senior Scholars' Basket of 11); and (4) the Style Calibration / Writing Quality Check pair as a template for keeping AI-assisted prose from drifting toward generic LLM cadence. The pipeline is heavily oriented toward IS/management venues but adaptable to economics with custom prompts.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/ai-peer-review]]
  - [[concepts/automated-research]]
  - [[concepts/citation-hallucination]]
  - [[concepts/human-in-the-loop]]

- **Related Summaries**
  - [[summaries/coarse-ink]]
  - [[summaries/haaland-reviewer]]
  - [[summaries/cc-series-44-four-criteria-referee]]
  - [[summaries/kohler-agentic-reproduction]]
  - [[summaries/ars-codex]]
  - [[summaries/katmer-code]]
