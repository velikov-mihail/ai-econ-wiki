---
title: "Vibe Research, or How I Wrote an Academic Paper in Four Days"
tags: [summary, academic-research, vibe-research, ai-tools, workflow]
sources:
  - "[[raw/articles/Vibe Research, or How I Wrote an Academic Paper in Four Days.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Vincent Gregoire (personal blog, 2026)

## Key Ideas

- "Vibe research" is the research analogue of "vibe coding" -- using AI to rapidly iterate on ideas and produce a research paper, analogous to Karpathy's concept for code.
- Gregoire went from idea to a complete working paper on SSRN in four days, using Claude Code as the primary workhorse with multiple AI agents (Codex CLI, OpenCode/Gemini) for parallel review.
- The workflow involved: idea generation from a podcast, outline via Claude, overnight first draft by Claude Code in YOLO mode, multi-agent review loops, iterative refinement, reference verification, and model simplification.
- Human judgment remained critical at every stage: choosing the idea, steering model design, deciding which reviewer suggestions to accept, and verifying references and math.
- Reference accuracy was a real problem -- one fabricated reference and one with wrong metadata were caught only through systematic verification using Claude with browser access.
- The author admits discomfort with not fully understanding every line of math in his own paper, highlighting a transparency and intellectual ownership tension.

## Summary

Vincent Gregoire recounts writing the paper "Investing in Artificial General Intelligence" in approximately four days using an AI-first approach, motivated by a call for papers for a Human x AI Finance conference at UCLA Anderson. The idea originated from listening to a Dario Amodei interview about AI infrastructure investment. Gregoire used Claude to develop a literature review and plan, then set Claude Code to work overnight in permissive mode, producing a complete first draft by morning.

The iteration process was systematic: multiple AI agents (Claude Code, Codex CLI, OpenCode with Gemini) independently reviewed the paper, code, and proofs, producing consolidated reports. Gregoire then directed Claude Code to implement the suggested fixes. He repeated this review-and-fix cycle many times, supplemented by reviews from ChatGPT and Claude.ai on the rendered PDF. He also used Claude's research mode for literature and media references, and Claude Cowork with Chrome for reference verification.

Key technical choices included using Quarto for the paper (markdown-based, AI-friendly), Python with uv for code, sympy for analytical solutions, and Git/GitHub for version control. The author emphasizes that despite AI doing nearly all writing and coding, the human in the loop provided essential guidance: the initial idea, simplification attempts, judgment calls on feedback, and reference verification. He frames the experience as making him "faster, not smarter."

## Relevance to Economics Research

This is one of the most detailed accounts of an economist using AI to produce a complete research paper, including a theoretical model with analytical and numerical solutions. It directly demonstrates how AI changes the production function of academic finance research -- dramatically compressing timelines while raising new questions about intellectual ownership, verification burden, and the meaning of authorship. The workflow is especially relevant for researchers considering AI-assisted theoretical or computational work.

## Related Concepts

- [[concepts/vibe-research]]
- [[concepts/feedback-machines]]
- [[concepts/ai-research-tools]]
- [[concepts/human-in-the-loop]]

## Related Summaries

- [[summaries/reflections-vibe-research]]
- [[summaries/feedback-machines]]
- [[summaries/ai-one-shot-papers]]
- [[summaries/research-in-time-of-ai]]
