---
title: "Vibe Research"
tags: [concept, academic-research, ai-limitations, research-quality]
sources:
  - "[[wiki/summaries/vibe-research.md]]"
  - "[[wiki/summaries/reflections-vibe-research.md]]"
  - "[[wiki/summaries/ai-one-shot-papers.md]]"
  - "[[wiki/summaries/can-ai-replace-researchers.md]]"
  - "[[wiki/summaries/research-in-time-of-ai.md]]"
date_updated: 2026-04-03
---

## Definition

**Vibe research** is the academic research analogue of "vibe coding" -- using AI to rapidly iterate on ideas and produce a research paper with minimal human hands-on-keyboard time, analogous to Andrej Karpathy's concept for software development. The term captures workflows where AI does nearly all the writing, coding, and formal analysis while the human provides direction, judgment, and quality control. In its most aggressive form, it means going from idea to posted working paper in days rather than months.

The concept is deliberately provocative. It names a real phenomenon -- the dramatic compression of research timelines enabled by AI tools -- while carrying an implicit warning that speed and ease can compromise rigor. The tension between the productivity gains and the quality risks is the central theme across all sources discussing vibe research.

## Context & Background

The term gained traction in 2025-2026 as multiple researchers publicly documented AI-first paper production. Vincent Gregoire went from idea to SSRN in four days using Claude Code. Joshua Gans ran a year-long experiment producing many working papers with maximum AI assistance. David Yanagizawa-Drott's APE platform automated the production of hundreds of policy evaluation papers. These experiments surfaced both the promise (dramatically compressed timelines, democratized access to sophisticated methods) and the problems (fabricated references, overclaimed results, pursuit of weak ideas, methodological monoculture).

The vibe research debate sits within a broader discussion about how AI changes the production function of academic research. Paul Goldsmith-Pinkham frames it as a cost reduction that "hones the question of what is good research" -- AI compresses execution but cannot substitute for research taste. David Karpf argues more bluntly that if Claude Code is a better researcher than you, the problem is that you stopped trying to answer interesting questions.

## Key Perspectives

**Gregoire** ([[wiki/summaries/vibe-research.md]]) provides the most detailed positive account. He produced a theoretical finance paper in four days using Claude Code in YOLO mode overnight, multi-agent review loops, and systematic reference verification. He emphasizes that human judgment remained critical at every stage: choosing the idea, steering model design, deciding which suggestions to accept, and verifying references. He admits discomfort with not fully understanding every line of math in his own paper, highlighting the intellectual ownership tension. His framing: AI makes you "faster, not smarter."

**Gans** ([[wiki/summaries/reflections-vibe-research.md]]) provides the most detailed negative account -- a rare, honest post-mortem from a year-long experiment. He identifies three major pitfalls. First, AI makes **subtle theoretical mistakes** beyond simple math errors -- particularly around equilibrium concepts and information sets in game-theoretic models. Second, the reduced cost of completion leads to **pursuing weaker ideas** that would normally be abandoned at natural decision points. Third, LLMs are **seductive** -- they present formal results with confidence, making it easy to believe you have discovered something when you have not. He produced many working papers, some accepted at lower-tier journals, but none at top-tier outlets. His revised approach: mandatory cooling-off periods, more peer feedback, and explicit go/no-go decision points.

**Goldsmith-Pinkham (One-Shot Papers)** ([[wiki/summaries/ai-one-shot-papers.md]]) examines the methodological composition of AI-generated empirical papers and finds that automated systems overwhelmingly default to difference-in-differences (64% of APE papers vs. 35% of NBER papers). This **methodological monoculture** reflects that DiD is the most formulaic causal inference method, but doing it well requires significant human judgment about parallel trends, treatment timing, and identification assumptions. The methods AI finds easiest to automate are precisely the ones where researcher discretion matters most.

**Karpf** ([[wiki/summaries/can-ai-replace-researchers.md]]) argues that the real issue is not AI capability but the broken incentive structure of academic publishing. If AI can produce "barely publishable" articles at scale, it accelerates the collapse of a publish-or-perish system that was already dysfunctional. Researchers should refocus on "What questions do I actually want to answer?" rather than optimizing for publication metrics.

**Goldsmith-Pinkham (Research in the Time of AI)** ([[wiki/summaries/research-in-time-of-ai.md]]) provides the most systematic framework. He maps the research pipeline stage by stage (ideation through publication) and argues that AI compresses execution but does not railroad over the process. The skills AI replicates are execution skills (coding, data cleaning, drafting); the skills it does not replicate -- research taste, identification judgment, institutional knowledge -- have become more valuable, not less.

## Practical Implications

- **Use AI to accelerate, not to shortcut**: The researchers who report the best outcomes use AI to compress timelines while maintaining human judgment at every decision point.
- **Build in cooling-off periods**: Gans's experience suggests that posting immediately after AI-assisted production bypasses the quality filters that normally catch weak ideas. Wait at least a month.
- **Verify everything**: Reference accuracy is a known failure mode. Gregoire caught one fabricated reference and one with wrong metadata only through systematic verification. Formal results require independent checking.
- **Maintain explicit go/no-go decision points**: The reduced cost of completion means the usual signals for abandoning a project (difficulty, slow progress) are suppressed. Actively decide whether each project is worth continuing.
- **Beware methodological monoculture**: If an AI system defaults to a particular empirical strategy, that should be a warning sign rather than a convenience. Consider whether the chosen method is actually the right one for the research question.
- **Distinguish execution from judgment**: AI can code a DiD estimation in minutes, but choosing the right control group, evaluating pre-trends, and interpreting results remain human tasks.

## Open Questions

- Will the academic community develop norms for AI-assisted research disclosure, analogous to conflict-of-interest disclosures?
- How should tenure committees evaluate a paper written in four days versus four years if the quality is comparable?
- Can AI-assisted replication offset the p-hacking risks that come with easier execution?
- Is "vibe research" a transitional phenomenon (improving as models get better at judgment) or a permanent limitation (reflecting something fundamental about the difference between execution and taste)?
- What institutions or norms can prevent the race to the bottom in which quantity of AI-produced papers crowds out quality?

## Sources

- [[wiki/summaries/vibe-research.md]] -- Gregoire's four-day paper production workflow
- [[wiki/summaries/reflections-vibe-research.md]] -- Gans's year-long post-mortem on AI-first research
- [[wiki/summaries/ai-one-shot-papers.md]] -- Goldsmith-Pinkham on methodological monoculture in AI-generated papers
- [[wiki/summaries/can-ai-replace-researchers.md]] -- Karpf on broken incentives and the core of social science
- [[wiki/summaries/research-in-time-of-ai.md]] -- Goldsmith-Pinkham's stage-by-stage analysis of AI in the research pipeline
