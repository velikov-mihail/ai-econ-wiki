---
title: "Claude Container: A Complete Beginner's Guide"
tags: [summary, foundations-setup, docker, safety, sandboxing]
sources:
  - "[[raw/articles/claude-containerdocsgetting-started.md at master.md]]"
date_updated: 2026-04-05
date_published: 2026-03
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale School of Management), via GitHub
- **Original**: [https://github.com/paulgp/claude-container/blob/master/docs/getting-started.md](https://github.com/paulgp/claude-container/blob/master/docs/getting-started.md)

- **Key Ideas**
  - Claude Container wraps Docker to give Claude Code an isolated Linux environment where it can run with full permissions (YOLO mode) without risking the host machine.
  - The project uses Colima (a free Docker alternative to Docker Desktop), a Justfile for simple commands (`just create`, `just claude`, `just destroy`), and bind mounts to share a project folder between host and container.
  - Key safety concept: the container is disposable but the shared project folder (`projects/<name>/`) is permanent and survives container destruction.
  - The guide covers 12 academic research use cases: data analysis, statistical modeling, literature review, web scraping, reproducible environments, teaching, database work, simulation, multi-language projects, and safe experimentation.
  - Authentication supports both Claude subscription (Pro/Max login) and API key approaches, with clear instructions for each.

- **Summary**

This is a comprehensive beginner's guide to Goldsmith-Pinkham's `claude-container` project, which provides a Docker-based sandbox for running Claude Code safely. The guide is written for researchers with no Docker or containerization experience, explaining every concept (containers, images, bind mounts, YOLO mode) in plain English with analogies.

The workflow is straightforward: install Colima and Docker via `just setup`, build the container image with `just build`, create a project container with `just create my-project`, and launch Claude Code inside it with `just claude my-project`. The container comes pre-installed with Python 3, R, Node.js 22, DuckDB, git, and build tools. Files created inside the container at `/workspace` appear on the host at `projects/<name>/`, providing seamless data exchange.

The guide is particularly valuable for its 12 detailed academic use cases, each with example prompts: from "explore the CSV files and create summary statistics" to "build a Schelling segregation simulation across a parameter grid." The emphasis throughout is that containers eliminate the risk of Claude accidentally modifying or deleting files on the researcher's actual machine, making full-autonomy (YOLO) mode safe for complex tasks.

- **Relevance to Economics Research**

Containers solve a real barrier to adoption: many researchers hesitate to give Claude Code full system access, especially on machines with important data. This guide makes sandboxing accessible to non-technical users, which is critical for broader faculty adoption. The pre-installed stack (Python, R, DuckDB) covers the standard economics research toolkit, and the reproducibility benefits --- recreating exact environments for coauthors or replication packages --- align with growing expectations in empirical economics.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/data-privacy]]
  - [[concepts/ide-and-terminal]]
  - [[concepts/reproducibility-transparency]]

- **Related Summaries**
  - [[summaries/getting-started-researchers]]
  - [[summaries/privacy-setup]]
  - [[summaries/install-mac]]
  - [[summaries/getting-started-economists]]
