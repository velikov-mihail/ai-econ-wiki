---
title: "Sign of the Future: GPT-5.5"
tags: [summary, ai-tools]
sources:
  - "[[raw/articles/Sign of the future GPT-5.5.md]]"
date_updated: 2026-04-25
date_published: 2026-04-23
---

- **Author/Source**: Ethan Mollick (Wharton), One Useful Thing (Substack)
- **Original**: [https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55)

- **Key Ideas**
  - Mollick's framing for thinking about AI progress: **models** (Opus 4.7, Gemini 3.1, GPT-5.5), **apps** (chatgpt.com, Claude Code, Codex), **harnesses** (the tools the model can use --- image generation, code execution, web search). All three are advancing simultaneously.
  - Concrete generation-over-generation demo: build a procedurally generated 3D simulation of a harbor town from 3000 BCE to 3000 AD. Only GPT-5.5 Pro actually modeled an *evolving* town rather than just replacing buildings. GPT-5.5 Pro completed the task in 20 minutes vs. 33 minutes for GPT-5.4 Pro.
  - **PhD-quality paper from four prompts.** Mollick gave Codex (powered by GPT-5.5) a decade-old folder of crowdfunding data (STATA, CSV, XLS, Word files), asked it to generate a hypothesis, test it sophisticatedly, write a literature review, and format the paper. Then fed GPT-5.5 Pro's comments back in. The output is what he'd be happy to see from a 2nd-year PhD project --- the literature is real, the statistics are real, the methodology is sophisticated, but the hypothesis is "not that interesting" and standard causation concerns remain.
  - **From one prompt to a 101-page playable RPG.** Codex generated an original tabletop RPG with rules, tables, simulated playtesting, and 101 illustrated pages of layout. The setting is "interesting and novel"; the rules appear to make sense.
  - **Image-gen-2 (the new OpenAI image model)** can render high-quality text in images, making it usable for slides, mockups, and example websites. Mollick demonstrates with a multi-style art gallery of his "Otter test" with readable labels under each piece.
  - **Jagged frontier persists.** Long-form fiction still has the characteristic AI failure modes: love of the uncanny, overly complex ideas that don't pay off, weird metaphors, identical-tone dialogue, and "the name Mara." Hypothesis generation produces sound statistics on uninteresting questions.
  - **Pattern over three years of newsletter writing:** every few months a new model arrives, something previously impossible becomes easy, and the size of the leap is growing each cycle. The jagged frontier hasn't disappeared --- it's just much further out.

- **Summary**

Mollick's GPT-5.5 review is less about the specific model than about the pattern it represents. He uses the post to reinforce his "models / apps / harnesses" frame for understanding why AI capabilities are accelerating: not just the models are getting smarter, the wrappers around them (Codex, Claude Code) and the tools they can call (image gen, code execution, sub-agents) are improving in parallel.

The most consequential demo for academics is the crowdfunding-data paper. Mollick had hundreds of anonymized files he'd never gotten around to analyzing. He asked Codex to sort them out, generate a hypothesis, test it, write a paper. Four prompts, no manual editing of the text. The literature review and statistics are real (a notable bar-clear since hallucinated citations were the standard failure mode through 2024--2025). His complaint is now at the level of "the hypothesis isn't interesting" and "I worry about causation despite the sophisticated identification" --- which is the level of complaint a senior advisor has about a 2nd-year PhD's draft. That's the real news.

The RPG demo is the same point in a different domain: agents can now produce attractive, structured, multi-format output (a 101-page illustrated PDF with rules, tables, and simulated playtests) from minimal prompting.

The fiction critique --- "weather and architecture are the same argument at different speeds" being cool once but exhausting across an entire book --- is Mollick's clearest articulation that creative-prose quality remains a bottleneck even as analytical-prose quality is essentially solved.

- **Relevance to Economics Research**

Direct. The crowdfunding-paper demo is the most concrete recent evidence that 2nd-year-PhD-quality empirical economics papers can now be produced with minimal human input from a folder of mixed-format data files --- which is the situation many faculty are sitting on (decade-old data they never wrote up). For Mihail and other empirical finance researchers, this is a *direct* pointer toward firing up Codex/Claude Code on dormant data folders. It also reinforces Hall ([[summaries/ai-10x-research]]) and Kustov-III ([[summaries/academics-wake-up-3]]) --- the bar for "publishable empirical paper" is rising because the floor of what an agent can produce has risen.

The "models / apps / harnesses" frame is also useful pedagogically for the master-class audience: it disentangles "GPT-5.5 is smarter" (model) from "Codex got better" (app) from "image gen now does real text" (harness/tool), all of which are independently advancing.

- **Related Concepts**
  - [[concepts/jagged-frontier]]
  - [[concepts/ai-tools-landscape]]
  - [[concepts/agentic-workflows]]
  - [[concepts/automated-research]]

- **Related Summaries**
  - [[summaries/shape-of-ai]]
  - [[summaries/guide-which-ai]]
  - [[summaries/ai-10x-research]]
  - [[summaries/academics-wake-up-3]]
  - [[summaries/agentic-everything]]
