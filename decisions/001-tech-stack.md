# Decision 001 — Tech Stack

## Decision
Python + Playwright for data collection. Claude Code (subscription) for analysis. `python-docx` for report output.

## Why Python
- Rich ecosystem for web scraping, HTML parsing, and document generation
- Single language for the entire pipeline
- Easy to run locally with no server setup

## Why Playwright (not Selenium, not a screenshot API)
- Modern, actively maintained, reliable on complex JS-heavy sites
- Handles both scraping AND screenshots in one tool
- Supports mobile viewport simulation natively
- No external API cost — runs fully local
- Selenium is older and more brittle; screenshot APIs cost money per call

## Why Claude Code for Analysis (not Claude API)
- User already has a Claude Code subscription — zero additional cost
- Claude Code can read local files directly (screenshots, JSON, HTML)
- No API key management or per-token billing
- Analysis happens interactively, consultant can steer findings

## Why python-docx for Output (not Google Docs API, not PDF)
- No authentication setup required
- `.docx` files upload cleanly to Google Drive and open as Google Docs
- Client can edit the document after receiving it
- PDF would require a rendering step and isn't editable
- Google Docs API requires OAuth credentials and a Cloud project
