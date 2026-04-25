---
title: "Claude Code 44: My Four Criteria for Using Agents, with an Application to Referee Reports"
tags: [summary, academic-research]
sources:
  - "[[raw/articles/Claude Code  My four criteria for using Agents, with an application to referee reports.md]]"
date_updated: 2026-04-25
date_published: 2026-04-23
---

- **Author/Source**: Scott Cunningham (Baylor), Causal Inference (Substack), Part 44 of the Claude Code series
- **Original**: [https://causalinf.substack.com/p/claude-code-44-my-four-criteria-for](https://causalinf.substack.com/p/claude-code-44-my-four-criteria-for)

- **Key Ideas**
  - **Four-criteria test for delegating a task to an AI agent.** All four must hold:
    1. **High value** --- the work or output matters (referee reports are the backbone of peer review).
    2. **High time use** --- it takes a lot of *human* hours, so the time saving is real.
    3. **Hard if not impossible to do well** --- even with infinite time the human probably can't ace it.
    4. **Easy to do badly, mediocre, or wrong** --- the failure mode is common (being triggered by the topic, missing the author a fair shake, lacking the relevant skills).
  - The post applies the test to refereeing and concludes referee reports score on all four. Cunningham doesn't have the agent *write* the report; he has the agent *prepare him to write the report*.
  - **Pipeline:** `/split-pdf` → markdown summaries with structured extraction → `/beautiful_deck` (Beamer) → `/referee2` (critique the agent's interpretation, not the manuscript) → `/blindspot` (look around the edges of the main results) → `/tikz` (image label sanity-check via Bézier curves) → final pass with `/referee2` + `/beautiful_deck` again.
  - **PDFs are not text** to LLMs --- they're "hieroglyphics or even drawings." `/split-pdf` (in his MixtapeTools repo) chunks the PDF into ~4-page splits and writes per-split markdown, then a master markdown with research question, identification, target parameter, and an assessment of how convincing the evidence is.
  - The deck is **for him** --- audience-aware rhetoric. He asks for narrative (people, places, advisors, coauthors) because that's how he ingests technical material best.
  - When the deck reaches an empirical claim, he asks for **simulations matching the paper's panel structure / estimator** rather than copying the authors' figures. That double-checks whether the chosen estimator is even valid for the design (e.g., long-panel minimum-wage paper using Callaway--Sant'Anna where a federal MW increase removes the never-treated control --- the simulation will surface that the estimator can't be computed).
  - `/referee2` reviews the *agent's interpretation* (deck + summaries), not the paper. `/blindspot` reviews everything (deck, summaries, and the `/referee2` output), creating a "donut hole" around the main results to surface things easy to miss like sample-size mismatches in tables.
  - `/tikz` works ~50% of the time on label-overlap problems; it uses Bézier-curve coordinate math, not vision, so it can rule out crossings deterministically when the figure isn't too dense.
  - **The bottleneck in science is no longer production --- it is verification.** The whole pipeline is an attempt to push as much of the verification work onto the agent as possible *before* he reads the manuscript himself.

- **Summary**

Cunningham proposes a clean four-condition test for when to use an AI agent on a research task. The test isn't about whether the agent *can* do the task; it's about whether delegating it makes sense given the task's value, the human time cost, the difficulty of doing it well, and the ease of doing it badly. Refereeing scores on all four: it's high-stakes, time-consuming, genuinely hard, and trivially easy to mess up.

Most of the post is the actual workflow he uses, which is notable for what it *doesn't* do: the agent never writes the referee report and never replaces reading the paper. The agent's job is to build him a mental map of the paper before he reads it, in the form of a Beamer deck. Five custom skills (`/split-pdf`, `/beautiful_deck`, `/referee2`, `/blindspot`, `/tikz`) chain together with multiple critique passes, including a deliberately fresh `/referee2` invocation at the CLI to keep its critique independent of the agent that produced the artifacts under review.

The most reusable conceptual moves are: (1) PDFs need preprocessing into markdown before LLM analysis, ideally chunked; (2) decks-to-myself are a different rhetorical artifact than decks-for-others, and that affects what the agent should produce; (3) simulating the authors' design from scratch surfaces estimator-validity problems that you might miss reading the paper alone; (4) "donut-hole" review (ignore the main result, look around it) catches errors the paper itself directs attention away from; (5) Bézier-curve geometric checks for label collisions outperform vision-based checks for tikz figures.

- **Relevance to Economics Research**

Highly relevant. Refereeing is one of the largest unpriced labor inputs in economics, and Cunningham is the first source in this wiki to lay out a complete agent-assisted workflow that respects the editor's expectation of careful, original review. The four-criteria framework is also generalizable: it offers Mihail and other PIs a clean test for whether to invest in agentifying any given task, and it pairs well with Andrews's [[summaries/andrews-ai-research|case-based framework]] for choosing what to invest in. The verification-vs-production framing connects directly to refine.ink (Calvó López & Golub) and Hall's argument that the bar for what gets *published* should rise as production gets cheaper.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/claude-code-skills]]
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-peer-review]]
  - [[concepts/ai-research-tools]]

- **Related Summaries**
  - [[summaries/cc-series-13-skills-split-pdf]]
  - [[summaries/cc-series-12-empirical-research]]
  - [[summaries/cc-series-29-finding-facts]]
  - [[summaries/andrews-ai-research]]
  - [[summaries/ai-10x-research]]
