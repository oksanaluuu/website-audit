# Decision 007 — GitHub Setup & Version Control

## Decision
Host the project on GitHub at `https://github.com/oksanaluuu/website-audit` as a public repo. Use `gh` CLI for repo management.

## What is in the repo
- All source code: `src/collect.py`, `src/report.py`
- All planning docs: `PRD.md`, `BACKLOG.md`, `decisions/`, `prompts/`
- Config templates: `requirements.txt`, `.env.example`, `README.md`
- Claude instructions: `CLAUDE.md`

## What is NOT in the repo (gitignored)
- `.venv/` — Python virtual environment (recreated via `pip install -r requirements.txt`)
- `output/` — client audit data, screenshots, .docx files — stays local only
- `.env` — contains agency name; only `.env.example` is committed

## gh CLI installation
- Installed to `~/bin/gh` (no sudo needed)
- `~/bin` added to `$PATH` in `~/.zshrc` — permanent across all terminal sessions
- Authenticated via `gh auth login --web`

## How to push updates
```bash
git add .
git commit -m "describe what changed"
git push
```

## Branch strategy
- `main` is the only branch for now
- Create feature branches if working on a large Sprint 4 change
