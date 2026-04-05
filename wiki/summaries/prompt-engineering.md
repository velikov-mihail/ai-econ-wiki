---
title: Prompt Engineering
tags:
- summary
- prompt-engineering-workflow
- prompt-engineering
- ai-workflows
sources:
- '[[raw/articles/Prompt Engineering - Claude Blattman · AI for Professionals Who
  Don''t Code.md]]'
date_updated: 2026-04-03
date_published: 2026-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/essentials/prompting/)

## Key Ideas

- The gap between mediocre and great AI output is almost always the prompt -- not the model or subscription tier. Good prompts provide context, specify the task, and define the output format.
- A well-structured prompt has up to six sections: Role, Context, Task, Constraints, Output Format, and Bookend (restating the key instruction at the end for long prompts).
- Match prompting effort to stakes: use light prompts for routine tasks, standard prompts (with assumptions and rationale) for analysis, and deep prompts (with verification against best practices) for high-stakes work.
- Use examples sparingly -- try without them first, tighten instructions, and only add examples if the output format or style is still wrong.
- XML-style tags separate instructions from pasted content, preventing the AI from confusing the two.
- Break complex tasks into chained prompts so you can course-correct between steps rather than getting mediocre output across all subtasks at once.
- Common anti-patterns include vague thoroughness language ("be comprehensive"), over-prompting in all-caps, and failing to give the AI permission to push back.

## Summary

This article presents prompt engineering as a learnable, repeatable method rather than a technical skill. The core argument is that most poor AI interactions stem from unclear communication, not model limitations. Blattman provides a six-part anatomy of an effective prompt -- Role, Context, Task, Constraints, Output Format, and Bookend -- and illustrates each with a concrete example of drafting a grant methodology section for an economics RCT.

The article introduces a three-tier effort framework: light prompts for quick tasks, standard prompts that include assumptions and rationale, and deep prompts that invoke verification against established standards. This calibration prevents both under-engineering (vague requests) and over-engineering (wasting tokens on routine tasks). Blattman also covers practical techniques like XML tags for separating instructions from content, prompt chaining for complex multi-step work, and the strategic use of examples.

A distinctive feature is the recommendation to offload prompt engineering itself to the AI: create a project in ChatGPT or Claude.ai with prompt-formatting instructions, and the AI will restructure messy input into clean prompts. This "meta-prompting" approach lowers the barrier for users who find structured prompting unintuitive. The article also links to downloadable resources including a Prompt Preferences Template and a Prompting Best Practices Guide.

## Relevance to Economics Research

For economics researchers, the six-part prompt structure directly applies to tasks like drafting methodology sections, generating referee-style feedback, structuring literature reviews, and building pre-analysis plans. The effort-calibration framework is especially useful: light prompts suffice for email drafts, while deep prompts with verification are appropriate for econometric methodology or identification strategy review. The anti-pattern warnings -- especially about vague thoroughness language and not giving the AI permission to disagree -- address common failure modes when researchers use AI for substantive intellectual work.

## Related Concepts

- [[concepts/prompt-engineering]]
- [[concepts/plan-driven-development]]
- [[concepts/ai-workflows]]
- [[concepts/context-management]]

## Related Summaries

- [[summaries/prompt-plan-review-revise]]
- [[summaries/patterns]]
- [[summaries/your-claude-md]]
- [[summaries/ai-project-folders]]
- [[summaries/prompting-insights-golub]]
