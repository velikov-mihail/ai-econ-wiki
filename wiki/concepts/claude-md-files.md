---
title: "CLAUDE.md Files"
tags: [concept, configuration, context-management, claude-code]
sources:
  - "[[summaries/your-claude-md.md]]"
  - "[[summaries/real-claude-md.md]]"
  - "[[summaries/learn-ai-coding-agents.md]]"
  - "[[summaries/claude-code-newbies.md]]"
  - "[[summaries/my-claude-code-setup.md]]"
  - "[[summaries/cc-changed-how-i-work-5.md]]"
  - "[[summaries/cc-series-6-video-explainer.md]]"
date_updated: 2026-04-05
---

## Definition

A **CLAUDE.md** file is a personal or project-level instruction document that Claude Code reads automatically at the start of every session. It provides persistent context about who you are, how you work, what tools you use, and what conventions to follow. Without it, every session starts fresh and generic; with it, Claude tailors its behavior to your actual workflow, skill level, and preferences from the first interaction.

CLAUDE.md files operate in a two-tier system. A **global** file at `~/.claude/CLAUDE.md` captures personal identity and general preferences. **Project-level** files in individual project directories capture project-specific conventions, team members, data locations, and tool choices. Claude loads the global file first, then project-specific overrides. This mirrors the distinction Antonio Mele draws between `CLAUDE.md` (personal, local, Claude Code only) and `AGENTS.md` (project-specific, version-controlled, shared with team, portable across tools).

## Context & Background

The CLAUDE.md concept emerged from a practical problem: LLMs have no memory between sessions. Every interaction starts with a blank slate unless the user provides context. Early users found themselves repeating the same background information -- their research field, preferred languages, file locations, co-author names -- at the start of every session. CLAUDE.md solves this by encoding that context in a file that loads automatically.

The concept has evolved from simple identity statements ("I'm a researcher") to sophisticated configuration systems. Chris Blattman's production CLAUDE.md is 150+ lines compared to the starter template's 20 lines -- a gap that represents months of iteration. The most iterated section is typically the Confirmation Guidelines: defining when Claude should act autonomously versus ask for permission. Advanced users employ a modular pattern, splitting detailed instructions into topic-specific files (`core-voice.md`, `email-voice.md`, `project-management.md`, `integration-notes.md`) to keep the main file under 200 lines.

## Key Perspectives

**Blattman (Your CLAUDE.md)** ([[summaries/your-claude-md.md]]) introduces the concept and provides a fill-in-the-blank template. He emphasizes being specific and actionable (file paths, skill levels, tool preferences) rather than vague. Key sections include: professional identity, primary work, tools and software, file locations, skill levels, working preferences, and current projects. He notes that everything in CLAUDE.md is sent to the API, so passwords and API keys must be excluded. Voice and writing style preferences can be stored in `~/.claude/rules/core-voice.md` for auto-loading.

**Blattman (Real CLAUDE.md)** ([[summaries/real-claude-md.md]]) shows the end state: a production file with a Technology Stack table mapping where files live and how to access each system, Inline Triggers that override default behavior for high-stakes actions (e.g., "use send-email.py, not MCP" for email; "use gh CLI, not MCP" for Overleaf), and a Modular Rules pattern. The Confirmation Guidelines define a boundary: ask before sending emails or writing to Google Docs, but do not ask after receiving clear instructions, after plan approval, or for routine file operations. He summarizes the design principle as: global CLAUDE.md describes *how you work*; project-level files describe *what you're working on*.

**Mele** ([[summaries/learn-ai-coding-agents.md]]) places CLAUDE.md within a broader configuration hierarchy: organization policies > user CLAUDE.md > project AGENTS.md > task-level skills > immediate prompt. He positions `AGENTS.md` as the primary project-level file (version-controlled, shared, portable across Claude Code, Cursor, and Gemini CLI) and `CLAUDE.md` as the personal-preferences layer.

**Sant'Anna** ([[summaries/my-claude-code-setup.md]]) demonstrates the most complex configuration: 22 slash commands, 18 context-aware rules, and a `[LEARN:tag]` system where corrections persist in a MEMORY.md file across sessions. His setup shows how CLAUDE.md can anchor a full multi-agent academic workflow.

## Practical Implications

- **Start small, iterate often**: Begin with 20 lines capturing your identity, tools, and file locations. Expand as you discover what Claude gets wrong without guidance.
- **Be specific**: "I use R and Stata for empirical work; data is at D:/Data/CRSP/" is far more useful than "I do data analysis."
- **Include honest skill levels**: Saying "beginner Python, expert Stata" prevents Claude from producing code that is too advanced or too basic.
- **Use the two-tier system**: Global file for identity and preferences; project files for each paper's conventions, co-author preferences, and data pipeline.
- **Sync across machines**: Use symlinks from `~/.claude/CLAUDE.md` to a cloud-synced folder (Dropbox, OneDrive).
- **Tune confirmation guidelines carefully**: Start permissive and tighten. The boundary between "just do it" and "ask me first" takes weeks to get right.
- **Go modular when complexity grows**: Split detailed instructions into topic-specific files loaded from `~/.claude/rules/` to keep the main file scannable.

## Open Questions

- How should co-authors coordinate when they have different global CLAUDE.md preferences but share a project?
- What is the optimal length and level of detail for a CLAUDE.md before it starts degrading performance by consuming too much context?
- Should CLAUDE.md files be version-controlled and shared publicly, or do they contain too much personal workflow information?
- How will the `AGENTS.md` standard (portable across tools) interact with Claude-specific `CLAUDE.md` features as the ecosystem evolves?

## Sources

- [[summaries/your-claude-md.md]] -- Blattman's introduction and template for CLAUDE.md
- [[summaries/real-claude-md.md]] -- Blattman's annotated production CLAUDE.md example
- [[summaries/learn-ai-coding-agents.md]] -- Mele's configuration hierarchy (CLAUDE.md vs. AGENTS.md)
- [[summaries/claude-code-newbies.md]] -- CLAUDE.md as part of the Claude Code setup sequence
- [[summaries/my-claude-code-setup.md]] -- Sant'Anna's advanced configuration with MEMORY.md and 18 rules
