---
title: "Automated Research"
tags: [concept, automation, research]
sources:
  - "[[summaries/automated-research-finance.md]]"
  - "[[summaries/zeropaper-gallery.md]]"
  - "[[summaries/project-ape.md]]"
  - "[[summaries/thread-alexolegimas.md]]"
  - "[[summaries/thread-arindube.md]]"
  - "[[summaries/scientist-one.md]]"
date_updated: 2026-08-23
---

# Automated Research

Automated research refers to the use of AI agents and pipelines to partially or fully automate stages of the research process — from data collection and cleaning to analysis and report generation.

## Context & Background

The dream of automated research ranges from modest automation of individual tasks to ambitious end-to-end systems that generate complete research papers. Current capabilities sit somewhere in between, with AI handling individual pipeline stages well but requiring human oversight for the research process as a whole.

Levels of research automation:

- **Task automation**: Individual steps (data cleaning, table formatting) run by AI
- **Pipeline automation**: Sequences of connected tasks (collect → clean → analyze → visualize)
- **Research assistant**: AI handles multiple aspects with human direction
- **Autonomous research**: AI designs and executes studies independently (experimental, high-risk)

## Key Perspectives

Projects like automated research in finance demonstrate how AI can execute well-defined research protocols. However, critics note that the most valuable part of research — asking the right question — remains fundamentally human.

**The integrity gap.** ScientistOne ([[summaries/scientist-one|Google Cloud AI Research]]) supplies the sharpest evidence on where autonomous research systems currently stand. On frontier algorithm-discovery benchmarks, *every* system tested — five of them — already matches or exceeds human expert baselines, and they converge to similar solution quality. What has not converged is whether the resulting papers can be believed. Their **CoE Audit** checks a finished paper against its artifacts on four dimensions — score verification (does the reported number reproduce), specification violation, reference verification, and method-code alignment — and finds that **every baseline system exhibits at least one systematic integrity failure**: hallucinated reference rates up to 21%, score verification passing in as few as 42% of papers, method-code alignment between 20% and 80%.

The design lesson they draw is that evidence chains must be maintained *throughout* the pipeline rather than retrofitted at write-up time — their own system pairs a Claim Verifier with the paper writer and reports 0/337 hallucinated references and 12/12 score verification. The four audit checks translate almost directly to economics: does the coefficient reproduce, does the stated specification match the code that ran, do the citations exist, was the sample definition respected.

## Practical Implications

- **Audit the write-up, not just the result**: reported numbers, cited references, and the match between described method and actual code each fail independently
- **Automate the repetitive**: Focus automation on tasks you do repeatedly across projects
- **Keep humans on strategy**: Automated execution works; automated research design is still risky
- **Build incrementally**: Automate one step at a time, verify each works before connecting them
- **Document the pipeline**: Automated workflows must be reproducible and transparent

## Related Concepts

- [[concepts/agentic-ai|Agentic Ai]]
- [[concepts/ai-agents|Ai Agents]]
- [[concepts/ai-workflows|Ai Workflows]]
- [[concepts/research-quality|Research Quality]]
