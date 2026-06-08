# Backlog — Website Audit Assistant

## Sprint 1 — Data Collection Layer ✅ DONE
- [x] Project scaffold: folder structure, `requirements.txt`, `.env.example`
- [x] `collect.py` — main entry point, accepts URL + optional client name
- [x] Playwright: full-page HTML scrape
- [x] Playwright: desktop screenshot (1280px)
- [x] Playwright: mobile screenshot (375px)
- [x] Playwright: crawl key sub-pages (products, contact, about)
- [x] HTML parser: extract meta title, meta description, H1–H3, image alt text
- [x] HTML parser: detect and extract forms (fields, labels, CTAs)
- [x] HTML parser: detect downloadable assets (PDFs, brochures)
- [x] HTML parser: extract navigation structure
- [x] PageSpeed via browser (pagespeed.web.dev) — mobile + desktop screenshots + score
- [x] Save all output to `/output/{Client Name}/{date}/raw/`

---

## Sprint 2 — Analysis Workflow ✅ DONE
- [x] Analysis prompt template in `prompts/analyze.md`
- [x] findings.json schema in `prompts/findings-schema.json`
- [x] Manufacturing-specific evaluation criteria (`decisions/003-analysis-scope.md`)
- [x] Per-section finding format: issue → impact → suggestion
- [x] Quick wins table with priority/effort/impact
- [x] Tested end-to-end on meech.com

---

## Sprint 3 — Report Generation ✅ DONE
- [x] `report.py` — generates `.docx` from findings.json
- [x] Cover page with client domain + date + agency name
- [x] All 11 sections formatted with headings and finding blocks
- [x] Screenshots embedded: homepage desktop/mobile, products, contact, PageSpeed
- [x] Quick Wins table with colour header
- [x] Next Steps + call invitation CTA

---

## Sprint 4 — Polish & Hardening 🔄 NEXT
- [ ] Update `collect.py` to accept optional client name: `python src/collect.py <url> "Client Name"`
- [ ] Reorganise output to `/output/{Client Name}/{YYYY-MM-DD}/` (see `decisions/006-folder-structure.md`)
- [ ] Update `report.py` to use new folder structure
- [ ] Error handling: sites that block headless browsers (add realistic UA + retry)
- [ ] Error handling: timeout on slow sites (graceful partial output)
- [ ] Crawl one sample product detail page (not just the catalog overview)
- [ ] RFQ friction scoring: flag forms with > 7 fields as "high friction"
- [ ] Product catalog depth check: detect missing specs, missing images, no CTA
- [ ] Industry trust signal check: look for ISO/ATEX/CE certifications in HTML
- [ ] Configurable agency logo in report cover page
- [ ] `README.md` — finalise with Sprint 4 usage examples

---

## Icebox (Future Ideas)
- Multi-language support for non-English manufacturing sites
- Scoring system (0–100) per section with a summary scorecard
- Before/after mockup sketch suggestion for one key page
- Automatic email draft with audit attached
- Competitor URL auto-detection (web search for "top competitors of X")
