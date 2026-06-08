# CLAUDE.md — Website Audit Assistant

This file is the operating manual for this project. Read it at the start of every session.

---

## What This Project Is

A local CLI tool that audits a manufacturing client's website and produces a professional `.docx` report used as a presale activity. The goal is to demonstrate expertise, show specific pain points, and spark a discovery call.

**Who uses it:** Agency consultant (Oksana), running locally via Claude Code.
**Who reads the output:** Marketing director or website owner at a manufacturing company.

---

## The Three-Step Workflow

### Step 1 — Collect data
```bash
cd /Users/oksanalu/dev/website-audit
source .venv/bin/activate
python src/collect.py https://client-website.com "Client Name"
```
- Takes ~5–7 minutes total (includes PageSpeed analysis)
- Saves everything to `output/{Client Name}/{YYYY-MM-DD}/raw/`
- Output: screenshots (desktop + mobile per page), HTML, data.json, PageSpeed screenshots

### Step 2 — Analyse (Claude Code reads the data)
Open Claude Code in this folder and say:

> Read the files in `output/{Client Name}/{date}/raw/` — the data.json and all screenshots.
> Generate `output/{Client Name}/{date}/findings.json` following the schema in `prompts/findings-schema.json`.
> Use the evaluation criteria in `decisions/003-analysis-scope.md`.
> Search the web for 2–3 competitors to include in the benchmarking section.

### Step 3 — Generate report
```bash
python src/report.py "{Client Name}" {date}
```
Example:
```bash
python src/report.py "Meech International" 2026-06-08
```
Output: `output/{Client Name}/{date}/audit_{slug}_{date}.docx`

---

## Project File Structure

```
website-audit/
├── CLAUDE.md                  ← you are here — read first every session
├── PRD.md                     ← full product requirements
├── BACKLOG.md                 ← sprint status — check before starting work
├── README.md                  ← end-user usage instructions
├── requirements.txt           ← Python dependencies
├── .env.example               ← copy to .env and set AGENCY_NAME
├── .env                       ← local only, gitignored
│
├── src/
│   ├── collect.py             ← scrapes website, takes screenshots, runs PageSpeed
│   └── report.py             ← generates .docx from findings.json
│
├── prompts/
│   ├── analyze.md             ← instructions for Claude Code analysis step
│   └── findings-schema.json   ← exact JSON structure Claude must produce
│
├── decisions/                 ← one file per key technical/process decision
│   ├── 001-tech-stack.md
│   ├── 002-data-collection.md
│   ├── 003-analysis-scope.md  ← what to evaluate in each audit section
│   ├── 004-output-format.md
│   ├── 005-pagespeed-browser.md
│   ├── 006-folder-structure.md
│   └── 007-github-setup.md
│
└── output/                    ← gitignored — client data stays local
    └── {Client Name}/
        └── {YYYY-MM-DD}/
            ├── raw/           ← screenshots, HTML, data.json
            ├── findings.json  ← Claude's analysis output
            └── audit_*.docx   ← final report
```

---

## Environment Setup (first time or after cloning)

```bash
cd /Users/oksanalu/dev/website-audit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
# Edit .env: set AGENCY_NAME="Your Agency Name"
```

---

## Key Decisions Log

All decisions are in `decisions/`. Before changing any approach, check if a decision file covers it.

| # | Decision | Short answer |
|---|---|---|
| 001 | Tech stack | Python + Playwright + python-docx |
| 002 | What data to collect | Only public/visible — no admin access |
| 003 | What to analyse | Visual, UX, catalog, RFQ, SEO basics, mobile |
| 004 | Output format | .docx locally, user uploads to Google Drive |
| 005 | PageSpeed | Browser via Playwright (not API — rate limits) |
| 006 | Folder structure | output/{Client Name}/{date}/ |
| 007 | GitHub | github.com/oksanaluuu/website-audit, gh CLI in ~/bin |

When a new decision is made during development, **immediately create a new numbered file** in `decisions/` and add a row to this table.

---

## Sprint Status

| Sprint | Topic | Status |
|---|---|---|
| 1 | Data collection | ✅ Done |
| 2 | Analysis workflow | ✅ Done |
| 3 | Report generation | ✅ Done |
| 4 | Polish & hardening | 🔄 Next |

See `BACKLOG.md` for the full task list within each sprint.

---

## Manufacturing Industry Context

This tool is built specifically for manufacturing websites. When analysing, pay attention to:

- **Product catalog:** specs, part numbers, datasheets, filtering by application/material
- **RFQ forms:** number of fields (> 7 = high friction), prominence, placement
- **Trust signals:** ISO certifications, ATEX/CE compliance, years in business, client logos
- **Application-based navigation:** manufacturing buyers search by problem/industry, not product name
- **Brochures & downloads:** datasheets, industry guides, operating manuals — proximity to product pages matters
- **Global presence:** regional offices, distributor maps, translated content

Common manufacturing website competitors to benchmark against:
- Static control: Simco-Ion, Fraser Anti-Static
- Air technology: EXAIR, Nex Flow
- Web cleaning: Teknek, Meech (if auditing a competitor)

---

## GitHub Workflow

```bash
# Push updates after any change
git add .
git commit -m "what you changed"
git push

# gh CLI is in ~/bin — available in all terminals
~/bin/gh repo view  # check repo status
```

Repo: `https://github.com/oksanaluuu/website-audit`

---

## Adding a New Process or Tool

When a new capability is added (e.g. email draft generation, scoring system, new page type):
1. Add tasks to the relevant sprint in `BACKLOG.md`
2. Create a `decisions/NNN-topic.md` file explaining the choice
3. Update this CLAUDE.md: add a row to the Key Decisions Log and update Sprint Status
4. Commit and push

This ensures every future Claude Code session starts with the full picture.
