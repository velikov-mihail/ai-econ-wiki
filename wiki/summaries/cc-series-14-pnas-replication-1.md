---
title: "Claude Code Part 14: I Asked Claude to Replicate a PNAS Paper Using OpenAI's Batch API (Part 1)"
tags: [summary, data-analysis, text-classification, openai-batch-api, replication, referee-2, nlp]
sources:
  - "[[raw/articles/Claude Code Part 13 I Asked Claude to Replicate a PNAS Paper Using OpenAI's Batch API. Here's What Happened (Part 1).md]]"
date_updated: 2026-04-05
date_published: 2026-02-05
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-part-13-i-asked-claude](https://causalinf.substack.com/p/claude-code-part-13-i-asked-claude)

- **Key Ideas**
  - Replicating Card et al. (PNAS 2022) on 140 years of immigration rhetoric using gpt-4o-mini zero-shot classification instead of a fine-tuned RoBERTa model
  - Claude Code autonomously found and downloaded the 1.39 GB replication package from GitHub, organized the project directory, and wrote modular Python scripts
  - 304,995 speech segments split into 39 batch files of 8,000 records each, submitted via OpenAI's Batch API at an estimated cost of $10.99
  - The classification prompt raised a methodological concern: listing specific keywords (e.g., "flood," "invasion") risks biasing the LLM toward pattern-matching rather than semantic understanding
  - Referee 2 audited the code before submission and caught label normalization edge cases, missing Cohen's Kappa metric, need for temporal stratification, and the prompt design concern
  - Plan mode used to structure the workflow backwards from desired output; defensive programming with dry-run flag and confirmation prompt before spending money

- **Summary**

Cunningham attempts something he genuinely did not know how to do: use Claude Code to orchestrate a large-scale text classification replication of Card et al.'s PNAS paper on immigration rhetoric in US political speeches. The original paper used a RoBERTa model fine-tuned on 7,626 human annotations to classify ~305,000 speech segments as PRO-IMMIGRATION, ANTI-IMMIGRATION, or NEUTRAL. Cunningham's approach uses gpt-4o-mini via OpenAI's Batch API for zero-shot classification at a fraction of the cost.

Claude Code handled the entire pipeline: finding and downloading the replication package, organizing a self-contained project folder with modular scripts (one per task), preparing JSONL batch files, and building in safety features like dry-run flags and explicit confirmation prompts. The classification prompt was deliberately detailed but raised concerns about keyword-based biasing. Before submitting the $11 batch job, Cunningham ran the Referee 2 protocol, which caught several issues including a string-matching bug where "NOT PRO-IMMIGRATION" would be misclassified as PRO (because "PRO" appears in the string), the absence of Cohen's Kappa for chance-corrected agreement, and the need for temporal stratification of results.

The post ends with the batch job submitted and results pending, setting up Part 2. The total setup time was approximately one hour of dictation to Claude Code.

- **Relevance to Economics Research**

This is a direct demonstration of how economists can use AI agents to conduct large-scale computational text analysis without machine learning expertise. The $11 cost and one-hour setup time dramatically lower the barrier to NLP-based research. The Referee 2 audit before running an expensive job illustrates a practical quality-control workflow. The methodological concerns raised (prompt bias, temporal heterogeneity, chance agreement correction) are exactly the issues a careful empirical researcher would need to address.

- **Related Concepts**
  - [[concepts/text-as-data]]
  - [[concepts/agentic-workflows]]
  - [[concepts/reproducibility-transparency]]
  - [[concepts/ai-agents]]

- **Related Summaries**
  - [[summaries/cc-series-15-pnas-replication-2]]
  - [[summaries/cc-series-12-empirical-research]]
  - [[summaries/cc-series-13-skills-split-pdf]]
