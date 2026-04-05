---
title: "Claude Code for Academics: An AI Agent for Empirical Research"
tags: [summary, academic-paper, claude-code, ai-agents, research-workflow, beamer]
sources:
  - "[[raw/papers/main.tex]]"
  - "[[raw/papers/main.pdf]]"
date_updated: 2026-04-03
date_published: 2026-03-18
---
- **Original**: [https://github.com/aspi6246/Claude-Code-Presentation](https://github.com/aspi6246/Claude-Code-Presentation)

**Authors**: Alessandro Spina (UTS Finance Department)

## Key Ideas

- Claude Code is an AI agent that lives in your terminal and operates directly on project files -- reading, editing, executing code, and building persistent memory via markdown files (CLAUDE.md)
- AI capability follows a "jagged frontier": superhuman at literature review, stats code, data cleaning, formatting/LaTeX, and cross-language replication, but below human level at visual reasoning, causal identification, economic judgment, and novel ideas
- The "Cunningham Conjecture" (from Scott Cunningham): hallucination errors are orthogonal across programming languages, so cross-language replication (R, Stata, Python matching to 6 decimal places) catches bugs that single-language review would miss
- Context window management is a core practical challenge -- CLAUDE.md files, session logs, and the Orient-Plan-Execute-Verify workflow are essential for productive sessions
- The marginal cost of generating figures drops to zero with AI agents, enabling "verification through visualization" -- plotting data before every regression as a routine sense check
- Claude Code can serve as a personal editor (using structured markdown personas) that audits prose, structure, and argumentation, with iterative Critic/Fixer patterns
- The entire slide deck was itself built with Claude Code, demonstrating the tool's capability for generating Beamer presentations from content descriptions

## Summary

This Beamer presentation, delivered at a UTS Finance Department brownbag in March 2026, provides a comprehensive introduction to Claude Code for finance and economics academics. Spina frames the core problem: most academics use LLMs in a copy-paste chat paradigm that lacks project context and implementation capability. The opportunity is an AI agent that functions as a dedicated research assistant, reading your data, running code, building slides, and working alongside you on full projects.

The presentation covers Claude Code's architecture (LLM + tools including Read, Write, Edit, Bash, Grep, Glob), pricing ($20-200/month), and alternatives (GitHub Copilot, ChatGPT, OpenAI Codex CLI). A central theme is the "jagged frontier" of AI capability -- tasks where AI excels (lit review, stats code, data cleaning, formatting, cross-language replication) versus where humans retain advantage (causal identification, economic judgment, novel ideas). Spina illustrates this with personal examples: rebuilding teaching courses, taming legacy codebases, and using AI-generated visualizations for data sense-checking.

The practical heart of the talk covers setup and workflow. Spina emphasizes the "amnesia problem" -- Claude forgets everything between sessions -- and the solution of external memory through CLAUDE.md files, README.md documentation, and dated session logs. The recommended workflow follows four steps: Orient (read the project), Plan (draft approach, get approval), Execute (run the work), and Verify (check output, cross-language tests). Data privacy considerations are noted: Claude Code runs locally but sends file contents to Anthropic's servers for processing, with data retained 30 days for safety review.

## Relevance to Economics Research

This presentation is tailored specifically for empirical finance and economics researchers, with examples drawn from event studies, asset pricing, and econometric workflows. The cross-language replication idea (the "Cunningham Conjecture") is particularly relevant for empirical work where coding errors can be subtle and consequential. The emphasis on CLAUDE.md as institutional memory for research projects addresses a real pain point in collaborative academic research. The practical setup instructions and workflow patterns make this an actionable guide for academics at any stage of AI adoption.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ai-agents]]
- [[concepts/context-management]]
- [[concepts/cross-language-replication]]
- [[concepts/ai-adoption-academia]]
- [[concepts/skills-vs-agents]]

## Related Summaries

- [[summaries/korinek-2023]]
- [[summaries/panjwani-slides]]
- [[summaries/baylor-ai-taskforce]]
