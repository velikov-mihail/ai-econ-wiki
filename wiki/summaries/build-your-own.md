---
title: "Build Your Own"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/Build Your Own - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/system/)

## Key Ideas

- The "Build Your Own" path teaches users to create custom skills, agents, and self-improving workflows -- moving beyond consuming tools to building them
- The core idea is a continuous improvement meta-skill: notice friction, build a solution, critique and iterate (using AI to improve AI tools), and share what works
- Four sub-pages cover the key topics: Building Skills (creating slash commands), Agents vs Skills (architecture decisions), Continuous Improvement (the tips pipeline), and Patterns (reusable design patterns)
- No coding knowledge is required -- skills are written in markdown, not a programming language
- The system compounds over time: every skill built makes the next one easier, and every pattern learned applies to the next problem
- Reference materials include a 16,000-word guide on how Claude Code works under the hood (message stack, agentic loop, context window)

## Summary

This article serves as the landing page and roadmap for the advanced "Build Your Own" track of the Claude Blattman system. While earlier sections (Essentials and Toolkit) teach users to use and configure AI tools, this section teaches them to create custom tools that solve their specific problems. The core argument is that the most valuable aspect of the system is not any individual skill but the meta-skill of continuous improvement -- systematically noticing friction in workflows, building solutions, iterating with AI assistance, and sharing results.

The page outlines four sub-topics that form the curriculum: Building Skills covers creating custom slash commands from scratch; Agents vs Skills addresses when to use subagent architecture versus skills; Continuous Improvement describes the tips pipeline for capturing and integrating discoveries; and Patterns catalogs reusable design patterns and quality checklists. The prerequisites are modest -- a working Claude Code installation, a configured CLAUDE.md, some experience with existing skills, and comfort editing markdown.

The article also points to downloadable reference materials for deeper study, including skill design patterns with archetypes and quality checklists, an agents-vs-skills decision guide, a detailed technical document on Claude Code internals, and a curated tips and research log.

## Relevance to Economics Research

The continuous improvement framework is particularly relevant for economics researchers building AI-assisted research pipelines. The notice-build-iterate-share cycle maps directly onto the process of developing reproducible research workflows -- noticing repeated data cleaning steps, building automated pipelines, iterating based on results, and sharing replication code. The emphasis on no-code skill building lowers the barrier for economists who may be proficient in Stata or R but less comfortable with general-purpose programming. The agents-vs-skills architecture decision is analogous to choosing between monolithic scripts and modular function libraries in empirical research.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/skills-vs-agents]]
- [[concepts/ai-workflows]]
- [[concepts/plan-driven-development]]

## Related Summaries

- [[summaries/building-skills]]
- [[summaries/skill-library]]
- [[summaries/continuous-improvement]]
- [[summaries/patterns]]
- [[summaries/real-claude-md]]
