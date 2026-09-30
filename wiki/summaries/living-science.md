---
title: "Introducing Living Science"
tags: [summary, academic-research, reproducibility, automated-research]
sources:
  - "[[raw/Clippings/Introducing Living Science.md]]"
date_updated: 2026-09-30
date_published: 2026-09-29
---

- **Author/Source**: Chenhao Tan (University of Chicago), via X article; also posted on the Living Science blog
- **Original**: [https://x.com/ChenhaoTan/article/2104960869763285422](https://x.com/ChenhaoTan/article/2104960869763285422) · [livingscience.ai/blog/introducing-living-science](https://livingscience.ai/blog/introducing-living-science)

- **Key Ideas**
  - **Papers are snapshots, not endpoints.** Especially in empirical work, a paper offers one view of the world at one point in time; new data, models, and methods make it possible to ask whether the pattern persists and whether the effect size has changed.
  - **Living Science** ([livingscience.ai](https://livingscience.ai/)) is a public project to keep influential research "alive" by routinely revisiting its findings as new data arrive. It starts with **economics**, choosing studies whose data sources are regularly updated.
  - **The goal is not to grade the original paper.** The aim is not to judge whether it was correct when published but to create a venue for ongoing discussion of influential results.
  - **Agent pipeline:** SAI's replication agent first looks for a public replication package, reproduces the key findings, documents what matches and what doesn't, then finds relevant data sources and **extends the analysis to newer data**. Because datasets and setups may differ from the original, the exercise is "closer to writing a follow-up paper than strict replication."
  - **Human checks:** the team sanity-checks results, asks the original authors for feedback, and invites public comments to flag issues. Replication repositories are published on GitHub.
  - **Cadence:** at least one new paper per week; the community can nominate papers.
  - **Initial findings:**
    - *Minimum wages* (Cengiz et al. 2019, extended to 236 state-level increases through 2024): affected wages +4.6%; employment −1.1%, statistically indistinguishable from zero.
    - *Unemployment ins and outs* (Shimer 2012, extended through June 2026): slower job finding still explains **89%** of unemployment fluctuations excluding 2020 (vs. ~90% originally), but job losses accounted for 38% over 2010–2026 because of the pandemic.
    - *Regional evolutions* (Blanchard & Katz 1992, extended through 2025): migration now absorbs **24–28%** of a local job-loss shock in the first year after 2008, down from 38% in 1978–1990. Local shocks still scar, but fewer people move away.
  - **Why a shared public record?** (1) others can build on existing replications instead of starting over; (2) **common knowledge**: an update that stays on one researcher's laptop doesn't stop others from citing a stale result; (3) science is communal, and keeping results current needs people who catch errors and add analyses.

- **Summary**

Tan introduces Living Science as a response to a structural feature of empirical research: once a paper is published, its findings are frozen, even though the underlying data keep accumulating. AI agents have made it cheap enough to revisit influential papers that doing so can become routine rather than a one-off replication project. The project uses an AI replication agent to reproduce each paper's headline results (starting from public replication packages where they exist), record the discrepancies, and then extend the analysis forward in time. Tan is explicit that this is closer to a follow-up paper than a strict replication, since the agent may assemble different data and make different setup choices.

The three launch reports show the range of outcomes the project wants to make visible. The minimum-wage and unemployment-flows results largely hold up. The Blanchard–Katz regional-adjustment result changes materially, with migration playing a much smaller role after 2008. In some cases the data needed to revisit a question no longer exist. The case for a *public* record, rather than private re-analyses, rests on common knowledge: the field keeps citing old estimates unless updates are published somewhere shared, inspectable (GitHub repos), and open to comment from the original authors and the community.

- **Relevance to Economics Research**

Living Science puts into practice an idea several other sources in this wiki have floated. Goldsmith-Pinkham ([[summaries/research-in-time-of-ai]]) argued that AI's biggest upside for research quality may be cheaper replication and scrutiny. Cowen ([[summaries/research-paper-disappear]]) asked when the static paper would give way to something more dynamic. This project combines both: agent-driven replication plus continuous extension, published as a living record attached to canonical papers. For labor and macro economists, the three launch reports are substantive updates to widely cited results. The Blanchard–Katz update especially should interest anyone teaching or building on regional adjustment models.

For empirical researchers generally, it signals a coming norm. Influential papers with regularly updated public data (CPS, JOLTS, QCEW, BLS series, and by extension CRSP/Compustat-style panels in finance) are the easiest targets for automated extension, so authors should expect their results to be re-run on new data by others. That makes clear replication packages and well-specified methods sections more valuable. Kohler et al. ([[summaries/kohler-agentic-reproduction]]) found that underspecified methods are the main cause of failed agentic reproduction. Living Science's approach, with public repos, author outreach, and open comments, is also a useful model for the human-in-the-loop verification that agent-produced empirical work still needs.

- **Related Concepts**
  - [[concepts/reproducibility-transparency]]
  - [[concepts/automated-research]]
  - [[concepts/future-of-academic-publishing]]
  - [[concepts/research-quality]]
  - [[concepts/empirical-methods]]

- **Related Summaries**
  - [[summaries/kohler-agentic-reproduction]]
  - [[summaries/research-paper-disappear]]
  - [[summaries/research-in-time-of-ai]]
  - [[summaries/project-ape]]
  - [[summaries/cc-series-14-pnas-replication-1]]
  - [[summaries/integration-collaboration-substack]]
