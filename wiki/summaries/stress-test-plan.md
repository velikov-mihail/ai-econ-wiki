---
title: "Stress-Test Any Plan"
tags: [summary, professional-productivity, plan-review, prompt-engineering, sycophancy]
sources:
  - "[[raw/articles/Stress-Test Any Plan - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/workflows/plan-review-browser/)

## Key Ideas

- AI tools are good at helping build plans but bad at critiquing them due to sycophancy -- the tendency to agree with what the user seems to want. The fix: the reviewer must not be the author.
- The method is simple: finish a plan in one conversation, then paste it into a brand new chat for critique. Fresh context eliminates anchoring bias.
- The provided prompt instructs the AI to act as an external reviewer (not collaborator), classify findings as "MUST FIX" or "WORTH CONSIDERING," and end with a PROCEED or REVISE FIRST verdict.
- For high-stakes plans (grants, major hires), run a second review in another fresh chat with a different persona (budget analyst, regulatory expert, field operations manager).
- Common mistakes: reviewing in the same conversation where you built the plan, trusting the verdict without reading findings, using a plan that is too vague, and adopting AI revisions wholesale without thinking.
- The prompt can be saved as a Claude.ai Project or ChatGPT Custom GPT for repeat use.

## Summary

This article presents a practical method for using AI to critically evaluate plans, proposals, and decisions. The core insight draws on the known problem of AI sycophancy: a model that helped develop an idea has a natural bias toward defending it. The solution is to always use a fresh conversation for review, ensuring the reviewer has zero knowledge of the author's reasoning, compromises, or earlier drafts.

The article provides a copy-paste prompt that frames the AI as an external reviewer tasked with finding failure modes, missing elements, unrealistic assumptions, and necessary changes. Each finding is classified by severity. The method applies to grant proposals, research designs, pre-analysis plans, hiring decisions, and any situation where the cost of a bad plan exceeds the 10 minutes the review takes. The article also provides instructions for saving the prompt as a reusable Claude.ai Project or ChatGPT Custom GPT, and warns against several common mistakes including over-trusting well-formatted AI output.

## Relevance to Economics Research

This technique is directly applicable to reviewing research designs, pre-analysis plans, and grant proposals -- all high-stakes documents in economics where catching problems early saves months of work. The adversarial review prompt can serve as a quick "pre-referee" check before circulating a paper or submitting a proposal. The multi-persona approach (reviewing as a methodologist, then as a budget analyst, then as a field operations manager) mirrors the different perspectives a grant review panel would bring, making it useful for stress-testing grant applications before submission.

## Related Concepts

- [[concepts/prompt-engineering]]
- [[concepts/ai-workflows]]
- [[concepts/sycophancy-and-bias]]

## Related Summaries

- [[summaries/project-management]]
- [[summaries/ai-executive-assistant]]
- [[summaries/example-research-design]]
