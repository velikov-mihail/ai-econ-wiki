---
title: "Human-AI Collaboration"
tags: [concept, workflow, research-quality]
sources:
  - "[[wiki/summaries/vibe-research.md]]"
  - "[[wiki/summaries/reflections-vibe-research.md]]"
  - "[[wiki/summaries/what-ai-got-wrong.md]]"
  - "[[wiki/summaries/research-in-time-of-ai.md]]"
  - "[[wiki/summaries/feedback-machines.md]]"
  - "[[wiki/summaries/agentic-everything.md]]"
date_updated: 2026-04-03
---

# Human-AI Collaboration

## Definition

Human-AI collaboration in economics research refers to the working relationship between a researcher and AI tools, where each party contributes distinct capabilities. The AI handles execution-intensive tasks -- coding, data cleaning, literature search, drafting, formatting -- while the human provides research taste, identification judgment, institutional knowledge, and the ability to recognize when AI output is plausible but wrong. The term "human-in-the-loop" captures the minimum requirement: a human who reviews, validates, and directs AI work at critical decision points.

This is not a symmetric partnership. The human sets direction, evaluates quality, and makes judgment calls; the AI executes at speed. The analogy most frequently used is supervising a very fast, very knowledgeable research assistant who occasionally fabricates results with complete confidence.

## Context & Background

The human-AI collaboration question became urgent in economics research in early 2026 as agentic tools made it possible to produce complete research papers with minimal human input. Two prominent experiments -- Vincent Gregoire's four-day paper and Joshua Gans's year-long AI-first research program -- provided contrasting evidence about what happens when the human role is minimized versus maintained. The emerging consensus is that AI makes researchers "faster, not smarter" (Gregoire), and that the human contribution -- knowing which questions matter, exercising judgment about identification, catching subtle errors -- has become more valuable precisely because everything else has become cheaper.

The error patterns documented by Blattman and others reveal a systematic feature of AI mistakes: they are consistently **plausible**. AI does not make random errors; it makes errors that look right to someone not checking carefully. This means that effective collaboration requires the human to exercise genuine domain expertise, not just rubber-stamp AI output.

## Key Perspectives

**Gregoire ([[wiki/summaries/vibe-research.md|Vibe Research]])** provides the most detailed account of human-AI collaboration in producing a complete academic paper. Over four days, he used Claude Code as the primary workhorse with multiple agents for parallel review. Human judgment was critical at every stage: choosing the idea, steering model design, deciding which reviewer suggestions to accept, and verifying references and math. He caught one fabricated reference and one with wrong metadata through systematic verification. His honest admission -- discomfort with not fully understanding every line of math in his own paper -- highlights the intellectual ownership tension inherent in deep AI collaboration.

**Gans ([[wiki/summaries/reflections-vibe-research.md|Reflections on Vibe Research]])** provides the cautionary counterpoint. After a year of AI-first research, he identifies three failure modes: AI makes subtle theoretical mistakes beyond simple math errors (especially around equilibrium concepts and information sets); lower completion costs lead to pursuing weaker ideas; and LLMs are "seductive" -- they present formal results with confidence, making it easy to believe you have a result when you do not. His conclusion: high-speed, low-human-input research did not produce high-quality output.

**Blattman ([[wiki/summaries/what-ai-got-wrong.md|What AI Got Wrong]])** documents specific error patterns from a tax preparation case study that generalize to research: PDF extraction errors in roughly 1 in 10 documents, plausible but wrong categorizations, and outright hallucinated numbers. Every error follows the same pattern: AI does something plausible but wrong, the error requires domain knowledge to catch, and a deliberate review mechanism catches it. His meta-lesson: "AI makes tax preparation faster. It does not make tax preparation easier."

**Goldsmith-Pinkham ([[wiki/summaries/research-in-time-of-ai.md|Research in the Time of AI]])** offers the systematic framework. He maps AI capabilities onto each stage of the research pipeline (ideation through publication) and identifies the key distinction: execution skills (coding, data cleaning, drafting) are depreciating, while judgment skills (research taste, identification strategy, institutional knowledge) are appreciating. AI is "a flashlight in the dark -- the hard part is still knowing where to walk."

**Backman ([[wiki/summaries/feedback-machines.md|Feedback Machines]])** demonstrates a specific collaboration pattern: using AI as a structured feedback tool. His workflow progresses from referee-style reports to section-by-section evaluation to consistency checks. The key limitation: AI can make weak arguments sound coherent, potentially smoothing over conceptual problems rather than fixing them.

**Svoronos ([[wiki/summaries/agentic-everything.md|Agentic Everything]])** frames the collaboration challenge as requiring two separate skills: domain expertise (which directs the AI) and AI tool proficiency (which makes direction effective). Both are necessary; neither is sufficient.

## Practical Implications

For economics researchers designing human-AI workflows:

- **Never skip verification**: AI errors are systematically plausible, not random. Fabricated references, hallucinated numbers, and wrong-but-reasonable categorizations require active domain expertise to catch.
- **Build explicit review gates**: the workflow should have mandatory human checkpoints between stages -- after data construction, after estimation, after interpretation. Do not let AI run from question to conclusion without intermediate review.
- **Use multiple agents for review**: Gregoire's multi-agent review (Claude Code, Codex, Gemini) and Blattman's agent debate pattern both exploit the principle that different AI instances catch different errors.
- **Maintain decision authority on identification**: which comparison group, which instrument, which exclusion restriction -- these are judgment calls that define the credibility of empirical work. AI can suggest options, but the researcher must choose and defend.
- **Budget cooling-off time**: Gans's recommendation of at least a month before posting is a practical safeguard against the seductiveness of rapid AI-assisted production.
- **Treat AI suggestions as candidates, not defaults**: Backman's principle of exercising independent judgment applies to every AI output, from code to prose to analytical suggestions.

## Open Questions

- What is the minimum level of domain expertise required for effective human-AI collaboration? Can a PhD student who has not yet internalized econometric intuition effectively supervise AI-generated empirical analysis?
- How should authorship norms evolve when AI contributes substantial intellectual labor (not just execution)?
- Is there a reliable way to detect when AI has made a subtle theoretical error (e.g., wrong equilibrium concept) versus a superficial one (e.g., wrong sign on a coefficient)?
- As AI capabilities improve, will the human role converge toward pure judgment and taste, or will new forms of collaborative work emerge that we cannot yet anticipate?
- How should the research community handle the disclosure dilemma -- where honest AI use disclosure creates professional risk while concealment faces no consequences?

## Sources

- [[wiki/summaries/vibe-research.md|Vibe Research]] -- Gregoire's four-day paper with detailed human-AI division of labor
- [[wiki/summaries/reflections-vibe-research.md|Reflections on Vibe Research]] -- Gans's year-long cautionary experiment
- [[wiki/summaries/what-ai-got-wrong.md|What AI Got Wrong]] -- Blattman's taxonomy of AI error patterns
- [[wiki/summaries/research-in-time-of-ai.md|Research in the Time of AI]] -- Goldsmith-Pinkham's pipeline framework
- [[wiki/summaries/feedback-machines.md|Feedback Machines]] -- Backman's structured feedback workflow
- [[wiki/summaries/agentic-everything.md|Agentic Everything]] -- Svoronos on the dual-skill requirement
