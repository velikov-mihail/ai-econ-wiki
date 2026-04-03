---
title: "Using LLMs with Cursor: Modern AI for Economics Research"
tags: [summary, ai-tools, cursor, coding, economics-research, prompting]
sources:
  - "[[raw/articles/Using LLMs with Cursor Modern AI for Economics Research w Benjamin Golub  Markus Academy  Ep. 154.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Benjamin Golub (Northwestern University) and Markus Brunnermeier (Princeton University), *Markus' Academy*, Episode 154, December 23, 2025
- **Original**: [https://www.youtube.com/watch?v=gb9v5ze0zhU](https://www.youtube.com/watch?v=gb9v5ze0zhU)

## Key Ideas

- **LLMs are brilliant but limited junior assistants**: strong at bounded tasks, weak on high-level project context and norms. They are overconfident (guess rather than say "I don't know") and suffer from tunnel vision (optimize local instructions at the expense of the real objective).
- **Cursor as an orchestration tool**: moves beyond browser-based chatbots by giving LLMs access to your entire project repository (LaTeX files, BibTeX, code), enabling retrieval-augmented generation (RAG) across your codebase.
- **Model selection by task**: Claude/Opus excels at coding and workflow management; GPT-5.2 excels at math-heavy tasks. Cursor allows easy switching between models mid-workflow.
- **Step-by-step decomposition**: split tasks into phases (background document, then proof strategy, then implementation) rather than one-shot prompts. This lets you review and steer at each stage.
- **Overleaf-to-GitHub-to-Cursor pipeline**: sync academic papers from Overleaf to GitHub, then clone into Cursor to get an AI-native LaTeX editing environment with full agent capabilities.
- **Don't fight the model**: if you get a wrong answer, start a new chat rather than continuing (wrong outputs poison future responses in the same context).
- Cursor's RAG automatically embeds your repository in a semantic space and pulls relevant context as it works, though you can also manually attach specific files.

## Summary

This video transcript captures Benjamin Golub's tutorial on using Cursor as an AI-native environment for economics research, introduced by Markus Brunnermeier's vision of how AI will transform the field by 2030. Brunnermeier outlines future possibilities including LLM-based agent models, synthetic experimental subjects, causal inference 2.0 with unstructured data, and AI-augmented refereeing. He also predicts that GitHub downloads will become a more important metric of paper impact than citations.

Golub demonstrates a practical workflow for academic economists: syncing papers from Overleaf to GitHub, cloning into Cursor, and then using the agent panel to assign tasks that have full access to your paper's LaTeX source, bibliography, and auxiliary code. He shows concrete examples including having the AI find and fill in missing references across a paper (a bounded RA-style task using Claude Opus), and then a more ambitious task of developing proof strategies for a proposition (using GPT-5.2 for its math capabilities). The key insight is that decomposing work into stages -- first a background document collecting relevant context, then a proof strategy, then implementation -- yields much better results than one-shot prompts because the model can focus its "thinking energy" on each stage separately.

Golub also demonstrates that for well-specified coding tasks (like generating a simulation to illustrate a theoretical result), one-shot prompts can work well -- the AI orchestrates its own software engineering workflow, installs dependencies, and produces working output. He emphasizes that Cursor's model-agnostic nature is its main advantage, allowing researchers to mix and match models based on task requirements, and that chatbots themselves are excellent guides for learning to use these tools.

## Relevance to Economics Research

This is one of the most directly relevant resources for economics researchers adopting AI tools. Golub demonstrates actual research workflows -- writing proofs, managing references, running simulations -- inside a tool environment that integrates naturally with existing academic infrastructure (Overleaf, GitHub, LaTeX, BibTeX). The model-selection-by-task approach (Claude for coding, GPT for math) and the step-by-step decomposition strategy are immediately applicable to theory, empirical, and computational economics work. The Overleaf-GitHub-Cursor pipeline solves a practical problem for co-authored papers.

## Related Concepts

- [[concepts/ai-agents]]
- [[concepts/prompt-engineering]]
- [[concepts/ide-and-terminal]]
- [[concepts/retrieval-augmented-generation]]
- [[concepts/agentic-workflows]]

## Related Summaries

- [[summaries/refine-ink-golub]]
- [[summaries/prompting-insights-golub]]
- [[summaries/guide-which-ai]]
- [[summaries/llm-collaboration]]
