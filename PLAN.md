# Implementation Plan: AI-in-Economics Wiki

## Progress (as of 2026-04-03)

- **Phase 0**: DONE — Git repo initialized, .gitignore, MkDocs config, requirements.txt, GitHub Actions deploy workflow, raw articles deduplicated (91 unique articles remain)
- **Phase 1**: DONE — Wiki scaffolding: index files, 10 category landing pages
- **Phase 2**: DONE — All 91 articles + 5 papers summarized (86 individual summary pages across 10 categories)
- **Phase 3**: DONE — 15 cross-cutting concept pages created
- **Phase 4**: DONE — Category map (Mermaid), author index, source timeline
- **Phase 5**: DONE — Validation tools (validate_frontmatter.py, build_index.py, find_duplicates.py), fixed 400 broken wikilinks (backslash escapes, wiki/ prefixes, 109 missing concepts consolidated into 49 new pages + redirects), expanded to 64 total concept pages
- **Phase 6**: DONE — Cross-link pass (0 orphans, all concepts ≥2 summary links), MkDocs strict build passes, GitHub remote created (private), pushed to main

**All phases complete.** Pending: enable GitHub Pages (Settings → Pages → Source: GitHub Actions), then optionally make repo public.

---

## Phase 7: Source URLs & Remaining Polish

### 7.1 — Source URLs (IN PROGRESS)
47 of ~96 summaries now have an `**Original**:` link to the source article. Remaining work:
- Add source URLs to the ~44 summaries from claudeblattman.com that use relative raw refs (e.g., building-skills, chatbot-essentials, etc.) — their URLs need to be constructed from the site structure
- Add source URLs to the 5 paper summaries (korinek-2023, panjwani-slides, spina-paper, baylor-ai-taskforce) — use DOIs or repo URLs
- Fix the 1 missing raw ref: `getting-started-researchers` → find the correct raw article match

### 7.2 — Remaining summaries without source URLs
The tool `tools/_add_source_urls.py` was used (and removed). To find remaining gaps:
```bash
cd wiki/summaries && grep -rL "Original" *.md | grep -v index | grep -v foundations-setup | grep -v prompt-engineering | grep -v ai-agents | grep -v claude-code-skills | grep -v data-analysis | grep -v academic-research | grep -v finance-econometrics | grep -v ai-tools | grep -v institutional-societal | grep -v professional-productivity
```

### 7.3 — Enable GitHub Pages
1. Go to repo Settings → Pages → Source: **GitHub Actions**
2. Verify the site builds and deploys at https://velikov-mihail.github.io/ai-econ-wiki/
3. Decide whether to make repo public

### 7.4 — Future: add new articles
- User plans to add new Substack articles to raw/articles/ (pending author confirmation)
- When added: create summaries, update category pages, update indexes, link to concepts

---

## Context

You have ~97 markdown web clippings and 6 papers in `raw/` covering AI workflows for economics/social science research. The goal is to compile these into a structured wiki in `wiki/`, publish it online via MkDocs Material + GitHub Pages, and maintain it as a living resource for academic researchers. The wiki follows Karpathy's "LLM knowledge base" pattern: raw sources are compiled by the LLM into interlinked markdown, viewable in Obsidian locally and published online.

---

## Phase 0: Infrastructure Setup

### 0.1 — Git init + `.gitignore`
- Initialize git repo
- Create `.gitignore` excluding:
  - `raw/` (all raw source data — clippings, papers, images — kept local/Dropbox only)
  - `.obsidian/workspace.json`, `.obsidian/cache/`
  - `site/`, `output/`, `__pycache__/`, `.DS_Store`, `Thumbs.db`
- Initial commit

### 0.2 — Deduplicate raw articles
- 6 articles have " 1" suffix duplicates with matching counterparts → delete the " 1" versions
- 2 articles have " 1" suffix but no counterpart → rename to remove suffix
- Net result: ~91 unique articles

