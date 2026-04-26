---
title: "AI, Ideas, and the Future of Research (Kansoy Deck)"
tags: [summary, institutional-societal, academic-research, ai-agents, agentic-workflows, automated-research]
sources:
  - "[[raw/articles/AI, Ideas, the Future of Research.md]]"
date_updated: 2026-04-26
date_published: 2026-04-17
---

- **Author/Source**: Fatih Kansoy (University of Oxford), six-section lecture deck released publicly on 2026-04-17
- **Slides**: [https://fatih.ai/airesearch/](https://fatih.ai/airesearch/)
- **Announcement thread**: [https://x.com/kansoy/status/2045073389274939690](https://x.com/kansoy/status/2045073389274939690) (deck built with Claude Code)

## Key Ideas

- **Judgment is the new scarce input.** Historical scarcities — physical access to knowledge, language, institutional gatekeeping — collapsed sequentially (1450 print, 19th-century libraries, 1990s open web). AI now drops the cost of *answering* hard questions, but in doing so it makes *taste* — knowing which questions are worth asking and which designs are credible — the binding constraint on research.
- **A capability ladder, not a binary.** ANI (today, narrow tasks) → AGI (broad competence, hypothetical) → ASI (speculative). Within current ANI, Kansoy distinguishes **AI-assisted** work (researcher leads, AI supports) from **AI-generated** work (AIGPs — AI executes substantial labor; human directs and critiques). Journals will need different disclosure rules for the two regimes.
- **Chatbot → agent is a categorical shift.** Where chatbots offer one-shot prompts with no memory or tools, agents have persistent context, tool access (files, code, APIs), multi-step execution with checkpoints, and verification loops.
- **The "LLM + SKILL.md = Agent" formula.** A `SKILL.md` file is plain text — not software — defining a Trigger, ordered Modules, References to read first, hard Constraints, and Checkpoints where the agent pauses for human verification. The same LLM becomes a Methodology Reviewer, Devil's Advocate, Socratic Mentor, or Code Writer depending on which skill it loads. Multiple agents coordinated by an orchestrator program become a research **pipeline**.
- **An eight-stage research pipeline.** Ideation → Design & Feasibility → Data Assembly → Core Analysis → Robustness & Extensions → Writing → Submission & Review → Publication. AI executes at each stage; the human judges at every handoff (which question, which strategy, which interpretation, which claim).
- **The AI Scientist (Lu et al., Nature 2026).** End-to-end agentic system that cycles through idea search, code-edit experiments, paper drafting, and self-review. Three of its papers entered ICLR 2025 blind workshop review; one scored 6.33/10 (top 45% of 43 submissions) — withdrawn per protocol — demonstrating that the loop already produces workshop-clearing output on a negative-result paper.
- **The research crisis (Park, Leahey, Funk, *Nature* 2023).** Across 45M papers and 3.9M patents, the disruption index — whether new work breaks from prior consensus — has fallen 92–100%. More science, less novelty. AI accelerates execution; it does not decide what is worth doing. Novel questions remain scarce.

## Summary

Kansoy's deck is a self-contained six-section lecture aimed at academics figuring out how the agentic shift reshapes research practice. The arc moves from macro-economic foundations (Hobbes → Solow → Romer → Jones, all rooted in the claim that ideas drive growth) through the historical collapse of knowledge gates, to a concrete operational picture of how AI agents are now organized into research pipelines, ending with a pointed argument about what depreciates and what appreciates in this regime.

The middle of the deck is the most operationally useful. Kansoy lays out the chatbot-vs-agent distinction as a four-row table (memory, tools, execution, verification), then introduces `SKILL.md` files as the protocol layer that turns a general-purpose LLM into a specialist. He gives a concrete example — an Academic Paper Review skill with four modules (referee report simulation, British-English audit, LLM-cliché detection, style/repetition audit), reference files to consult, and checkpoints between modules. The pedagogical move is to show that "agentification" is not a software project but a documentation discipline: write the protocol clearly enough and the LLM follows it.

Section 5 walks through eight pipeline stages with two real research examples: a 14-language, 132-central-bank corpus of speeches and minutes (37,790 + 3,602 documents) used to estimate the gap between climate talk in public versus private deliberations, and a Bank of England Twitter archive (9,810 tweets, 3.1M public responses, 2011–2022) supporting multiple papers on attention, format, and timing. The point is that these projects were not previously *impossible* — they were too expensive in human-labor terms to start.

Section 6 is the demonstration: a research question on whether wealth composition (housing-illiquid vs. liquid) shapes life, work, and voting, run end-to-end three different ways. Traditional execution: 6–18 months. Chatbot-assisted: 2–4 months. Agentic with a 361-line master prompt across seven stages: 1–3 weeks. The agentic run produced 28.5M rows cleaned, a 26,936 analysis sample, 21 Python scripts, 7 figures, 6 tables, and a 5,297-word manuscript across six free public datasets (PSID, CPS, CEX, ANES, ACS, FRED). The substantive finding was strong descriptive patterns but a weak first stage that fails to justify the causal claim. Kansoy's lesson is unflinching: *good execution cannot rescue weak design*. The agent built the telescope; only the researcher could decide whether the results deserved belief.

The closer drives home the argument with the Park-Leahey-Funk disruption-decline result: science is producing more while breaking less. Combined with the AlphaFold reference (a 50-year stall broken when models, data, and compute aligned), Kansoy argues that abundant execution will widen — not close — the gap between researchers who have taste and those who do not.

## Relevance to Economics Research

This is one of the most operationally substantive deck-format treatments of agentic research currently in the wiki. Three things stand out for economists:

1. **A clean conceptual stack for thinking about agents.** The "LLM + SKILL.md = Agent; Agents + Pipeline = Research" formula is concise enough to use in graduate-level methods discussions, and the four-row chatbot-vs-agent table is the cleanest such comparison in the corpus (cf. [[summaries/agentic-everything]] which makes a similar point informally).
2. **A worked example with honest results.** Unlike many enthusiast-mode demos, the wealth-composition example shows the agent producing a polished but causally weak paper, and Kansoy uses that explicitly to draw the line between execution and judgment. Pair this with [[summaries/zeropaper-gallery]] (Lopez-Lira's 22 autonomous papers) as evidence on what current pipelines do and don't deliver.
3. **The "judgment as appreciating asset" frame.** This connects to [[summaries/what-will-be-scarce]] (Imas), [[summaries/research-paper-disappear]] (Cowen), and [[summaries/ai-10x-research]] (Hall). Kansoy's distinctive contribution is grounding it in the empirical disruption-decline literature, giving the claim sharper teeth than usual.

Recommended for graduate methods seminars and faculty discussions about how to allocate PhD training time between substantive expertise and toolchain proficiency (cf. [[summaries/andrews-ai-research]] for a complementary case-based framework).

## Related Concepts

- [[concepts/agentic-workflows]]
- [[concepts/automated-research]]
- [[concepts/ai-skills]]
- [[concepts/skills-vs-agents]]
- [[concepts/domain-expertise-vs-ai-skills]]
- [[concepts/research-quality]]

## Related Summaries

- [[summaries/agentic-everything]] — Svoronos: parallel "agent = LLM + tools + loop + goal" framing
- [[summaries/ai-10x-research]] — Hall (Stanford): 10x → 100x research acceleration framing
- [[summaries/zeropaper-gallery]] — Lopez-Lira: 22 papers from a fully autonomous pipeline
- [[summaries/automated-research-finance]] — Lopez-Lira: the announcement of the ZeroPaper pipeline
- [[summaries/kohler-agentic-reproduction]] — Kohler et al. (ETH): agentic reproduction of social-science results
- [[summaries/spina-paper]] — Spina: skills-based academic workflow with Claude Code
- [[summaries/velikov-smeal-cop]] — Velikov: parallel deck on chatbots → agents for business/economic research
- [[summaries/skill-library]] — Blattman on building a personal skill library
- [[summaries/andrews-ai-research]] — Andrews (MIT): allocating PhD training under AI uncertainty
- [[summaries/academics-wake-up-3]] — Kustov: human slop predates AI; non-adoption is malpractice
