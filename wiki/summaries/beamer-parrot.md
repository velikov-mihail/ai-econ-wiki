---
title: "Beyond the Stochastic Beamer Parrot (Bäckman)"
tags: [summary, claude-code-skills, presentations, visualization, explorable-explanations]
sources:
  - "[[raw/articles/Beyond the Stochastic Beamer Parrot.md]]"
date_updated: 2026-09-30
date_published: 2026-09-29
---

- **Author/Source**: Claes Bäckman (Aarhus University), via Substack
- **Original**: [https://claesbackman.substack.com/p/beyond-the-stochastic-beamer-parrot](https://claesbackman.substack.com/p/beyond-the-stochastic-beamer-parrot) · skill: [`Skills/explorable-deck` in claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)

- **Key Ideas**
  - **The "stochastic Beamer parrot."** Ask an agent to make conference slides from your paper and you get a competent deck that looks like every other academic deck online, because that is what it learned from. It is an *old thing done faster*, not better. Bäckman's [AI-made Beamer example](http://claesbackman.com/assets/BDK_Seminar.pdf) for his housing-returns paper is decent after polishing out the "Claudisms" (e.g., "A control matters only if it predicts gains and covaries with income. Location does both."). A style file helps a little.
  - **Agents solved the mechanical pain of slides.** With access to the paper and the code, an agentic tool can build a paper-consistent deck and keep running "until the damn presentation compiles."
  - **Use AI to do *new* things, not just old things faster.** Bäckman adapted Nityesh Agarwal's `/explorable-explanation` Claude skill into an **`/explorable-deck`** skill. The original is built on Nicky Case's "explorable explanations," with ideas from Bret Victor and Steven Strogatz, and generates interactive websites. The adaptation produces **interactive slide decks** with a clear narrative, interactive elements that carry the message, and a clean visual language.
  - **Examples**: an [explorable deck](https://claesbackman.com/Slides_HousingReturns/#/title-slide) and an [explorable explanation](https://claesbackman.com/Explorable_HousingReturns/index.html) of the housing-returns paper, and an unedited [deck for his LLM financial-advice paper](https://claesbackman.com/assets/03_ExplorableDeck/index.html) for comparison. Each is backed by an editable **Quarto-Markdown** source. Claude writes the narrative, redraws the graphs (similar to the paper's but not identical), and builds the interactivity.
  - **"AI can crystallize expertise."** A skill packages years of thinking by expert explainers, so non-experts in explorable design can still benefit from it.
  - **You still have to know your paper.** (1) The deck is only as good as the paper underneath, which is a *higher* demand for expertise. Claude will always find *some* story, and it may not be the right one, though that can help you test whether your paper has a coherent narrative at all. (2) Building slides used to be how you learned your own talk. Once AI removes that step, **practice** has to replace it.

- **Summary**

Bäckman argues that the default use of AI for academic presentations, "make slides from my paper," produces a stochastic Beamer parrot: reasonable, compilable, generic decks that reproduce the median academic presentation. That is useful, but it wastes the opportunity. His alternative is an `/explorable-deck` skill, adapted with Claude from Nityesh Agarwal's explorable-explanation skill. It borrows the craft of people who explain ideas for a living (Nicky Case, Bret Victor, Steven Strogatz) to generate interactive, narrative-driven Quarto slide decks and companion websites from a paper.

The post keeps human responsibility in view. The paper's quality and narrative remain the foundation, and the researcher has to judge whether the story Claude builds is the right one. Because AI now removes the slide-building work through which presenters used to internalize their talk, Bäckman thinks rehearsal matters more than before. "An interactive deck also raises the bar for practice, so you can't quite take the day off yet."

- **Relevance to Economics Research**

Most AI-for-slides material in the wiki (e.g., [[summaries/cc-series-7-beautiful-decks|Cunningham's beautiful decks]], [[summaries/cc-series-11-deck-prompt|the one-prompt deck]]) aims to produce better *Beamer* faster. Bäckman makes the complementary argument that AI should change the *form* of research communication itself, with interactive explainers that let seminar audiences, students, and policymakers play with a model or a result. It is a concrete, installable instance of skills as "crystallized expertise," and it echoes [[summaries/research-paper-disappear|Cowen's question about the future of the static paper]]. The warning about practice fits the wider theme that AI removes tasks that used to build expertise as a side effect.

- **Related Concepts**
  - [[concepts/visualization]]
  - [[concepts/claude-code-skills]]
  - [[concepts/ai-skills]]
  - [[concepts/future-of-academic-publishing]]
  - [[concepts/domain-expertise-vs-ai-skills]]

- **Related Summaries**
  - [[summaries/cc-series-7-beautiful-decks]]
  - [[summaries/cc-series-10-lecture-decks]]
  - [[summaries/cc-series-11-deck-prompt]]
  - [[summaries/ai-research-feedback-skills]] — the repo that hosts `explorable-deck`
  - [[summaries/feedback-machines]]
  - [[summaries/research-paper-disappear]]
  - [[summaries/agentic-bootcamp-2-aslim-beam]] — `/academic-beamer-deck` lecture builder
