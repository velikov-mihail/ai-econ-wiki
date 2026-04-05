---
title: "Claude Code Part 11: Use This Prompt to Make a Deck"
tags: [summary, prompt-engineering-workflow, beamer, lecture-slides, multi-agent]
sources:
  - "[[raw/articles/Claude Code part 11 use this prompt to make a deck.md]]"
date_updated: 2026-04-05
date_published: 2026-01-30
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-part-11-use-this-prompt](https://causalinf.substack.com/p/claude-code-part-11-use-this-prompt)

- **Key Ideas**
  - A single, copy-pasteable prompt that generates a full Beamer lecture deck with original style, R scripts, embedded figures and tables, and narrative flow
  - The prompt instructs Claude Code to create an original Beamer style, restructure an existing deck with new rhetoric, embed and run R scripts, then compile and fix all overfull/underfull errors
  - Multi-agent review is built into the prompt: a second agent evaluates whether instructions were met, and a third agent checks only graphics for labeling, positioning, and numerical accuracy
  - Users should customize by specifying their language (Stata, Python), audience demographics, and any existing course materials
  - Claude Code will install R and LaTeX itself if needed

- **Summary**

This brief post provides a single prompt template designed to be pasted directly into Claude Code while inside a course folder. The prompt asks Claude Code to design an original Beamer style, restructure an existing deck with improved rhetoric and pedagogical flow, embed R scripts that generate figures and tables, compile the deck, eliminate all overfull/hbox/vbox errors, and then run two additional agent passes -- one for overall quality review and one specifically for graphics accuracy (TikZ labeling, ggplot positioning, coordinate placement). Cunningham encourages users to enrich the prompt with details about their students (year, major, background) and to specify alternative languages like Stata or Python.

The post is notable for its simplicity: the entire workflow is encoded in a single prompt. This contrasts with the detailed, iterative dictation approach described in Part 10, offering instead a "fire and forget" entry point for newcomers.

- **Relevance to Economics Research**

The prompt template is directly usable by any economist teaching a quantitative course. The multi-agent review pattern -- where separate agents check content quality and graphical accuracy -- is a lightweight verification protocol that addresses the hallucination risk in automated slide generation. The approach also demonstrates how prompt design can encode an entire multi-step workflow, which is relevant for researchers building reproducible pipelines.

- **Related Concepts**
  - [[concepts/prompt-engineering]]
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-agents]]

- **Related Summaries**
  - [[summaries/cc-series-10-lecture-decks]]
  - [[summaries/cc-series-12-empirical-research]]
