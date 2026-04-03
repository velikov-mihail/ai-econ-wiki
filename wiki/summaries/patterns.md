---
title: "Patterns"
tags: [summary, design-patterns, ai-workflows, claude-code]
sources:
  - "[[raw/articles/Patterns - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---
- **Original**: [https://claudeblattman.com/system/patterns/](https://claudeblattman.com/system/patterns/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/system/patterns/)

## Key Ideas

- Phased Execution breaks complex workflows into stages with user checkpoints ("STOP: Discuss with user before proceeding"), preventing irreversible actions from running without review.
- Flags Parsing uses named arguments (`quick`, `depth:light/standard/deep`, `file:path`, `focus:dimension`, `dryrun`, `help`) to keep one skill flexible instead of creating multiple variants.
- The Critic Stance pattern explicitly shifts Claude from collaborator to critic, counteracting its default tendency toward agreement -- especially important when Claude reviews its own work.
- Output Templates define the exact format of skill output for consistency and comparability across runs.
- Iteration Gates present output and then explicitly ask whether to proceed, adjust, or stop before applying changes.
- Depth Calibration adjusts thoroughness (light/standard/deep) based on task importance, avoiding over-engineering simple requests.
- Behavioral patterns include Graceful Degradation (proceeding with available resources when integrations are missing) and Domain Auto-Detection (inferring the right behavior from content signals rather than requiring explicit flags).

## Summary

This article catalogs reusable design patterns for building Claude Code skills and workflows, organized into structural patterns and behavioral patterns. The structural patterns address how to organize skill execution: Phased Execution with human checkpoints, Flags Parsing for configurable behavior, Critic Stance for honest assessment, Output Templates for consistent formatting, and Iteration Gates for user approval before changes take effect.

The behavioral patterns address how skills should adapt to context: Depth Calibration scales thoroughness to task stakes, Graceful Degradation handles missing integrations without dead ends, and Domain Auto-Detection infers the appropriate behavior from content signals (e.g., detecting "regression" or "RCT" triggers a methodology persona). Together, these patterns form a design vocabulary for building AI tools that are flexible, robust, and appropriately cautious.

The article concludes with a Quality Checklist for shipping skills: the zero-argument case should be the most common use, output format should be specified (not left to Claude), error handling should cover missing files and integrations, the skill should be focused on one task, and it should be tested with real tasks beyond the happy path.

## Relevance to Economics Research

Several patterns are directly applicable to research tool-building. Phased Execution maps onto multi-step empirical workflows where intermediate results should be reviewed before proceeding (e.g., data cleaning before estimation). Depth Calibration is useful for tasks that range from quick data checks to full robustness analyses. The Critic Stance pattern is valuable for getting honest feedback on research designs, paper drafts, or identification strategies -- addressing the well-known problem that AI defaults to agreement. Domain Auto-Detection could allow a single research assistant skill to adapt its behavior for theory papers versus empirical work based on content signals.

## Related Concepts

- [[concepts/design-patterns]]
- [[concepts/ai-workflows]]
- [[concepts/prompt-engineering]]
- [[concepts/human-in-the-loop]]

## Related Summaries

- [[summaries/architecture-patterns]]
- [[summaries/prompt-plan-review-revise]]
- [[summaries/prompt-engineering]]
- [[summaries/workflows]]
