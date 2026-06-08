# Decision 006 — Output Folder Structure (by Client)

## Decision
Organise output by client name (human-readable), not by domain. Each audit run gets its own dated subfolder so history is preserved.

## Structure
```
output/
  {Client Name}/
    {YYYY-MM-DD}/
      raw/
        homepage_desktop.png
        homepage_mobile.png
        products_desktop.png
        contact_desktop.png
        pagespeed_mobile.png
        pagespeed_desktop.png
        homepage.html
        data.json
      findings.json
      audit_{client-slug}_{date}.docx
```

## Why client name, not domain
- Domains change; company names don't
- Consultants think in terms of clients, not URLs
- Easier to find in Finder: "Meech International" is clearer than "meech.com"

## Why dated subfolder
- Multiple audits for the same client over time (e.g. before/after redesign)
- Historical comparison: show client how their score improved
- Prevents overwriting previous audit data

## Usage
```bash
# With client name (preferred)
python src/collect.py https://meech.com "Meech International"

# Without client name (falls back to domain)
python src/collect.py https://meech.com
```

## gitignore
The entire `output/` folder is excluded from git — client data stays local only, never uploaded to GitHub.
