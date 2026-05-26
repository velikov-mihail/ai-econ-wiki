---
title: "Permissions, Sandboxes, and Autonomous Agents (companion Substack post)"
tags: [summary, foundations-setup, claude-code, sandboxing, autonomous-agents]
sources:
  - "[[raw/articles/Permissions, Sandboxes, and Autonomous Agents.md]]"
date_updated: 2026-05-26
date_published: 2026-05-23
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM), Substack — companion to Markus Academy Ep. 162-7
- **Original**: [https://paulgp.substack.com/p/permissions-sandboxes-and-autonomous](https://paulgp.substack.com/p/permissions-sandboxes-and-autonomous)

- **Key Ideas**
  - Written companion to [[permissions-openclaw-markus-162-7|Markus Academy 162-7]] — same five-part structure, but tightened, with copy-pasteable Docker and `safehouse` commands and a much more explicit data-governance hierarchy.
  - **Two kinds of permission**: folder access (rwx on files; "the internet is a folder too") and tool access (`bash`, Python, `git`, package installs, browser tools, MCP, long-running jobs). Granting both turns a chat model into an agent.
  - **Three approval modes** are really three choices about *when* you do the thinking: *manual* (interim, every action), *auto* (ex ante + interim — Anthropic's classifier catches destructive operations), *YOLO / `--dangerously-skip-permissions`* (purely ex ante; design the environment so the worst case is survivable).
  - **The reflexive-`y` problem**: most academics already approve dozens of actions without reading them. Per-action prompts are "friction without protection." The real safety lever is *ex ante* environment design, not interim confirmations.
  - **The real question is the environment, not the model**: which folders are mounted, what tools are installed, are credentials in reach, is the internet reachable, what's the worst case if you're wrong? An unsandboxed `claude --dangerously-skip-permissions` in the home directory runs with `~/.ssh`, every API key, and every repo you've cloned in scope.
  - **Container = sandbox**: a virtual machine that sees only what you mount in. The agent cannot mount or unmount anything from inside — boundary is enforced by the host. Choices: Docker / devcontainers; `agent-safehouse` (Mac, kernel-enforced, brew-installable); `scode`; `nono.sh`; the author's own `claude-container` wrapper; remote VMs / CI runners. The brand doesn't matter — the *boundary* does.
  - **Docker recipe** (verbatim from the post): `econ-sandbox` image based on `rocker/tidyverse` with Python, R, LaTeX, Node, DuckDB, `just`, `uv`, and Claude Code. `docker run` mounts only the project folder and `~/.claude`, drops Linux capabilities, disables new privileges, and launches Claude in YOLO mode. The author's `ccr` (claude-code-runner) wrapper packages this so per-project use is one command.
  - **`agent-safehouse` for Mac**: `brew install eugene1g/safehouse/agent-safehouse`, then `safehouse claude --dangerously-skip-permissions`. SSH keys and other-project folders return "Operation not permitted" at the kernel. Selective read-only mounts widen the view: `safehouse --add-dirs-ro=…`.
  - **Data exposure is a separate problem from sandboxing**: a container limits *what the agent can do*, not *what it can see* once you mount data. PII still leaves your machine when a remote model reads it. Three privacy tiers: (1) Anthropic API calls are contractually private (vs. Pro/Max subscriptions, which may be trained on); (2) AWS Bedrock runs Anthropic models without sending data to Anthropic and can be HIPAA-compliant; (3) for truly sensitive data, run a local model. Plus optional preprocessing with OpenAI's privacy filter to strip names/emails/addresses.
  - **Recommended hierarchy** (weakest → strongest): minimize mounts → sandbox → filter PII → use a local model for sensitive data.
  - **Duncan Idaho** is the author's personal autonomous-agent stack: Claude Code in a persistent Docker container, talked to via Telegram and tied into Slack for research-team work, with read-only mounts of a project database and the author's working-paper pipeline plus a writable Dropbox folder. Apoorva Lal's "krabs-the-clawdbot" walkthrough is cited as a step-by-step recipe for replicating this.
  - **Cowork and cloud tools are *already* sandboxed by default** — same design, less control. "I can't do that here" messages from Cowork, Claude on the web, ChatGPT, or Gemini are the visible boundary of someone else's container.

- **Summary**

This Substack post is the written, more shareable form of the Markus Academy 162-7 episode and lands the same conceptual points more crisply. The core argument — *interim* per-action confirmations are theater; the real lever is *ex ante* environment design — is the load-bearing claim of the entire series and is the post's tightest formulation of it. The author is also more explicit here than in the video about *why* this matters: an unsandboxed YOLO Claude session running in the user's home directory has, by default, read access to SSH keys, API tokens, and every cloned repo. Whether autonomy is acceptable is a question about the environment, not the model.

Three things make this companion post worth its own summary even if you've watched the video. First, the Dockerfile + `docker run` block is verbatim and copy-pasteable, including the security flags (`--cap-drop=ALL`, `--security-opt=no-new-privileges`) and the mount of `~/.claude` for auth. Second, the data-governance section is more developed than in the talk: the explicit API-vs-subscription distinction (paid API calls are contractually not trained on; Pro/Max subscriptions may be), the Bedrock-as-HIPAA-pathway note, and the four-tier privacy hierarchy are all written-form only. Third, the Duncan Idaho section is no longer a live demo but a clean architectural sketch: container + Telegram + Slack + mounted database (read-only) + mounted Dropbox + paper pipeline + teaching files. The pointer to Apoorva Lal's "krabs-the-clawdbot" walkthrough turns this into a reproducible recipe.

The closing footnote on Duncan Idaho — *ghola* persistence in the Dune universe as a metaphor for an agent re-instantiated session after session with preserved memory — is a quietly excellent piece of agent-design framing.

- **Relevance to Economics Research**

For empirical economists this is the canonical defensive checklist: minimize mounts, sandbox the environment, filter PII, and for restricted data (Census micro, HIPAA-covered health data, proprietary trading data) use a local model — not a remote API behind a sandbox. The Bedrock pathway is a genuinely useful concrete option for academic researchers who need Anthropic-quality models on data that cannot leave a HIPAA-compliant boundary. The API-vs-subscription distinction is non-obvious and matters for any researcher who uses Claude on identifiable data: API calls (per-token) have a contractual no-training guarantee that Pro/Max ($20/100/200 per month) subscriptions do not. For coauthors building shared agent infrastructure, the Slack-bot pattern (Duncan + Slack) is a concrete recipe for giving an entire research team access to an agent that has read-only access to project data and writable access to a shared output folder.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/data-privacy]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/ai-agents]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/permissions-openclaw-markus-162-7]]
  - [[summaries/claude-container]]
  - [[summaries/writing-thinking-ai-assistance]]
  - [[summaries/writing-thinking-markus-162-5]]
  - [[summaries/getting-started-economists]]
