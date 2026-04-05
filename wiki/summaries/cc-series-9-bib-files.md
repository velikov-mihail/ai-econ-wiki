---
title: "Claude Code Series (Part 9): Creating .bib Files and Automating Article Retrieval"
tags: [summary, claude-code-skills, literature-review, bibtex, automation, beamer]
sources:
  - "[[raw/articles/Claude Code Series (part 9) creating .bib files and automating article retrieval.md]]"
date_updated: 2026-04-05
date_published: 2026-01-24
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-series-part-9-creating](https://causalinf.substack.com/p/claude-code-series-part-9-creating)

- **Key Ideas**
  - Claude Code can automate the full literature-review pipeline: generate a .bib file of seminal papers on a topic, retrieve the PDFs from the web, organize them locally, create a LaTeX narrative document citing them, and produce a Beamer deck storyboarding the literature.
  - The entire pipeline (25 papers on economics of abortion access regulation) took about 50 minutes, including iterative deck refinement.
  - The workflow reflects how Cunningham processes research: piecing together the narrative of a literature is the cognitive work; Claude Code handles the mechanical retrieval, formatting, and visualization.
  - Deck iteration is part of the process -- repeatedly tinkering with slides until they communicate the story effectively is how the researcher internalizes the literature.

- **Summary**

Cunningham demonstrates a four-step literature-review workflow using Claude Code on his HB2 abortion project. First, he asked Claude to create a .bib file containing the top 25 seminal economics papers on regulating abortion access (demand-side and supply-side), covering a range of outcomes. Second, Claude went online, retrieved the PDFs, and placed them in a local folder. Third, Claude produced a LaTeX document citing and organizing the 25 papers into a coherent narrative. Fourth, Claude built a Beamer deck storyboarding the literature visually.

The session took about 50 minutes, with a significant portion spent iterating on the deck -- tinkering with layout, narrative flow, and aesthetics until Cunningham was satisfied. He frames this as integral to his workflow: the deck is not a final product but a tool for processing and internalizing the literature. The bibliography is not exhaustive (the task was narrowly scoped to high-citation economics papers on access regulation), but it provides a working foundation and a .bib file ready for use in the manuscript.

- **Relevance to Economics Research**

Addresses one of the most common complaints about ChatGPT -- its unreliability for literature reviews -- by showing how Claude Code's filesystem access and web retrieval change the equation. The ability to produce a .bib file, retrieve actual PDFs, and generate both a narrative LaTeX document and a visual deck in under an hour represents a major productivity gain for the literature-review stage of any empirical project. The hallucination risk remains (citations should be verified), but the mechanical labor of assembling bibliographies and organizing papers is largely automated.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/literature-review-ai]]
  - [[concepts/claude-code-skills]]
  - [[concepts/visualization]]
  - [[concepts/ai-research-tools]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/cc-series-7-beautiful-decks]]
  - [[summaries/cc-series-10-lecture-decks]]
  - [[summaries/cc-series-6-video-explainer]]
  - [[summaries/cc-changed-how-i-work-4]]
