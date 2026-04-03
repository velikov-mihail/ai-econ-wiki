---
title: "Data Privacy in AI Research"
tags: [concept, privacy, security, data]
sources:
  - "[[summaries/getting-started-economists.md]]"
  - "[[summaries/getting-started-researchers.md]]"
  - "[[summaries/llm-collaboration.md]]"
  - "[[summaries/mcp-setup.md]]"
  - "[[summaries/privacy-setup.md]]"
date_updated: 2026-04-03
---

# Data Privacy in AI Research

Data privacy in AI research covers the security and confidentiality considerations that arise when using cloud-based AI tools with potentially sensitive research data.

## Context & Background

Most AI tools send data to external servers for processing, raising significant concerns for researchers working with confidential data — including IRB-protected human subjects data, proprietary financial data from WRDS or similar providers, pre-publication research findings, and student records.

Key privacy considerations include:

- **Data transmission**: What data leaves your machine when you use an AI tool?
- **Data retention**: Do AI providers store your inputs for training or other purposes?
- **Compliance**: Does AI tool use comply with IRB protocols, data use agreements, and institutional policies?
- **Local alternatives**: When should you use local/on-premise models instead of cloud services?

## Key Perspectives

Several sources emphasize the importance of understanding privacy settings before using AI with any research data. Claude Code, for example, offers zero-retention API options, while other tools may use inputs for model training by default.

## Practical Implications

- **Read the terms of service**: Understand what happens to data you send to AI providers
- **Use zero-retention modes**: When available, enable settings that prevent data storage
- **Never send protected data**: IRB-restricted data should generally not be processed by cloud AI
- **Consider local models**: For sensitive data, use locally-running models (e.g., Ollama, llama.cpp)
- **Check data use agreements**: WRDS and similar providers may restrict AI processing of their data
- **Document your approach**: Include AI data handling in your research data management plan

## Related Concepts

- [[concepts/ai-tools-landscape|Ai Tools Landscape]]
- [[concepts/ai-limitations|Ai Limitations]]
- [[concepts/reproducibility-transparency|Reproducibility Transparency]]
