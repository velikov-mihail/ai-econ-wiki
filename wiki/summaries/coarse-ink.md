---
title: "coarse.ink: Open-Source AI Academic Paper Reviewer"
tags: [summary, ai-tools]
sources:
  - "[[raw/articles/coarse.ink.md]]"
date_updated: 2026-04-25
date_published: 2026-04-16
---

- **Author/Source**: David Van Dijcke, GitHub repo (Davidvandijcke/coarse), v1.3.0
- **Original**: [https://github.com/Davidvandijcke/coarse](https://github.com/Davidvandijcke/coarse)
- **Web interface**: [https://coarse.vercel.app/](https://coarse.vercel.app/)

- **Key Ideas**
  - Free, open-source AI paper reviewer (MIT-licensed, BYO API key) positioned as outperforming popular paid AI reviewers --- typically **under $2 per review**, with a default $10/review hard spending cap.
  - One-line install: `uvx coarse-ink review paper.pdf --api-key sk-or-v1-YOUR_KEY` --- the review lands as `paper_review.md` in the working directory. Permanent install via `uv tool install coarse-ink` or `pip install coarse-ink`.
  - Supported formats: PDF, TXT, Markdown, LaTeX, DOCX, HTML, EPUB. PDFs use **Mistral OCR** (routed through OpenRouter's file-parser plugin); other formats use Docling with lightweight fallbacks.
  - **Pipeline** (10 stages): OCR/extraction → vision-LLM spot-check (auto-triggered on garbled text) → structure analysis (sections, math content, domain) → domain calibration + Perplexity Sonar Pro lit search in parallel → overview agent (single macro pass) → completeness agent (structural gaps) → parallel section agents + adversarial proof verification for math-heavy sections → cross-section synthesis (results vs. discussion consistency) → editorial filter (deduplication, contradiction, quality) → quote verification (fuzzy-match against source, stricter for math) → final markdown render.
  - **Model selection** is fully flexible via litellm: any model with a string like `openai/gpt-4o`, `anthropic/claude-sonnet-4-6`, `gemini/gemini-3-flash-preview`. Default is `qwen/qwen3.5-plus-02-15` via OpenRouter. `--cheap` auto-selects the cheapest model the user has a key for.
  - **API keys:** only `OPENROUTER_API_KEY` is needed for everything (review agents, lit search, OCR). Direct-provider keys (OpenAI, Anthropic, Google, Mistral, Groq, Together, Cohere, Azure) are optional for lower latency / separate billing.
  - **Output:** structured markdown with an "Overall Feedback" section (4--6 macro issues with titles and body paragraphs) and a "Detailed Comments" section (20+ numbered comments, each with a verbatim paper quote and actionable feedback).
  - Python API exposes `review_paper(pdf_path, model)` returning `(Review, markdown, PaperText)` for programmatic use.
  - **Cost realism:** the README warns that estimates include a 30% buffer but are not a ceiling --- math-heavy papers with deep proof-verification chains can run materially over.

- **Summary**

coarse.ink is the open-source counterpart to [[summaries/refine-ink-golub|refine.ink]] (Calvó López & Golub) --- both are agentic paper-reviewing pipelines, but the design philosophies are different. refine.ink is a hosted product designed to give referee-quality feedback on long economics papers; coarse is a CLI tool that runs the pipeline locally, lets the user pick the model, and pushes the per-review cost down to under $2 by routing through cheap models (OpenRouter + Qwen by default) and aggressive editorial deduplication.

The pipeline architecture is more transparent than refine's: every stage is named and documented in the README, and the editorial filter is the explicit quality gate that decides which detailed comments survive to the final review. The math-handling deserves attention --- math-content sections trigger an *adversarial proof check* and tighter quote-verification thresholds, both of which exist because hallucinated math criticism is the most likely failure mode for general-purpose LLMs reviewing technical papers.

The choice to run lit search through Perplexity Sonar Pro (with arXiv fallback) is interesting: rather than asking the LLM to recall related work, the pipeline does a real web search and feeds those results back into the section agents. This is the same pattern that makes refine.ink reliable on long papers and that Hall noted in [[summaries/ai-10x-research]] for surfacing referee-quality criticism.

- **Relevance to Economics Research**

Useful as a low-cost referee for working drafts and as a baseline for anyone wanting to roll their own reviewing pipeline. The under-$2 price point makes it cheap enough to run on every revision, not just at submission, which changes how it gets used --- closer to a CI step than to a one-time external review. The Python API also makes it embeddable in research workflows: a coauthor could include `review_paper()` in a pre-commit hook on the LaTeX repo and get a fresh review every time the manuscript is updated.

For users skeptical of "AI-as-referee" given the failure modes Cunningham documents in [[summaries/cc-series-44-four-criteria-referee]], the explicit pipeline stages and the quote-verification step are the right things to look at: this isn't an LLM "vibing" a referee report; it's a structured pipeline with verifiable output. Doesn't mean the criticism is right, but the chain of reasoning is auditable.

- **Related Concepts**
  - [[concepts/ai-peer-review]]
  - [[concepts/ai-research-tools]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/refine-ink-golub]]
  - [[summaries/cc-series-44-four-criteria-referee]]
  - [[summaries/ai-10x-research]]
  - [[summaries/prompting-insights-golub]]
