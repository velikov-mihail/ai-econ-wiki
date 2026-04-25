---
title: "Writing & Thinking with AI Assistance (Goldsmith-Pinkham Substack)"
tags: [summary, academic-research]
sources:
  - "[[raw/articles/Writing & Thinking with AI Assistance.md]]"
date_updated: 2026-04-25
date_published: 2026-04-11
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM), companion Substack post to Markus Academy 162-5
- **Original**: [https://paulgp.substack.com/p/writing-and-thinking-with-ai-assistance](https://paulgp.substack.com/p/writing-and-thinking-with-ai-assistance)

- **Key Ideas**
  - **Three preliminary concerns** that frame the rest of the post:
    1. **Writing is thinking.** Cognitive offloading is real --- if you hand vague ideas to an LLM, it does the intellectual work for you and you lose the thinking. The test for whether you've offloaded too much: can you discuss the ideas in depth *without* the LLM?
    2. **Homogenization of voice.** LLMs are "floor raisers" --- they significantly improve poor writing but produce a uniform default voice. Voice is part of being a human academic; you should be aware of yours and try to preserve it.
    3. **Banal but necessary writing.** Boilerplate emails, memo summaries, regression-coefficient write-ups --- LLMs are excellent at this, and offloading the banal frees time for the important. The trick is the bright line between banal and important.
  - **Style-guide-as-skill workflow:** collect samples → ask Claude to extract patterns → curate output into `writing_style.md` → reference in prompts. The output is "a list of rules of what it thinks about how to tweak the LLM's behavior" --- not a voice capture but a set of constraints that pushes the output in a better direction. By default the analysis is sycophantic; push hard for negative observations if you want the bad-habits list.
  - Multiple style guides for different registers: Goldsmith-Pinkham keeps separate ones for academic papers vs. social media / blog posts. The social media one is "painfully sycophantic to read back."
  - **Strategic-revision skill** (Sihvonen, Aalto): parses each referee comment into a discrete task → categorizes (argumentative / empirical-robustness / clarification / editorial) → builds a NetworkX DAG to find dependencies → organizes into parallel execution blocks → flags conflicts between referees → identifies collateral risks → proposes coauthor task division. Demonstrated on a Goldsmith-Pinkham published paper: 26-task plan in five blocks. He's used it on two real papers and prefers it for *both* empirical and theoretical work --- the dependency structure is sometimes cleaner for theory papers.
  - **Editor-not-rewriter pattern:** prompt Claude to insert markdown HTML comments around weak passages without editing the prose. The comments stay invisible in render but visible in source. This solves the homogenization-of-voice problem because Claude never replaces your sentences; you're forced to engage with each comment and decide whether to rewrite, cut, or disagree.
  - **Margin-notes approach to ideas:** instead of "what should I write?" ask the LLM to comment on what you've *already* written. Same logic as the editor pattern --- keeps you the author, uses Claude as the analytics engine.
  - **Practical:** style-guide / referee-skill / strategic-revision require Cowork or Claude Code (filesystem access). Chat can run them inline if you paste the skill markdown into the prompt, but it loses local-filesystem skills and creates extra distance between your files and the LLM.
  - **Closing image:** the IBM 1979 training manual --- "A computer can never be held accountable, therefore a computer must never make a management decision." Substitute "writing" for "management decision."

- **Summary**

This is the written companion to Goldsmith-Pinkham's Markus Academy 162-5 video (see [[summaries/writing-thinking-markus-162-5]]). The substantive demos are the same --- build a personal style guide as a Claude skill, use Sihvonen's strategic-revision skill on referee reports, use Claude as a comment-only editor --- but the post frames them inside a more careful three-concern preamble: writing is thinking, voice gets homogenized, banal writing is the easy win.

The framing matters because it gives a principled answer to "when should I use an LLM in my writing?" Goldsmith-Pinkham's answer: offload the banal aggressively (boilerplate, first-pass regression write-ups), use the LLM as a constraint-setting tool (style guides) for things that need to sound like you but where you don't want to do the thinking, use it as a comment-only editor when you want to preserve voice while getting feedback, and avoid the cognitive-offloading trap by iterating ideas yourself before bringing the LLM in. The "test for over-offloading" --- can you discuss the ideas in depth without the LLM? --- is the practical heuristic.

Style guides are reframed in this post as "list of rules" rather than "voice capture" --- a useful clarification, because the implicit expectation that a skill will *recreate* your voice is the wrong frame. The right frame is that the skill biases the model toward better-than-default output that has *some* of your characteristic constraints, not a sufficient set of them. You iterate, you curate, you keep multiple guides for different registers.

The strategic-revision section reproduces the same demo as the video but adds the design rationale: a referee report is overwhelming because it's a flat list of comments with implicit dependencies. Converting it to a DAG with execution blocks turns "I have to do all this stuff" into "do these three tasks in parallel, then these two depend on the first set."

The IBM-1979 closing is the strongest line in the post. The author is responsible. Use the tools, but don't let them make decisions you should be making.

- **Relevance to Economics Research**

Direct and complementary to the video summary. Where the video shows *what* the workflow looks like in practice, the Substack post explains *why* the workflow is designed this way --- which is the more durable artifact for course material or for someone deciding how to integrate AI into their own writing process.

For Mihail's master-class audience, the three preliminary concerns (writing as thinking, voice homogenization, banal-vs-important) are the cleanest framing of the AI-and-writing problem in the wiki. They give students a defensible posture --- not "AI is bad" or "use AI for everything," but "offload the banal, use AI as a constraint-setter for voice work, use AI as a comment-only editor when voice matters, never let AI make the decision." That's the position to recommend.

- **Related Concepts**
  - [[concepts/ai-writing]]
  - [[concepts/claude-code-skills]]
  - [[concepts/agentic-workflows]]
  - [[concepts/ai-in-education]]

- **Related Summaries**
  - [[summaries/writing-thinking-markus-162-5]]
  - [[summaries/cc-series-44-four-criteria-referee]]
  - [[summaries/teaching-ai-your-voice]]
  - [[summaries/refine-ink-golub]]
  - [[summaries/feedback-machines]]
