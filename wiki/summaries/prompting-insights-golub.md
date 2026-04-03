---
title: "Prompting Insights: Modern AI for Economics Research with Benjamin Golub"
tags: [summary, prompt-engineering, economics-research, llm-limitations]
sources:
  - "[[raw/articles/Prompting Insights Modern AI for Economics Research with Benjamin Golub  Markus Academy  Ep. 154.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Benjamin Golub (Northwestern University / refine.ink), Markus' Academy Ep. 154, published 2025-12-23. [YouTube](https://www.youtube.com/watch?v=ixyzgnmqAiU)

## Key Ideas

- LLMs are "superpowered but limited assistants": they have incredible intuition from training on the internet and can solve exam-level math problems, but they lack project-specific context, critical taste, and the ability to say "I don't know."
- Wrong information in a chat poisons the context and causes the model to try to reconcile errors with everything that follows -- so correcting mistakes inline is counterproductive. Start fresh chats for focused tasks instead.
- Good prompts specify the goal explicitly ("make surgical changes to handle corner solutions"), provide full context (proposition statement, existing proof, referee comment), and set behavioral rules upfront ("write concisely, do not rewrite from scratch") rather than reacting after the fact.
- Four key prompting techniques: role-playing ("you are a senior probabilist writing for Econometrica"), step-by-step decomposition, avoiding argument with the model (start new context instead), and handoff reports to transfer context between chats.
- LLMs have tunnel vision -- they optimize the immediate instruction even at the cost of broader quality (e.g., commenting out important code to make something compile). Their revealed preference is to give a conclusive answer rather than admit uncertainty.
- No striking long-distance conceptual connections across fields have been made by LLMs despite their vast training data, suggesting post-training has made consumer chatbots narrow.
- Managing multiple LLM tasks feels like "organizing a little bureaucracy" -- handoff reports between chats are essential for maintaining continuity across focused tasks.

## Summary

This is a transcript from a Markus' Academy webinar where Benjamin Golub, an economic theorist at Northwestern and co-founder of refine.ink, discusses how he uses AI in his research process. The talk is the first of a three-part series (prompting, Cursor, and refine.ink). Golub frames LLMs as brilliant but limited assistants that require active management, drawing an analogy to supervising eager but inexperienced junior employees.

Golub's central insight is that effective prompting is fundamentally about micromanagement -- providing the model with context it lacks and constraining its behavior in advance. He demonstrates this with a concrete example: fixing corner solutions in a network theory proof. The poor prompt simply says "handle the corner solutions." The good prompt specifies the goal (surgical changes only), provides full context (proposition, proof, referee comment), and sets house rules (write concisely, follow existing notation, do not rewrite from scratch). He emphasizes that behavioral instructions should be given proactively rather than reactively -- telling the model not to be verbose before it generates output, rather than asking it to shorten after the fact.

A recurring theme is the danger of poisoned context. When an LLM produces a mathematical error, the natural human instinct is to explain why it was wrong -- but this introduces wrong information into the chat that the model then tries to reconcile with subsequent output. Golub's solution is to start new chats for focused tasks and use handoff reports to transfer essential context between them. He endorses Paul Goldsmith-Pinkham's four prompting practices (role-playing, step-by-step planning, iteration, and not arguing) and notes these techniques are consistent across models (Claude, ChatGPT, Gemini). The discussion touches on a notable limitation: despite training on vast cross-disciplinary data, consumer chatbots have not produced unexpected cross-field conceptual connections, suggesting post-training narrows their capabilities.

## Relevance to Economics Research

This is one of the most directly relevant sources for economics researchers because Golub speaks as a practicing economic theorist. His examples -- fixing proofs, handling referee comments, writing for specific journal standards -- are core research tasks. The insight about poisoned context is especially important for researchers using AI for mathematical work: correcting a wrong proof step inline makes subsequent output worse, not better. The recommendation to use handoff reports between focused chats addresses the practical challenge of managing multi-task research projects (e.g., revising multiple propositions in response to referee reports). His observation that LLMs can solve Caltech exam-level math but lack taste for field-specific norms (combinatorics journal vs. AER proof standards) helps calibrate expectations for using AI in theoretical economics.

## Related Concepts

- [[concepts/prompt-engineering]]
- [[concepts/ai-limitations]]
- [[concepts/context-management]]
- [[concepts/ai-research-tools]]

## Related Summaries

- [[summaries/prompt-engineering]]
- [[summaries/prompt-plan-review-revise]]
- [[summaries/your-claude-md]]
- [[summaries/patterns]]
