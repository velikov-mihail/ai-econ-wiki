---
title: "Category Map"
tags: [visualization, navigation]
date_updated: 2026-04-26
---

# Category Map

A visual map of how the ten knowledge-base categories relate to one another. Arrows indicate primary knowledge-flow direction (foundational → applied).

```mermaid
graph TD
    FS["<b>Foundations & Setup</b><br/>16 summaries"]
    PE["<b>Prompt Engineering<br/>& Workflow</b><br/>10 summaries"]
    AG["<b>AI Agents &<br/>Agentic AI</b><br/>11 summaries"]
    CS["<b>Claude Code Skills<br/>& Advanced</b><br/>23 summaries"]
    DA["<b>Data Analysis &<br/>Web Scraping</b><br/>10 summaries"]
    AR["<b>Academic Research<br/>& Publishing</b><br/>23 summaries"]
    FE["<b>Finance &<br/>Econometrics</b><br/>13 summaries"]
    AT["<b>AI Tools &<br/>Comparisons</b><br/>9 summaries"]
    IS["<b>Institutional &<br/>Societal</b><br/>19 summaries"]
    PP["<b>Professional<br/>Productivity</b><br/>13 summaries"]

    %% Foundational layer
    FS --> PE
    FS --> AT
    PE --> AG
    PE --> CS

    %% Technical layer
    AG --> CS
    AG --> DA
    CS --> DA
    AT --> AG

    %% Applied layer
    DA --> AR
    DA --> FE
    AR --> FE
    CS --> AR
    AG --> AR

    %% Productivity & big picture
    PE --> PP
    CS --> PP
    AR --> IS
    FE --> IS

    %% Styling
    classDef foundation fill:#4a90d9,stroke:#2c5f8a,color:#fff
    classDef technical fill:#50b080,stroke:#2d7a50,color:#fff
    classDef applied fill:#e8a838,stroke:#b07820,color:#fff
    classDef bigpicture fill:#d05050,stroke:#903030,color:#fff

    class FS,PE foundation
    class AG,CS,AT technical
    class DA,AR,FE applied
    class IS,PP bigpicture
```

## Reading the Map

| Color | Layer | Categories |
|-------|-------|------------|
| Blue | **Foundational** | Foundations & Setup, Prompt Engineering & Workflow |
| Green | **Technical** | AI Agents, Claude Code Skills, AI Tools & Comparisons |
| Orange | **Applied** | Data Analysis, Academic Research, Finance & Econometrics |
| Red | **Big Picture** | Institutional & Societal, Professional Productivity |

**Suggested reading order:** Start with the blue (foundational) categories, then explore the green (technical) layer, and finally move to orange (applied) and red (big-picture) topics.

## Category Links

- [[summaries/foundations-setup|Foundations & Setup]]
- [[summaries/prompt-engineering-workflow|Prompt Engineering & Workflow]]
- [[summaries/ai-agents|AI Agents & Agentic AI]]
- [[summaries/claude-code-skills|Claude Code Skills & Advanced]]
- [[summaries/ai-tools|AI Tools & Comparisons]]
- [[summaries/data-analysis|Data Analysis & Web Scraping]]
- [[summaries/academic-research|Academic Research & Publishing]]
- [[summaries/finance-econometrics|Finance & Econometrics]]
- [[summaries/institutional-societal|Institutional & Societal]]
- [[summaries/professional-productivity|Professional Productivity]]
