# Backlog — Website Audit Assistant

## Sprint 1 — Data Collection Layer
*Goal: Run a URL and get all raw data saved locally.*

- [ ] Project scaffold: folder structure, `requirements.txt`, `.env.example`
- [ ] `collect.py` — main entry point, accepts URL as argument
- [ ] Playwright: full-page HTML scrape
- [ ] Playwright: desktop screenshot (1280px)
- [ ] Playwright: mobile screenshot (375px)
- [ ] Playwright: crawl key sub-pages (products, contact, about)
- [ ] HTML parser: extract meta title, meta description, H1–H3, image alt text
- [ ] HTML parser: detect and extract forms (fields, labels, CTAs)
- [ ] HTML parser: detect downloadable assets (PDFs, brochures)
- [ ] HTML parser: extract navigation structure
- [ ] PageSpeed Insights API: fetch desktop + mobile scores and Core Web Vitals
- [ ] Save all output to `/output/<domain>/raw/` as structured JSON + images

---

## Sprint 2 — Analysis Workflow
*Goal: Claude Code reads raw data and produces structured audit findings.*

- [ ] Define analysis prompt template covering all 9 audit sections
- [ ] Manufacturing-specific evaluation criteria (product catalog, RFQ, brochures)
- [ ] Competitor research: auto-search 2–3 competitors based on industry + location
- [ ] Per-section finding format: issue → impact → suggested fix
- [ ] Quick wins scoring: prioritize by effort vs. impact
- [ ] Save structured findings to `/output/<domain>/findings.json`

---

## Sprint 3 — Report Generation
*Goal: Turn findings into a formatted, shareable `.docx` file.*

- [ ] `report.py` — generates `.docx` from findings JSON
- [ ] Document template: cover page, header, footer with agency branding
- [ ] Section formatting: headings, body text, callout boxes
- [ ] Embed screenshots (desktop + mobile) with captions
- [ ] Quick Wins table (priority, effort, impact)
- [ ] Next Steps section with call invitation
- [ ] Save to `/output/<domain>/audit_<domain>_<date>.docx`

---

## Sprint 4 — Polish & Manufacturing Specifics
*Goal: Make the audit smarter about the manufacturing industry.*

- [ ] Product catalog depth: check for filtering, specs, part numbers, datasheets
- [ ] RFQ form analysis: field count heuristic, friction scoring, missing fields
- [ ] Industry trust signals: ISO certifications, case studies, client logos
- [ ] Brochure quality check: file naming, accessibility, CTA after download
- [ ] Configurable agency name/logo in report header
- [ ] README with full usage instructions
- [ ] Error handling: invalid URLs, sites that block scraping, timeouts

---

## Icebox (Future Ideas)

- Multi-language support for non-English manufacturing sites
- Automatic email draft with audit attached
- Scoring system (0–100) for each section
- Before/after mockup suggestion for one key page
