---
title: "LLM Reasoning"
tags: [concept, technology, evaluation]
sources:
  - "[[summaries/ai-agents-generative-ai.md]]"
  - "[[summaries/chatgpt-vs-claude.md]]"
  - "[[summaries/llm-collaboration.md]]"
  - "[[summaries/project-ape.md]]"
  - "[[summaries/theory-core-uses-markus-166-1.md]]"
date_updated: 2026-08-23
---

# LLM Reasoning

LLM reasoning refers to the ability of large language models to perform multi-step logical inference, mathematical analysis, and complex problem-solving — and the methods used to evaluate these capabilities.

## Context & Background

Modern LLMs demonstrate increasingly sophisticated reasoning through techniques like chain-of-thought prompting, where the model "thinks step by step" before answering. Specialized reasoning models (e.g., Claude with extended thinking, OpenAI's o-series) dedicate more computation to complex problems.

Key aspects of LLM reasoning include:

- **Chain-of-thought**: Step-by-step reasoning that improves accuracy on complex tasks
- **Deep research**: Extended autonomous investigation of complex questions
- **Tool-augmented reasoning**: Using calculators, code execution, and databases to supplement reasoning
- **Evaluation challenges**: Reasoning quality is hard to assess because correct-looking reasoning can reach wrong conclusions

### Reasoning on formal proofs

Ortoleva and Sandomirskiy's assessment ([[summaries/theory-core-uses-markus-166-1|Markus Academy 166-1]]) is the most specific evidence in this wiki on reasoning quality for formal work. Their verdict: frontier models generate *reliable* proofs for the kind of model economists typically write — reliable meaning usually correct, not submittable, since the prose is notation-heavy and over-long. Non-frontier models are not reliable end-to-end and need the task decomposed into single steps.

More useful than the reliability question is their reframing of what reasoning is *for*. Three uses beat proof generation: **attack** (the model as hostile referee hunting weak steps), **repair** (given a false statement, which assumption rescues it), and **inspiration** (a wrong proof that suggests a route the author hadn't considered). The last is the sharpest point — reasoning output can be valuable even when the conclusion is wrong.

The corresponding failure mode is that fluent reasoning is increasingly hard to falsify. Ortoleva describes losing two weekends to a polished proof of a statement he knew to be false, which neither he nor an adversarial model could break. His rule: the risk scales with your own ignorance of the area, so treat proofs invoking mathematics you cannot personally check as the highest-risk case.

## Practical Implications

- **Use reasoning models for complex tasks**: When accuracy matters more than speed, choose models with extended thinking
- **Verify reasoning chains**: Don't just check the answer — review the reasoning steps
- **Decompose complex problems**: Break hard questions into simpler sub-questions
- **Provide relevant context**: Reasoning improves dramatically when the model has access to the right information
- **Put the model in the adversarial seat**: Asking it to attack a proof or argument is more reliable than asking it to produce one
- **Never grade in the same session**: Use a separate verifier — and, for high stakes, a third judge between prover and verifier

## Related Concepts

- [[concepts/ai-limitations|Ai Limitations]]
- [[concepts/agentic-ai|Agentic Ai]]
- [[concepts/ai-agents|Ai Agents]]
