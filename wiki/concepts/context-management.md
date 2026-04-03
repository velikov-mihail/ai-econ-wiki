---
title: "Context Management"
tags: [concept, workflows, productivity]
sources:
  - "[[summaries/ai-project-folders.md]]"
  - "[[summaries/claude-code-what-comes-next.md]]"
  - "[[summaries/data-analysis-economists.md]]"
  - "[[summaries/edgar-filings.md]]"
  - "[[summaries/empty-folder-to-figure.md]]"
  - "[[summaries/getting-started-economists.md]]"
  - "[[summaries/getting-started-researchers.md]]"
  - "[[summaries/prompt-engineering.md]]"
date_updated: 2026-04-03
---

# Context Management

Context management refers to the strategies and techniques for working within the limited context window of large language models. Since LLMs can only process a finite amount of text at once (typically 100K-200K tokens), researchers must be deliberate about what information the model sees at each step.

## Context & Background

Every LLM interaction is constrained by a context window — the total amount of text (prompt + conversation history + response) the model can handle. For long research tasks, this creates practical challenges: the model may "forget" earlier instructions, lose track of project goals, or fail to connect insights across different parts of a large codebase.

Effective context management strategies include:

- **CLAUDE.md files**: Persistent instructions loaded at the start of every session
- **Structured project files**: Keeping plans, progress notes, and key decisions in files the AI can reference
- **Chunking**: Breaking large tasks into focused sub-tasks that fit within context
- **Summarization**: Periodically summarizing progress to compress context
- **Memory files**: Storing key decisions and learnings for retrieval across sessions

## Practical Implications

- **Front-load critical information**: Put the most important instructions at the beginning
- **Use file-based memory**: Don't rely on conversation history alone — write important context to files
- **Be explicit about scope**: Tell the model exactly which files or data to focus on
- **Refresh context periodically**: In long sessions, re-state key goals and constraints

## Related Concepts

- [[concepts/claude-md-files|Claude Md Files]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/plan-driven-development|Plan Driven Development]]
