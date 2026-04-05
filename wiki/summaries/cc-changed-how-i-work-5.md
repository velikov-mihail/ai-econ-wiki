---
title: "Claude Code Changed How I Work (Part 5): Challenges of Adopting Software Not Designed For Us"
tags: [summary, claude-code-skills, marginal-user, risk-management, shell-commands, workflow-design]
sources:
  - "[[raw/articles/How Claude Code Changes How I Work (part 5) On The Challenges of Adopting Software That Was Not Designed For Us.md]]"
date_updated: 2026-04-05
date_published: 2026-01-12
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/more-claude-code-part-5-letters-to](https://causalinf.substack.com/p/more-claude-code-part-5-letters-to)

- **Key Ideas**
  - The marginal user of Claude Code (empirical social scientists) is fundamentally different from the average user (computer scientists) -- the knowledge gap about shell commands, terminal, and filesystem operations creates real hazards.
  - Claude Code can do anything you can do at the terminal: it has access to the same shell commands, including destructive ones like `rm -rf`, `git reset --hard`, `chmod`, and file overwrites.
  - The real risk is not malice or rogue behavior but miscommunication -- the gap between what you intended ("clean up this data and save it") and what Claude Code interpreted ("overwrite the original").
  - Permission fatigue is a specific hazard: Anthropic's safety prompts ask for confirmation so frequently that users start auto-approving, potentially authorizing destructive operations.
  - The solution is not listing prohibited commands but designing workflows that endogenously minimize risk: version control, radical backups, dry runs, precise language, test environments, and working-directory awareness.

- **Summary**

Cunningham writes a cautionary post for empirical social scientists -- the "marginal user" of Claude Code -- who are about to adopt a tool built by and for computer scientists. The core argument is that the average Claude Code user takes for granted knowledge about Unix, terminal, shell commands, and filesystem operations that the marginal user simply does not have. Most social scientists work inside graphical interfaces (RStudio, Stata) and have never typed `rm -rf` or `git reset --hard`. They do not realize that Claude Code operates via these same shell commands, and that anything they could do at a terminal, Claude Code can and will do if instructed -- knowingly or unknowingly.

The post catalogs specific dangerous commands (file deletion, disk overwrites, permission changes, git history destruction, data corruption) not to teach them but to illustrate the magnitude of the knowledge gap. Cunningham then pivots to the real risk: miscommunication. Drawing on the social scientist's cardinal rule of never saving over original data, he shows how ambiguous instructions ("clean up this data and save it," "move these files to archive," "delete the temp files") can be interpreted destructively. He proposes six practical safeguards: version control everywhere, radical backups (Dropbox, Time Machine, external drives), habitual dry runs, precise "annunciated" language, starting in test environments, and always checking the working directory. The overarching message is that the workflow itself -- not any single rule -- is the safety mechanism.

- **Relevance to Economics Research**

Essential reading for any economist adopting Claude Code or similar AI agents. The marginal-vs-average user framework is itself an economics concept applied to technology adoption. The specific risks cataloged (overwriting data, destructive git commands, silent file moves) map directly onto common empirical workflow hazards. The proposed safeguards -- especially version control, backups, and precise instructions -- constitute a practical risk-management checklist for AI-augmented empirical research.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/ai-adoption-academia]]
  - [[concepts/version-control-research]]
  - [[concepts/claude-md-files]]
  - [[concepts/human-ai-collaboration]]
  - [[concepts/ai-for-non-coders]]
  - [[concepts/ide-and-terminal]]

- **Related Summaries**
  - [[summaries/cc-changed-how-i-work-1]]
  - [[summaries/cc-changed-how-i-work-2]]
  - [[summaries/cc-changed-how-i-work-3]]
  - [[summaries/cc-changed-how-i-work-4]]
  - [[summaries/cc-series-6-video-explainer]]
