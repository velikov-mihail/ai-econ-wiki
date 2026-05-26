---
title: "Permissions & OpenClaw: Claude Code for Economists (Markus Academy 162-7)"
tags: [summary, foundations-setup, claude-code, sandboxing, autonomous-agents]
sources:
  - "[[raw/articles/Permissions & OpenClaw Claude Code for Economists w P. Goldsmith-Pinkham  Markus Academy  162-7.md]]"
date_updated: 2026-05-26
date_published: 2026-05-25
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM, NBER), Markus Academy Ep. 162-7 (7th of 8 in mini-series)
- **Original**: [https://www.youtube.com/watch?v=8Jnx5rL_Gfk](https://www.youtube.com/watch?v=8Jnx5rL_Gfk)

- **Key Ideas**
  - **Two dimensions of permissions**: (1) *folder access* — what files the agent can read, write, or execute (including "the internet as a folder"); (2) *tool access* — what tools the agent can call. Both compose: powerful agents = lots of folders × lots of tools.
  - **Three permission modes**: *manual* (approve every action), *auto* (Claude Code's default — Anthropic-trained on which actions need confirmation, e.g., overwrite/delete), and *YOLO / `--dangerously-skip-permissions`* (fully autonomous). Manual mode gives a "false sense of security" because users start saying yes reflexively; the real choice is *ex ante* care vs. *interim* care.
  - **Mario Zechner's principle** (quoted): "As soon as an agent can write code and run code, it's pretty much game over… if it has access to tools that can read private data and make network requests, you're playing whack-a-mole." → Don't rely on per-action confirmations as security; design the worst-case scenario to be survivable.
  - **Persistence of agents**: in earlier episodes, Claude was denied the `ls` tool and immediately tried `find` to accomplish the same goal — "like a very clever child." Permission-by-permission denial is not a real boundary.
  - **Sandboxing with containers**: a Docker container is a virtual machine that sees only the folders and tools you grant it; inside the container it cannot mount or unmount anything. Build a Docker file once (Goldsmith-Pinkham's includes Python, R, LaTeX, Node, DuckDB, `just`, `uv`, Claude Code), then spin up throwaway containers per project. Once configured, a single CLI wrapper (his `ccr` / claude code runner) launches an isolated Claude session bound to a chosen folder.
  - **Lighter-weight alternatives to Docker** for the same idea: **Safe House** (Mac, free) enforces folder restrictions at the kernel level so the agent literally cannot delete files in protected folders even in YOLO mode. Also mentioned: Scode, No, dev containers. Cloud-side environments (Claude in the browser, Codex Cloud, Cowork) are *already* sandboxed by default.
  - **Data governance is separate from sandboxing**: a container limits what the agent can touch on your machine, but if the model sees PII and is a remote model, the data still leaves. Mitigations: OpenAI's privacy filter (block PII before sending), or run a local model (Llama, Chinese open-source models) on your own machine for sensitive data.
  - **OpenClaw and autonomous agents**: Goldsmith-Pinkham demos his own "Duncan Idaho" agent — Claude Code running in a persistent container, reachable via Telegram/WhatsApp, with mounted read-only access to project data, Dropbox, a paper pipeline (54,000 economics papers searchable in sub-second), and PhD teaching files. It is an RA that wakes itself up, takes notes, and runs cross-project queries while the researcher is away from the keyboard.
  - **Provider portability** is a deliberate stance: "you don't want to be subject to a monopolist." Goldsmith-Pinkham rotates across Claude Code, Codex, ChatGPT, and Gemini and recommends learning to move between ecosystems.

- **Summary**

This is the most operationally important episode in the Markus Academy 162 mini-series so far. The first half is a clean conceptual framework: agents are dangerous not because they talk but because they *act*, and the security model has to be designed *ex ante* (which folders, which tools, what's the worst case) rather than enforced *interim* via permission prompts. Goldsmith-Pinkham is explicit that manual mode and YOLO mode are theatrically opposite but practically converge — manual users become habituated to clicking yes. The real defense is container isolation.

The Docker demo is honest about complexity: Goldsmith-Pinkham walks through a real Dockerfile, builds the `econ_sandbox` image, launches a YOLO Claude session inside it, hits authentication friction (logging into Claude inside a container) and web-scraping friction (Princeton's site blocks bots), and pivots to a working example. The takeaway is not that any single demo worked end-to-end, but that the cost of a misbehaving agent inside `econ_sandbox` is bounded to the throwaway container. His `claude code runner` wrapper hides the Dockerfile complexity behind a single CLI command per project. For Mac users who want most of the benefit without Docker, Safe House is presented as the easiest on-ramp.

The "Duncan Idaho" portion is the most distinctive contribution. It demonstrates a long-running, container-isolated, persistent-memory agent that an academic can text via Telegram or Slack — accessible from a phone, with mounted read-only access to a curated pipeline of 54k economics papers and to project Dropbox folders, but no ability to modify the protected sources. It is, concretely, an always-on RA that can search the literature, draft replies, and run data analysis across multiple projects while preserving cross-project memory. The closing reflection on local models for sensitive data, and on rotating across providers to avoid lock-in, frames containerization as the prerequisite for autonomy rather than as a defensive afterthought.

- **Relevance to Economics Research**

For empirical economists, this is the closest the series gets to a deployable autonomous-RA recipe. The sandboxing pattern (read-only mount of raw data, writable scratch folder for outputs, no network unless explicitly granted) is exactly the discipline that protects WRDS extracts, restricted Census data, or any project where licensing limits redistribution. Goldsmith-Pinkham's Dockerfile choices (Python + R + LaTeX + DuckDB + `uv`) are a reasonable canonical stack for an asset-pricing or applied-micro project. The Duncan Idaho pattern — an agent with read-only access to a curated paper pipeline plus project Dropbox — is a working answer to "how do I make literature review and replication continuous rather than episodic." The data-governance caveat (sandboxing does not solve PII leakage to remote models) is a useful reminder that container isolation and model-side privacy filtering are independent layers.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/data-privacy]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/ai-agents]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/claude-container]]
  - [[summaries/getting-started-economists]]
  - [[summaries/data-analysis-economists]]
  - [[summaries/large-datasets-economists]]
  - [[summaries/web-scraping-economists]]
  - [[summaries/writing-thinking-markus-162-5]]
