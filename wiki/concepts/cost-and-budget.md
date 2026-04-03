---
title: "Cost and Budget"
tags: [concept, tools, professional-productivity]
sources:
  - "[[summaries/cost-reality.md]]"
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/llm-collaboration.md]]"
  - "[[summaries/train-left-station.md]]"
  - "[[summaries/daaf-framework.md]]"
date_updated: 2026-04-03
---

# Cost and Budget

## Definition

The cost of AI-assisted research encompasses subscription fees for AI tools, API usage charges, the time investment required to learn and configure the tools, and the opportunity cost of the researcher's attention. For economics researchers, the relevant comparison is not abstract value but concrete alternatives: hours of research assistant time, conference travel, software licenses, and the researcher's own hourly rate. A realistic cost-benefit analysis must account for both the ongoing subscription costs and the significant upfront learning investment required to reach productive use.

## Context & Background

As of early 2026, the AI tool landscape for researchers spans a wide price range. At the low end, a single $20/month subscription (Claude Pro or ChatGPT Plus) provides access to capable chatbot-level AI. At the high end, a full productivity stack -- agentic coding tool, secondary AI for web search, voice dictation, meeting transcription -- runs approximately $140/month ($1,700/year). API-based usage (Claude Code on the Anthropic API) adds variable costs depending on usage intensity. The rapid decline in LLM operating costs -- 83-92% since GPT-4's launch, according to Korinek -- means that the cost calculus is a moving target, with capabilities increasing and per-token prices decreasing simultaneously.

For academic researchers, these costs must be evaluated against institutional norms. A $1,700/year tool subscription is modest relative to typical research budgets (roughly equivalent to 7 RA hours/month at $20/hour) but may feel significant to unfunded graduate students or researchers at under-resourced institutions. The introduction of free and open-source frameworks like DAAF provides a partial path to reducing costs, though the most capable models still require paid subscriptions.

## Key Perspectives

**Blattman ([[summaries/cost-reality.md|The Cost Reality]])** provides the most detailed cost breakdown for academic researchers. His full stack costs approximately $140/month: Claude Max ($100), ChatGPT Plus ($20), Wispr Flow ($10), Granola ($10). The minimum viable setup for graduate students is approximately $20/month (Claude Pro plus free built-in dictation and Zoom transcription). His ROI framework is straightforward: if the system saves 5+ hours/month at an effective hourly rate of $40+, the math works. A configured system realistically saves 10-15 hours/month, but reaching that level requires honest upfront time investment. He recommends a four-week ramp-up sequence starting with just the chatbot and adding tools progressively.

**Panjwani ([[summaries/ai-agents-econ-research.md|AI Agents for Economic Research]])** offers budget-conscious advice specifically for development economists and researchers at under-resourced institutions. For budget-constrained researchers at $20/month, he recommends Codex (OpenAI) over Claude Code due to more generous usage limits. He argues that pushing toward $200/month is worthwhile if possible, because learning speed is proportional to usage. His advice acknowledges the global dimension: researchers in low-income countries face the same subscription costs as those at well-funded US institutions.

**Korinek ([[summaries/llm-collaboration.md|LLM Collaboration]])** documents the macro cost trends: LLM operating costs have declined 83-92% since GPT-4's launch while quality has improved substantially. Open-source models (Llama, Qwen) have closed much of the gap with proprietary leaders, offering benefits of transparency, privacy, and reproducibility at lower cost. The shift to inference-heavy reasoning models (o1-style) introduces higher variable costs, changing the cost structure from training-dominated to inference-dominated.

**Messing and Tucker ([[summaries/train-left-station.md|The Train Has Left the Station]])** add a dimension often omitted: energy consumption. They report that coding sessions consume 25-50 watt-hours and full-day usage exceeds 1 kilowatt-hour. While not a significant cost for individual researchers, this matters at institutional scale and for the broader sustainability discussion.

**DAAF ([[summaries/daaf-framework.md|DAAF Framework]])** represents the open-source alternative. As a free, LGPL-3.0-licensed framework built on Claude Code, it provides sophisticated research workflows (pre-analysis plans, reproducibility verification, econometric methods) without additional licensing costs -- though it still requires a Claude Code subscription for the underlying model.

## Practical Implications

For economics researchers making budget decisions:

- **Minimum viable entry**: $20/month (one AI subscription) is sufficient for chatbot-level assistance with writing, literature search, and basic coding. This is accessible to most graduate students.
- **Productive research workflow**: $100-200/month unlocks agentic coding tools that qualitatively change what is possible (autonomous code execution, data pipeline construction, multi-agent review). For researchers with grant funding, this is equivalent to a few RA hours and likely saves more time than it costs.
- **Grant budgets**: AI tool subscriptions should be included in research budgets. At $1,700/year, the cost is comparable to a single conference registration or a few months of part-time RA support.
- **ROI is front-loaded in learning time**: the biggest cost is not the subscription but the hours spent learning to use the tools effectively. Budget 20-40 hours of learning over the first month.
- **API vs. subscription pricing**: Claude Code running on the API incurs variable costs that scale with usage. Heavy users may find subscription plans (Claude Max at $100/month) more predictable. Light users may prefer pay-as-you-go API access.
- **Data policy matters for cost**: researchers handling confidential data (CRSP, Compustat, administrative records) must understand which tools and pricing tiers guarantee data is not used for training. Claude Code API conversations are not used for training; Claude.ai consumer tier has a different policy.

## Open Questions

- How quickly are costs declining, and when will capable agentic tools be effectively free (or included in institutional site licenses)?
- Should universities and departments negotiate institutional subscriptions for AI tools, similar to existing licenses for Stata, MATLAB, or journal access?
- How should the cost of AI tool usage be allocated in co-authored projects -- is it a shared research expense, like data access fees?
- Does the cost differential between tools create a meaningful research quality gap between well-funded and under-funded researchers? If so, is this a problem the profession should address?
- How should researchers account for AI costs in replication packages -- should the cost of reproducing AI-assisted analysis be documented?

## Sources

- [[summaries/cost-reality.md|The Cost Reality]] -- Blattman's detailed cost breakdown and ROI framework
- [[summaries/ai-agents-econ-research.md|AI Agents for Economic Research]] -- Panjwani's budget-conscious recommendations
- [[summaries/llm-collaboration.md|LLM Collaboration]] -- Korinek's documentation of macro cost trends
- [[summaries/train-left-station.md|The Train Has Left the Station]] -- Energy consumption estimates
- [[summaries/daaf-framework.md|DAAF Framework]] -- Open-source alternative for cost-conscious researchers
