---
title: "AI Limitations"
tags: [concept, quality, risk]
sources:
  - "[[summaries/ai-one-shot-papers.md]]"
  - "[[summaries/can-ai-replace-researchers.md]]"
  - "[[summaries/chatbots-done-right.md]]"
  - "[[summaries/korinek-2023.md]]"
  - "[[summaries/openai-automated-researcher.md]]"
  - "[[summaries/prompting-insights-golub.md]]"
  - "[[summaries/reflections-vibe-research.md]]"
date_updated: 2026-04-03
---

# AI Limitations

AI limitations encompass the known failure modes, capability boundaries, and systematic biases of current large language models that researchers must understand to use these tools responsibly.

## Context & Background

Despite rapid improvements, LLMs have well-documented limitations that are especially consequential in research settings where accuracy matters:

- **Hallucination**: Generating plausible but false information, including fabricated citations, statistics, and facts
- **Sycophancy**: Tendency to agree with the user rather than push back on incorrect assumptions
- **Reasoning failures**: Struggling with complex logical chains, mathematical proofs, and multi-step deductions
- **Knowledge cutoffs**: Training data has a fixed endpoint; models don't know about recent developments
- **Context limitations**: Performance degrades with very long inputs or when key information is buried
- **Lack of true understanding**: Pattern matching can mimic understanding without genuine comprehension

## Key Perspectives

The "jagged frontier" concept (Ethan Mollick) captures how AI capabilities are uneven — performing superbly on some tasks while failing unpredictably on seemingly similar ones. This makes it dangerous to generalize from AI successes to assume competence across all tasks.

## Practical Implications

- **Always verify**: Treat AI output as a first draft requiring expert review, never as ground truth
- **Test edge cases**: AI often fails on unusual inputs or uncommon scenarios
- **Use structured outputs**: Constrained formats reduce hallucination risk
- **Maintain domain expertise**: AI amplifies the capabilities of knowledgeable users; it cannot replace expertise
- **Document AI involvement**: Track which parts of your work involved AI for reproducibility

## Related Concepts

- [[concepts/research-quality|Research Quality]]
- [[concepts/human-in-the-loop|Human In The Loop]]
- [[concepts/jagged-frontier|Jagged Frontier]]
- [[concepts/sycophancy-and-bias|Sycophancy And Bias]]