### 0.3 — MkDocs Material config
Create `mkdocs.yml` at repo root:
- `docs_dir: .` (so MkDocs sees both `wiki/` and `raw/`)
- Theme: Material with navigation tabs, search, dark/light toggle
- Plugins: `search`, `roamlinks` (converts `[[wikilinks]]` to standard links at build time), `tags`
- Extensions: admonition, superfences (for Mermaid diagrams), footnotes, toc with permalinks
- Nav structure mapping to wiki/ subdirectories

### 0.4 — `requirements.txt`
```
mkdocs-material>=9.5
mkdocs-roamlinks-plugin>=0.3
```

### 0.5 — GitHub Actions deploy
Create `.github/workflows/deploy.yml`:
- Trigger on push to `main`
- Build with `mkdocs build --strict`
- Deploy to GitHub Pages via `actions/deploy-pages`

### 0.6 — Initial commit with infrastructure

---

## Phase 1: Scaffolding — Index Files and Templates

### Files to create:

1. **`wiki/index.md`** — Master TOC with category table, brief descriptions, source counts
2. **`wiki/summaries/index.md`** — Lists all summaries organized by category
3. **`wiki/concepts/index.md`** — Lists all concept pages (initially empty, populated incrementally)
4. **`wiki/visualizations/index.md`** — Landing page for diagrams/visualizations
5. **10 category landing pages** in `wiki/summaries/` (one per category, see below)

### Summary template (each file in `wiki/summaries/`):
```yaml
---
title: "<Article Title>"
tags: [summary, <category-slug>]
sources:
  - "[[raw/articles/<filename>.md]]"
date_updated: YYYY-MM-DD
---
```
Followed by: Author/date/source link, Key Ideas (3-7 bullets), Summary (2-4 paragraphs), Relevance to Economics Research, Related Concepts (wikilinks), Related Summaries (wikilinks).

### Concept page template (each file in `wiki/concepts/`):
```yaml
---
title: "<Concept Name>"
tags: [concept, <category-slug>]
sources:
  - "[[wiki/summaries/<source1>.md]]"
date_updated: YYYY-MM-DD
---
```
Followed by: Definition, Context & Background, Key Perspectives (by source), Practical Implications, Open Questions, Sources.

---

## Phase 2: Incremental Category Processing

Process in this order (foundational → technical → applied → contextual):

### Batch 1 — Foundational
1. **Foundations & Setup** (~11 articles): Install guides, VS Code, Privacy, Getting Started, MCP Setup, Starter Templates, Chatbot Essentials, Claude Code for Newbies
2. **Prompt Engineering & Workflow Architecture** (~8 articles): Prompt Engineering, Prompt-Plan-Review-Revise, Architecture Patterns, Patterns, Workflow Overview, Your CLAUDE.md, AI Project Folders

### Batch 2 — Core Technical
3. **AI Agents & Agentic AI** (~7 articles): Agentic Everything, AI Agents for Econ Research (VoxDev), Agents vs Skills, Learn About AI Coding Agents, Claude Code and What Comes Next
4. **Claude Code Skills & Advanced Workflows** (~8 articles): Building Skills, Skill Library, Build Your Own, Continuous Improvement, Compilation & Review, DAAF framework

### Batch 3 — Domain Applications
5. **Data Analysis & Web Scraping** (~5 articles): Data Analysis (Goldsmith-Pinkham), Web Scraping, EDGAR Filings, WRDS tools, Empty Folder to a Figure
6. **AI for Academic Research & Publishing** (~12 articles): Feedback Machines, Vibe Research, AI one-shot papers, Can AI Replace Researchers, Teaching AI Your Voice, Document Collection

### Batch 4 — Specialized
7. **Finance & Econometrics Applications** (~6 articles): Project APE, Automated Research in Finance, policy evaluation threads, Applications (Generative AI for Econ)
8. **AI Tools & Comparisons** (~6 articles): ChatGPT vs Claude, Guide to Which AI, NotebookLM, Using LLMs with Cursor

