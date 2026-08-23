---
title: "AI Engineering Skills Map: Building and Deploying AI Applications"
tags: [summary, foundations-setup, ai-skills, ai-agents, human-capital]
sources:
  - "[[raw/Clippings/AI Engineering Skills Map Building and Deploying AI Applications.md]]"
date_updated: 2026-08-23
date_published: 2026-08-21
---

- **Author/Source**: Andrew Ng (DeepLearning.AI), via X
- **Original**: [https://x.com/AndrewYNg/status/2090840747738374568](https://x.com/AndrewYNg/status/2090840747738374568)

- **Key Ideas**
  - Ng's AI Engineering Skills Map has four top-level skills: (i) building and deploying AI applications, (ii) software engineering fundamentals, (iii) using coding agents, and (iv) shaping the build. This post fleshes out the first.
  - The defining difference between AI and non-AI software is **output unpredictability**. You cannot know in advance what an LLM will emit, so building AI systems is inherently iterative rather than plannable — build, examine, decide what to try next.
  - The payoff of that iterative skill: "create reliable software systems based on unreliable AI components."
  - Six sub-skills: **LLM foundations** (tokenization, context-window tradeoffs, caching, knowledge cutoffs, reasoning effort, sampling parameters, tool calling, when to fine-tune or self-host); **grounding models with data** (RAG is only the earliest technique — also knowledge graphs, semantic layers over structured data, prompt-vs-retrieve decisions, document-to-LLM-input pipelines); **building agentic systems** (workflow vs. harness, chaining vs. parallelizing, tool/MCP/CLI/sandbox choices, memory architecture, long-session context management, when multi-agent beats single-agent, plus guardrails against adversarial inputs and data exfiltration); **evaluation-driven development**; **operating in production** (observability, drift detection, regression testing, cost/latency optimization); and **machine learning foundations**.
  - Ng singles out **evals and error analysis** as "the most important trait that distinguishes someone great at building AI systems" — and admits it is tricky to master because the right approach varies by project and by project stage.
  - Building good evals is itself a deep technical skill: reading traces, exploratory analysis of outputs, choosing between deterministic checks, LLM-as-a-judge, and human-in-the-loop — and then evaluating your evals.
  - ML foundations still matter because bias/variance, error analysis, and data engineering are "core mental frameworks for navigating how to work with systems with uncertain output."
  - The map was constructed empirically — from a large number of job postings, structured expert interviews, and survey responses.

- **Summary**

Andrew Ng lays out the sub-skills that constitute the first pillar of his AI Engineering Skills Map: building and deploying AI applications. His organizing insight is that AI software differs from ordinary software in one crucial way — its outputs are not predictable in advance. That unpredictability propagates through the entire development process, making the work iterative rather than plannable. The skilled AI engineer, in Ng's telling, is the one who can repeatedly build a piece of the system, inspect what it actually does, and make a good decision about the next step. That capacity is what allows reliable systems to be assembled out of unreliable components.

The six sub-skills range from the fairly technical (tokenization, sampling parameters, fine-tuning, distillation) to the architectural (when to chain LLM calls in a fixed workflow versus hand control to an agent harness that decides its own next step; when a task genuinely requires multi-agent orchestration). Grounding gets substantial attention: Ng frames vector-search RAG as an early technique in a menu that has grown to include knowledge graphs and semantic layers over structured records, and stresses that the real decisions are what to put in the prompt versus what to let the model retrieve on demand, and how to keep the underlying data clean and fresh.

The strongest claim in the piece concerns evaluation. Ng says the disciplined evals/error-analysis loop is what separates the great from the merely competent, because it is what turns development from a random walk into systematic progress. He notes it is a hard skill precisely because it is not transferable off the shelf — what to measure depends on the project, the stage, and business context, and the evals themselves need to be evaluated and evolved. The post closes on production concerns (observability, drift, prompt-injection incidents, regression testing calibrated to the risk of a mistake, cost and latency optimization) and on machine learning fundamentals, which Ng argues every good LLM builder he knows possesses at some depth.

- **Relevance to Economics Research**

Most economists using AI sit on the *consumption* side — using Claude Code, ChatGPT, or Codex as tools. But a growing number are building things: RA-replacement pipelines, automated literature screeners, text-as-data classifiers, agentic replication harnesses. The moment a researcher moves from using an agent to building one, Ng's map describes the skill gap they are about to hit.

Two items translate especially directly. First, **evaluation-driven development** is the discipline economists already know under other names — validation, out-of-sample testing, measurement error — and Ng's insistence that it is the differentiating skill should read as familiar. An LLM-based classifier applied to 50,000 filings is a measurement instrument, and it needs the same scrutiny an economist would apply to any constructed variable: hand-coded validation samples, inter-rater reliability against the LLM, sensitivity to prompt specification. The "evaluate your evals" point maps onto the question of whether a hand-coded gold standard is itself reliable.

Second, the **grounding** discussion is the technical backbone of every "point the AI at my literature/data" workflow. Understanding that RAG is one option among several — and that the prompt-versus-retrieve tradeoff is a design decision, not a default — is what separates a working literature pipeline from one that silently drops relevant papers.

The framing of unpredictability as the core difficulty also connects to the reproducibility problem: if outputs are not deterministic, the standard of "reproducible" for AI-assisted empirical work has to be re-specified, which is exactly the debate running through [[concepts/reproducibility-transparency]].

- **Related Concepts**
  - [[concepts/ai-skills]]
  - [[concepts/ai-agents]]
  - [[concepts/agentic-workflows]]
  - [[concepts/retrieval-augmented-generation]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/context-management]]
  - [[concepts/human-capital]]
  - [[concepts/reproducibility-transparency]]

- **Related Summaries**
  - [[summaries/architecture-patterns]]
  - [[summaries/skill-library]]
  - [[summaries/agents-vs-skills]]
  - [[summaries/ai-agents-econ-research]]
