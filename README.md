# Website Audit Assistant

Generates professional website audit reports for manufacturing industry presales.

## Setup (one time)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
# Edit .env and set your AGENCY_NAME
```

## How to audit a website

### Step 1 — Collect data
```bash
source .venv/bin/activate
python src/collect.py https://client-website.com
```

This takes ~2–3 minutes. It will:
- Screenshot the homepage, products, contact, and about pages (desktop + mobile)
- Scrape all visible HTML content
- Pull Google PageSpeed scores
- Save everything to `output/<domain>/raw/`

### Step 2 — Analyze with Claude Code

Open Claude Code in this folder and paste:

```
Read output/<domain>/raw/data.json and the screenshots in output/<domain>/raw/.
Follow the instructions in prompts/analyze.md to generate output/<domain>/findings.json.
```

Claude Code reads the screenshots visually and the JSON data, then writes `findings.json`.

### Step 3 — Generate the report
```bash
python src/report.py <domain>
```

Example: `python src/report.py acmeindustrial.com`

Your report appears at: `output/<domain>/audit_<domain>_<date>.docx`

Upload it to Google Drive and share with the client.

---

## Output structure

```
output/
  acmeindustrial.com/
    raw/
      data.json                  ← all scraped data
      homepage.html
      homepage_desktop.png
      homepage_mobile.png
      products_desktop.png
      contact_desktop.png
    findings.json                ← Claude's analysis
    audit_acmeindustrial.com_2026-06-08.docx
```

## Customization

- **Agency name:** set `AGENCY_NAME` in `.env`
- **Audit sections:** edit `prompts/findings-schema.json`
- **Report layout:** edit `src/report.py`