### Batch 5 — Big Picture
9. **Institutional & Societal Implications** (~8 articles): AI as Normal Technology, The Bitter Lesson, The Shape of AI, Academics Need to Wake Up, The train has left the station
10. **Professional Productivity** (~6 articles): AI Executive Assistant, Project Management, Tax Season, Meeting Transcription, Cost Reality

### Batch 6 — Papers
11. **Academic Papers** (6 items): Korinek (2023), Panjwani slides, Spina/main.tex, Baylor AI Task Force, Awesome Econ AI resource list

### Per-category workflow:
1. Read all raw articles in the batch
2. Create one summary per article in `wiki/summaries/`
3. Identify 2-5 cross-cutting concepts → create/update pages in `wiki/concepts/`
4. Update the category landing page
5. Update `wiki/summaries/index.md` and `wiki/concepts/index.md`
6. Add cross-links to previously created summaries/concepts
7. Commit the batch

---

## Phase 3: Concept Pages (Cross-Cutting Synthesis)

~15 anticipated concept pages, created incrementally during Phase 2:
- Agentic Workflows, Claude Code, CLAUDE.md Files, Prompt Engineering, Plan-Driven Development
- Vibe Research, Feedback Machines, MCP (Model Context Protocol), Skills vs Agents
- Data Pipelines (EDGAR/WRDS/FRED), AI Adoption in Academia, Human-AI Collaboration
- AI as Normal Technology, Cost & Budget, Reproducibility & Transparency

---

## Phase 4: Navigation & Visualization

- **Category map** — Mermaid diagram showing relationships between categories
- **Author index** (`wiki/authors.md`) — All unique authors with links to their summaries
- **Source timeline** — Articles by publication date

---

## Phase 5: Tools (Optional Quality-of-Life)

- `tools/validate_frontmatter.py` — Check YAML fields, wikilink targets
- `tools/build_index.py` — Auto-generate index files from existing wiki pages
- `tools/find_duplicates.py` — Detect near-duplicate raw articles

---

## Phase 6: Polish & Deploy

1. Final cross-link pass (every summary → concept, every concept → 2+ summaries)
2. Check for orphan pages
3. `mkdocs serve` local test — verify rendering, wikilinks, search, navigation
4. Create GitHub remote (start as **private repo**), push, verify GitHub Actions deploys to Pages
5. Review wiki privately, then make repo public when ready
6. Update CLAUDE.md with templates and category assignments

---

## GitHub Privacy Note

- Create the repo as **private** initially
- GitHub Pages works on private repos with GitHub Pro/Teams/Enterprise
- On the free plan, the repo must be public for Pages — so keep it private during development, then flip to public when ready to publish
- Alternatively, use Cloudflare Pages or Netlify which support private repo deploys on free tiers

---

## Verification Plan

After each batch:
- [ ] All new `.md` files have valid YAML frontmatter (`title`, `tags`, `sources`, `date_updated`)
- [ ] All `[[wikilinks]]` resolve to existing files
- [ ] Index files updated
- [ ] `mkdocs build --strict` passes

Final verification:
- [ ] Local `mkdocs serve` renders correctly
- [ ] GitHub Pages site is live and navigable
- [ ] Search works across all wiki pages
- [ ] Obsidian graph view shows connected nodes

---

## Critical Files

| File | Action | Purpose |
|------|--------|---------|
| `.gitignore` | Create | Git exclusions |
| `mkdocs.yml` | Create | MkDocs Material config |
| `requirements.txt` | Create | Python dependencies |
| `.github/workflows/deploy.yml` | Create | Auto-deploy to GitHub Pages |
| `wiki/index.md` | Create | Master TOC |
| `wiki/summaries/index.md` | Create | Summary index |
| `wiki/concepts/index.md` | Create | Concept index |
| `wiki/summaries/<category>.md` | Create (x10) | Category landing pages |
| `wiki/summaries/<article>.md` | Create (~91) | Individual source summaries |
| `wiki/concepts/<concept>.md` | Create (~15) | Cross-cutting concept pages |
| `wiki/authors.md` | Create | Author index |
| `CLAUDE.md` | Update | Add templates, categories |
