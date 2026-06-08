# Decision 004 — Output Format

## Decision
Generate a `.docx` file locally using `python-docx`. Consultant uploads it to Google Drive manually.

## Report Structure

```
Cover Page
  - Client company name + website
  - "Website Audit" title
  - Date
  - Agency name

Section 1: Executive Summary (half page)
Section 2: First Impressions & Visual Design
Section 3: Navigation & User Flow
Section 4: Product Catalog Review
Section 5: RFQ / Lead Generation Forms
Section 6: Content & Downloads
Section 7: SEO Basics
Section 8: Mobile Experience
Section 9: Competitor Benchmarks
Section 10: Quick Wins (table: priority | issue | effort | impact)
Section 11: Next Steps & Call Invitation
```

## Formatting Conventions
- Each section: heading + 3–6 findings
- Each finding: bold issue label + body text
- Screenshots: inline images with captions (desktop + mobile)
- Quick Wins: formatted table
- Tone: professional, direct, not academic

## Why .docx over PDF
- Client can be given an editable version if needed
- Uploads to Google Drive and opens natively as a Google Doc
- No rendering step or wkhtmltopdf dependency

## Why .docx over Markdown
- Proper formatting (tables, images, headings) without conversion
- Ready to share immediately, looks professional out of the box

## File Naming
`audit_<domain>_<YYYY-MM-DD>.docx`
Example: `audit_acmeindustrial.com_2026-06-08.docx`

## Storage
All output stored under: `/output/<domain>/`
```
/output/acmeindustrial.com/
  raw/
    homepage.html
    homepage_desktop.png
    homepage_mobile.png
    products.html
    products_desktop.png
    contact.html
    data.json          ← all extracted structured data
  audit_acmeindustrial.com_2026-06-08.docx
```
