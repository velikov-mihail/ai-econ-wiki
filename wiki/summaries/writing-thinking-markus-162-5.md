---
title: "Writing & Thinking: Claude Code for Economists (Markus Academy 162-5)"
tags: [summary, academic-research]
sources:
  - "[[raw/articles/Writing & Thinking Claude Code for Economists with Paul Goldsmith-Pinkham  Markus Academy  162-5.md]]"
date_updated: 2026-04-25
date_published: 2026-04-12
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM), Markus Academy Ep. 162-5 (5th of 7 in mini-series)
- **Original**: [https://www.youtube.com/watch?v=BxfSiB3Moyo](https://www.youtube.com/watch?v=BxfSiB3Moyo)
- **Companion notes**: [https://paulgp.substack.com/p/writing-and-thinking-with-ai-assistance](https://paulgp.substack.com/p/writing-and-thinking-with-ai-assistance)

- **Key Ideas**
  - Three demonstrations: (1) build a personal style guide as a Claude skill from your own papers + blog posts; (2) use Jukka Sihvonen's `strategic-revision` skill to convert referee reports into a dependency-mapped revision plan; (3) use Claude as an editor that **comments without editing** to preserve voice.
  - **Style-guide skill workflow:** point Claude Cowork at a folder of your papers and blog posts, ask it to write a `.claude/skills/yourname-voice/SKILL.md` markdown file capturing tone, sentence structure, and "verbal habits." The output is a caricature-of-you, useful but biased toward sycophancy --- "even the world's worst researcher would get a relatively positive take." Push the model hard if you want it to flag your bad habits.
  - The skill is "just text" --- a markdown file dumped into the context. So the same skill works in chat (paste it inline), in Cowork (auto-loaded from `.claude/skills/`), and in Claude Code on the command line.
  - Demonstrates the skill on a "please explain difference-in-differences to a PhD audience" prompt: with the skill, the output sets up the practical problem, does a 2x2 example before regression --- recognizably Goldsmith-Pinkham's style. Without the skill, default-AI voice that gets to the method too fast.
  - **Strategic Revision skill** (Jukka Sihvonen, Aalto): takes (paper, referee reports, editor letter) and emits a revision master plan as a directed acyclic graph using NetworkX. Identifies what tasks block what, batches them into execution blocks, flags conflicts between referees, and even proposes how to divide tasks between coauthors. Better for empirical papers (where the dependency structure is messy) than for theoretical (where dependencies are usually obvious).
  - Demonstrated by having Claude write a referee report on Goldsmith-Pinkham's own published RFS paper, then feeding the report + paper into the skill --- it produced a 26-task revision plan with critical path identified.
  - **refine.ink comparison:** refine is much better at internal-consistency checking and is what Goldsmith-Pinkham uses pre-submission. Strategic-revision is cheaper to run and complementary --- about *organizing* what to do once you have the report, not finding what's wrong.
  - **Editor-not-rewriter pattern:** ask Claude to read a draft and *insert markdown HTML comments* around weak passages without editing the text. Comments like "throat clearing," "vague praise that doesn't advance the argument," "filler" --- the kind of feedback you'd get from a NYT editor. Preserves voice because Claude never replaces your sentences.
  - Cowork (the browser desktop app) vs. Claude Code (CLI): for writing tasks Goldsmith-Pinkham uses Cowork; for data tasks Claude Code on the CLI. Editor-comment task can't be done in chat (chat can't write to local files); chat works for inline-skill-paste demos.
  - Closing aphorism (paraphrasing the IBM 1979 manual): "A computer can never be held accountable, therefore a computer must never make a management decision." Translate: in the end, it's *your* writing. You're responsible for what's there.

- **Summary**

This is the writing-and-thinking installment of Goldsmith-Pinkham's seven-part Markus Academy mini-series on Claude Code for applied economists. Where Episode 162-4 was about building 291M-row HMDA databases, this one is about the prose side of the research workflow.

The first third is a live build of a personal style-guide skill. Goldsmith-Pinkham points Claude Cowork at a folder containing his papers and blog posts and prompts (loosely): "create a writing style guide as a skill so I can get Claude to write in my voice." The result is a markdown file in `.claude/skills/paul-voice/SKILL.md` capturing patterns like "first-person plural in academic papers, conversational in blog posts, frequent em-dashes, set up the problem before the regression." He demonstrates the skill on a DiD-explainer prompt --- with-skill output is recognizably Paul, without-skill is default-AI. The honest caveat: the skill is sycophantic by default. Without explicit prompting it will not surface your *bad* writing habits, which limits its usefulness as a self-editing tool.

The middle third is a demo of [Sihvonen's strategic-revision skill](https://github.com/jusi-aalto/strategic-revision). The skill takes a paper + referee reports + editor letter and produces a directed-acyclic-graph revision master plan: what tasks block what, which referees disagree, how to batch the work into execution blocks, and how to split tasks between coauthors. Goldsmith-Pinkham emphasizes this is cheaper to run than refine.ink and complementary --- refine finds problems, strategic-revision organizes the response. He's used it on two actual papers and prefers it for empirical work (where the dependency structure is hard to see at a glance) over theoretical (where dependencies are typically more obvious).

The final third is the editor-not-rewriter pattern. Asked to "read this blog post and give comments in the style of a NYT editor for writing and clarity, but do not edit my writing --- create inline markdown HTML comments around weak passages" Claude returned the blog post unchanged but with marginal comments like "throat clearing," "vague praise that doesn't advance the argument," and "shape is jargon only bond literature would understand." Goldsmith-Pinkham frames this as the right way to use LLMs for writing if you want to preserve your voice: as an analytics engine that explains why a passage is weak, not as a rewriter.

- **Relevance to Economics Research**

Highly relevant for any economist doing manuscript-stage work. Three concrete things to take away: (1) the personal-style-guide-as-skill is a 5-minute setup that pays off in every subsequent writing task; (2) the strategic-revision skill is a real productivity gain on R&Rs --- the bottleneck on a revision is usually figuring out what to do, not doing it; (3) the editor-comment-only pattern solves the "AI rewrites my voice into mush" complaint that's been the main objection to AI-assisted writing.

For Mihail's audience, this is also a useful pairing with Cunningham's referee-report pipeline ([[summaries/cc-series-44-four-criteria-referee]]): Cunningham is on the *receiving* side of refereeing (using AI to prepare to write a report), Goldsmith-Pinkham is on the *responding* side (using AI to plan the revision after getting a report). Together they cover both ends of the peer-review loop.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/claude-code-skills]]
  - [[concepts/ai-writing]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/cc-series-38-plug-paulgp]]
  - [[summaries/large-datasets-economists]]
  - [[summaries/large-datasets-video]]
  - [[summaries/cc-series-44-four-criteria-referee]]
  - [[summaries/teaching-ai-your-voice]]
  - [[summaries/refine-ink-golub]]
