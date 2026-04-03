---
title: "Prompt Engineering"
tags: [concept, prompt-engineering, communication, workflows]
sources:
  - "[[summaries/prompt-engineering.md]]"
  - "[[summaries/prompting-insights-golub.md]]"
  - "[[summaries/prompt-plan-review-revise.md]]"
  - "[[summaries/patterns.md]]"
  - "[[summaries/your-claude-md.md]]"
date_updated: 2026-04-03
---

## Definition

**Prompt engineering** is the practice of crafting clear, structured instructions that guide an AI model toward high-quality output. It is a learnable, repeatable method rather than a technical skill -- the core argument across sources is that most poor AI interactions stem from unclear communication, not model limitations. A well-structured prompt provides context, specifies the task precisely, constrains the output format, and anticipates common failure modes.

The gap between mediocre and great AI output is almost always the prompt, not the model or subscription tier. As Blattman puts it, prompt engineering is about matching the precision of your request to the stakes of the task -- light prompts for routine work, deep prompts with verification for high-stakes analysis.

## Context & Background

Prompt engineering has evolved from a niche technical skill to a core competency for any knowledge worker using AI tools. In the chatbot era, prompting meant typing a question. In the agentic era, prompting encompasses structured multi-section instructions, behavioral constraints given proactively, persona assignments, and meta-prompting (using AI to structure your own prompts). The shift reflects a deeper change: AI interactions are becoming more like project management than conversation.

For economics researchers, prompt engineering intersects with existing skills in clear writing and structured thinking. The six-part prompt structure (Role, Context, Task, Constraints, Output Format, Bookend) maps naturally onto tasks like drafting methodology sections, generating referee-style feedback, and building pre-analysis plans. The challenge is calibrating effort: over-engineering routine tasks wastes tokens, while under-engineering high-stakes tasks produces unreliable output.

## Key Perspectives

**Blattman** ([[summaries/prompt-engineering.md]]) presents the foundational framework: a six-part prompt anatomy (Role, Context, Task, Constraints, Output Format, Bookend) with a three-tier effort calibration (light, standard, deep). Key techniques include XML-style tags to separate instructions from pasted content, prompt chaining for multi-step work, and strategic use of examples (try without them first). Common anti-patterns include vague thoroughness language ("be comprehensive"), over-prompting in all-caps, and failing to give the AI permission to push back. Blattman also recommends meta-prompting: creating an AI project whose job is to restructure messy input into clean prompts.

**Golub** ([[summaries/prompting-insights-golub.md]]) provides the theorist's perspective. His central insight is that effective prompting is fundamentally about **micromanagement** -- providing the model with context it lacks and constraining behavior in advance. He emphasizes four key techniques: role-playing ("you are a senior probabilist writing for Econometrica"), step-by-step decomposition, avoiding argument with the model (start new context instead), and handoff reports to transfer context between chats. His most distinctive warning: wrong information in a chat **poisons the context** and causes the model to reconcile errors with everything that follows. The solution is to start fresh chats for focused tasks rather than correcting inline.

**Blattman (PPRR)** ([[summaries/prompt-plan-review-revise.md]]) operationalizes prompting within a repeatable workflow. The `/prompt` skill takes rough, stream-of-consciousness input and reformats it into a structured prompt, lowering the barrier for users who find formal prompting unintuitive. The persona technique assigns multiple expert perspectives to debate and converge before committing to a plan.

**Blattman (Patterns)** ([[summaries/patterns.md]]) catalogs structural and behavioral patterns that extend prompting into reusable tools. The Critic Stance pattern explicitly shifts Claude from collaborator to critic, counteracting its default tendency toward agreement. Depth Calibration adjusts thoroughness to task stakes. Domain Auto-Detection infers the right behavior from content signals rather than requiring explicit flags.

## Practical Implications

- **Match effort to stakes**: Use light prompts for email drafts and quick lookups. Use standard prompts (with assumptions and rationale) for data analysis. Use deep prompts (with verification steps) for econometric methodology and identification strategy.
- **Give behavioral instructions proactively**: Tell the model to be concise, follow existing notation, and not rewrite from scratch *before* it generates output -- not after.
- **Use the six-part structure for high-stakes work**: Role, Context, Task, Constraints, Output Format, and Bookend (restating the key instruction at the end for long prompts).
- **Do not argue with the model**: If it produces a wrong result, start a fresh chat with correct context rather than trying to fix it inline. Poisoned context degrades all subsequent output.
- **Separate instructions from content**: Use XML-style tags (`<paper>`, `<data>`, `<instructions>`) to prevent the AI from confusing your meta-instructions with the material being analyzed.
- **Break complex tasks into chains**: Course-correct between steps rather than getting mediocre output across all subtasks at once.
- **Give the AI permission to disagree**: Explicitly state "push back if you think this approach is wrong" to counteract sycophancy.

## Open Questions

- As models improve, will detailed prompt engineering become less necessary, or will it remain important because the ceiling of what can be achieved also rises?
- How should prompt engineering be taught to PhD students -- as a separate skill or integrated into methods courses?
- Is there a point of diminishing returns for prompt complexity, beyond which additional structure degrades rather than improves output?
- How do prompting best practices differ across models (Claude, GPT, Gemini), and are they converging?

## Sources

- [[summaries/prompt-engineering.md]] -- Blattman's six-part prompt anatomy and three-tier effort framework
- [[summaries/prompting-insights-golub.md]] -- Golub on micromanagement, poisoned context, and handoff reports
- [[summaries/prompt-plan-review-revise.md]] -- The PPRR loop and the `/prompt` skill for structured prompting
- [[summaries/patterns.md]] -- Design patterns including Critic Stance and Depth Calibration
- [[summaries/your-claude-md.md]] -- CLAUDE.md as persistent prompt context across sessions
