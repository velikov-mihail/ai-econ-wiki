---
title: "Version Control for Research"
tags: [concept, tools, reproducibility]
sources:
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/project-manager-claude.md]]"
date_updated: 2026-04-03
---

# Version Control for Research

Version control for research applies software engineering practices — primarily Git and GitHub — to manage research code, data pipelines, papers, and collaborative workflows in economics and social sciences.

## Context & Background

Version control is standard in software engineering but still uncommon in economics research. AI coding tools are accelerating adoption because they work best within version-controlled repositories — tools like Claude Code create commits, branches, and can manage the full git workflow.

Benefits for researchers include:

- **History tracking**: Every change is recorded with context about why it was made
- **Collaboration**: Multiple researchers can work on the same codebase without conflicts
- **Reproducibility**: Any past state of the analysis can be exactly recreated
- **Backup**: Distributed repositories provide automatic redundancy
- **AI integration**: AI coding tools can read git history to understand project evolution

## Practical Implications

- **Start with git init**: Every new research project should be a git repository from day one
- **Commit frequently**: Small, focused commits with clear messages make history useful
- **Use GitHub for collaboration**: Share code and track issues with coauthors
- **Don't commit data**: Keep large datasets out of git; use .gitignore and document data sources
- **Let AI manage commits**: Tools like Claude Code can create atomic commits as they work

## Related Concepts

- [[concepts/reproducibility-transparency|Reproducibility Transparency]]
- [[concepts/plan-driven-development|Plan Driven Development]]
- [[concepts/ide-and-terminal|Ide And Terminal]]
