---
title: "Claude Code 25: More Autonomous Agents Are Coming to Research"
tags: [summary, ai-agents, security, openclaw, remote-control, cowork, anthropic, autonomous-agents]
sources:
  - "[[raw/articles/Claude Code 25 More Autonomous Agents Are Coming to Research.md]]"
date_updated: 2026-04-05
date_published: 2026-02-26
---

- **Author/Source**: Scott Cunningham (Baylor University), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-25-more-autonomous-agents](https://causalinf.substack.com/p/claude-code-25-more-autonomous-agents)

- **Key Ideas**
  - OpenClaw went viral (230k GitHub stars) as an always-on AI agent but had catastrophic security flaws: no authentication by default, unmoderated skill marketplace, prompt injection vulnerabilities
  - Cisco's Skill Scanner found a top-ranked OpenClaw skill was functionally malware, silently exfiltrating user data via curl commands
  - Kaspersky found ~1,000 open OpenClaw installations with no authentication; 230+ malicious plugins published in one week on ClawHub
  - A new class of security risk: the attack vector is a prompt (semantic), not exploitable code (syntactic), making it invisible to conventional security tools
  - Anthropic responded with two features: Cowork scheduled tasks (`/schedule`) and Claude Code Remote Control (phone access to local sessions)
  - Key architectural difference: Anthropic uses TLS encryption, sandboxed environments, short-lived credentials, explicit permission prompts, and no inbound ports — contrasting OpenClaw's open design
  - Anthropic's early investment in safety and trust may now be a competitive advantage as security concerns grow with AI agent adoption
  - Practical research use cases: overnight data jobs, automated RA tasks, remote classroom support, iterative paper management from mobile

- **Summary**

Cunningham uses the OpenClaw security disaster as a lens for understanding the next phase of AI agent development and Anthropic's response. OpenClaw — an always-on AI agent accessed via WhatsApp — went viral in January 2026 but was riddled with security vulnerabilities. Cisco's research found a top-ranked skill was secretly exfiltrating user data. Kaspersky discovered nearly 1,000 installations with zero authentication, and over 230 malicious plugins appeared on ClawHub in a single week. Most alarmingly, the attack surface is semantic (malicious prompts embedded in emails or documents) rather than syntactic, making it largely invisible to traditional security tools.

Anthropic responded by shipping two features that target the same always-on use case but with proper security architecture: Cowork scheduled tasks (recurring automated work while your machine is awake) and Claude Code Remote Control (accessing your local session from a phone with encrypted, outbound-only connections). The tradeoff is less raw capability — your computer must be on, and there is more friction — but the security model is fundamentally different. Cunningham argues that Anthropic's long bet on safety as a brand identity is now paying dividends, and he outlines four practical research applications: overnight data jobs, automated RA tasks, remote classroom support, and managing paper revisions from a phone.

- **Relevance to Economics Research**

The essay introduces researchers to the emerging security landscape of AI agents — a critical concern as these tools gain system-level access to research data, code, and credentials. The practical use cases (overnight simulations, automated literature sweeps, remote paper management) map directly onto common research workflows. The discussion of prompt injection as a new attack vector is essential reading for anyone deploying AI agents in environments with sensitive data such as WRDS credentials or pre-publication results.

- **Related Concepts**
  - [[concepts/agentic-ai]]
  - [[concepts/data-privacy]]
  - [[concepts/ai-adoption-academia]]
  - [[concepts/ai-research-tools]]
  - [[concepts/claude-code]]

- **Related Summaries**
  - [[summaries/cc-series-21-faculty-adoption]]
  - [[summaries/cc-series-24-agents-auditing-did]]
  - [[summaries/cc-series-21-attention-congestion]]
  - [[summaries/cc-series-16-memory-foam]]
