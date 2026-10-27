---
title: "Agent Sandboxing & Permission Modes"
tags: [concept, sandboxing, security, autonomous-agents, claude-code]
sources:
  - "[[summaries/claude-container.md]]"
  - "[[summaries/econ-yolobox.md]]"
  - "[[summaries/permissions-openclaw-markus-162-7.md]]"
  - "[[summaries/permissions-sandboxes-substack.md]]"
date_updated: 2026-10-27
---

# Agent Sandboxing & Permission Modes

Agent sandboxing means running a coding agent (Claude Code, Codex) inside an environment, usually a container, that limits which files, tools, network destinations and credentials it can reach. The agent can then run without per-action approval while the worst case stays survivable.

## Context & Background

Coding agents act through tools: they read and write files, run shell commands, install packages and make network requests. Claude Code and Codex offer roughly three approval modes:

- **Manual**: approve every action.
- **Auto**: a classifier or reviewer decides which actions need confirmation.
- **YOLO** (`--dangerously-skip-permissions`): no prompts at all.

Goldsmith-Pinkham ([[summaries/permissions-openclaw-markus-162-7]], [[summaries/permissions-sandboxes-substack]]) frames these as choices about *when* you do the safety thinking: during the session (manual) or in advance (environment design). Manual mode gives a false sense of security because people approve prompts reflexively, and a determined agent works around individual tool denials (denied `ls`, it tries `find`).

## Key Perspectives

- **The boundary matters, not the brand.** Docker and dev containers, `agent-safehouse` (kernel-enforced on macOS), `claude-container` ([[summaries/claude-container]]) and remote VMs all apply the same principle: the agent sees only what the host mounts, and it cannot change that from inside.
- **Sandboxing as a risk-return frontier.** Chen's [[summaries/econ-yolobox]] plots AI use from no AI up to YOLO mode and argues that YOLO *inside a container* beats the frontier. His design adds a permissive "normie" container on the same files, and package volumes the YOLO agent can only read. The aim is that nobody has a reason to switch the sandbox off, and an unattended agent cannot install malicious packages.
- **Network allowlists.** A firewall that allows only the model providers (plus chosen research sites) blocks data exfiltration and prompt-injected downloads. It also blocks legitimate browsing, which is why the setups pair it with an escape hatch.
- **Credentials are the soft spot.** An unsandboxed agent in your home directory can reach `~/.ssh` and every API key. Even inside a container, credential relays (e.g., attaching VS Code to the container) can leak host access.
- **Sandboxing does not protect your data.** A container limits what the agent can *do*, not what the model *sees*. Mounted confidential data still goes to the provider. For that problem see [[concepts/data-privacy]]: API versus subscription terms, Bedrock, PII filtering and local models.

## Practical Implications

- Never run YOLO mode directly on your host machine. Start it only inside a container or a kernel-level sandbox.
- Mount only the project folder (read-only where possible), and keep SSH keys and other projects out of reach.
- Use a separate, permissive environment for package installs and web research, rather than loosening the main sandbox.
- Keep git history for every project so that a destructive agent action can be undone (see [[concepts/version-control-research]]).
- Treat the sandbox and data governance as two separate decisions.

## Related Concepts

- [[concepts/data-privacy|Data Privacy]]
- [[concepts/claude-code|Claude Code]]
- [[concepts/human-in-the-loop|Human in the Loop]]
- [[concepts/agentic-workflows|Agentic Workflows]]
- [[concepts/version-control-research|Version Control Research]]
