---
title: "Revise-and-Resubmit Workflows"
tags: [concept, academic-research, publishing]
sources:
  - "[[summaries/point-by-point.md]]"
  - "[[summaries/ars-claude-code.md]]"
  - "[[summaries/cc-series-44-four-criteria-referee.md]]"
date_updated: 2026-05-15
---

# Revise-and-Resubmit Workflows

The revise-and-resubmit (R&R) stage is the most structured part of academic publishing: a fixed set of referee concerns, each requiring a written response and (usually) a corresponding manuscript change. The structure is what makes R&R highly AI-assistable — clear inputs (referee reports), clear outputs (per-concern response + revised text), and a built-in completeness check.

## Context & Background

Standard R&R workflow has four sub-steps: (1) parse the referee letters into a flat list of concerns; (2) for each concern, draft a response and identify the corresponding manuscript change; (3) track which concerns have been addressed and which still lack a response; (4) assemble the response letter, typically in a tabular per-concern format with point references back to the manuscript.

Two distinct tooling patterns have emerged:

- **Single-purpose web apps** like [[summaries/point-by-point|Point by Point]] (Nagaraj) — per-concern workspaces, completeness tracking, LaTeX export of the final response letter. Bring-your-own API key.
- **Modes within larger pipelines** like [[summaries/ars-claude-code|ARS]]'s revision-coach mode — parses reviewer comments into a revision roadmap and an R&R Traceability Matrix that records the author's claim, the verified change, and a "Verified?" column for the re-review stage.

The R&R Traceability Matrix pattern is especially valuable because it lets a re-review agent (or human editor) independently check whether the claimed revision is actually in the revised manuscript.

## Practical Implications

- **Decompose the referee letters first.** Each concern gets its own workspace. Resist the temptation to draft a "global response" before per-concern work is done.
- **Track completeness explicitly.** A response letter is done when every concern has both a written response and a manuscript change (or a justified refusal). Tools that show this completeness state at a glance prevent the standard "I thought I addressed that" failure mode.
- **Build a traceability matrix.** For each concern: what did the referee ask, what did the author claim to do, what actually changed in the revised manuscript? A re-review pass should be able to independently verify the third column.
- **Don't lose private comments.** Many referee letters have a separate "comments to the editor" block that is not for the authors. Tools should keep these compartmentalized.
- **R&R is multi-author.** Point by Point's secret-URL collaboration model is a useful starting point; the per-concern decomposition makes co-authorship cleaner than a shared document.

## Key Sources

- [[summaries/point-by-point|Point by Point]] — Guided R&R response letter workflow with completeness tracking and LaTeX export
- [[summaries/ars-claude-code|ARS]] — Revision-coach mode + R&R Traceability Matrix (Schema 11)
- [[summaries/cc-series-44-four-criteria-referee|Four Criteria for Using Agents (Referee Reports)]] — Cunningham's pipeline for incoming referee reports

## Related Concepts

- [[concepts/ai-peer-review|AI-Assisted Peer Review]]
- [[concepts/ai-workflows|AI Workflows]]
- [[concepts/future-of-academic-publishing|Future of Academic Publishing]]
