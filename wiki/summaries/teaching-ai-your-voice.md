---
title: "Teaching AI Your Voice"
tags: [summary, ai-tools, writing, workflow, prompting]
sources:
  - "[[raw/articles/Teaching AI Your Voice - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman (claudeblattman.com)

## Key Ideas

- AI has a default "house style" that overwrites your voice; the fix is a "voice file" reference document, not better prompting.
- The process involves: collecting 5-10 writing samples, having AI analyze them for specific patterns, generating a voice spec/style guide, and adding annotated examples.
- Annotated examples (with context, example text, and notes) teach AI your patterns far more reliably than abstract rules.
- A "ban list" of AI-default words (delve, leverage, multifaceted, furthermore, robust, compelling, etc.) provides immediate improvement.
- The voice file must be loaded into a persistent project (Claude Projects, ChatGPT Projects, or CLAUDE.md for Claude Code), not pasted into one-off chats.
- Voice drift is the primary long-term failure mode; fix it by updating the voice file whenever the AI gets your voice wrong.

## Summary

Chris Blattman presents a systematic five-step method for teaching AI to write in your personal voice. The approach centers on creating a "voice file" -- a reference document that captures your actual writing patterns -- and loading it into a persistent AI project so every conversation inherits your style. The method starts with collecting diverse writing samples, then having AI analyze them for specific patterns (paragraph openings, sentence length, repeated moves, vocabulary preferences), generating a concise style guide, and crucially, adding 3-5 annotated examples that show rather than tell.

The article demonstrates the difference with a before/after comparison: without a voice file, AI produces generic academic prose ("The mentoring program represents a comprehensive approach..."); with one, it produces writing that sounds like a specific researcher ("We're testing whether a cheap, scalable mentoring program can reduce violence among high-risk young men..."). Blattman emphasizes that examples beat rules because AI pattern-matches against examples more reliably than it follows abstract instructions, and provides a structured format with context, example text, and explanatory notes.

The article also covers maintenance: every time AI gets your voice wrong, you should update the voice file rather than just fixing the output. A diagnostic table maps common failures (using banned words, long compound sentences, hedging) to the rules that need to be added or tightened.

## Relevance to Economics Research

Maintaining a distinct authorial voice is important for economists who use AI for drafting and editing. This guide is directly applicable to writing research papers, grant proposals, referee responses, and policy briefs. The voice file approach addresses the common complaint that AI-assisted writing "all sounds the same" and can help researchers preserve the directness, precision, and personal style expected in top economics journals.

## Related Concepts

- [[concepts/ai-writing-workflow]]
- [[concepts/prompting-techniques]]
- [[concepts/ai-research-tools]]

## Related Summaries

- [[summaries/feedback-machines]]
- [[summaries/document-collection]]
- [[summaries/research-in-time-of-ai]]
