# PRD — Website Audit Assistant

## Overview

A local CLI tool that scrapes a client's website, captures screenshots, collects public technical metrics, and generates a professional audit report as a `.docx` file. The audit is used as a presale activity to spark interest and drive a discovery call.

**Who uses this:** Agency consultant (you), running it locally via Claude Code.
**Who reads the output:** Marketing director or website owner at a manufacturing company.

---

## Problem

Cold outreach to manufacturing companies lacks credibility. A personalized, expert-level audit of their website demonstrates expertise, shows specific pain points, and gives the prospect a reason to respond and schedule a call.

---

## Goals

- Produce a professional audit in under 30 minutes of work
- Show expertise in manufacturing website design without giving everything away
- Make the prospect feel understood, not sold to
- End with a clear next step (call invitation)

---

## Workflow

```
1. Consultant runs: python collect.py https://client-site.com
2. Script scrapes site, takes screenshots, pulls PageSpeed data
3. All data saved to /output/<domain>/ folder
4. Consultant opens Claude Code, runs audit analysis
5. Claude writes audit to /output/<domain>/audit.docx
6. Consultant uploads audit.docx to Google Drive, shares with client
```

---

## Audit Report Sections

| # | Section | Source |
|---|---|---|
| 1 | Executive Summary | Claude synthesis |
| 2 | First Impressions & Visual Design | Screenshots |
| 3 | Navigation & User Flow | HTML + screenshots |
| 4 | Product Catalog Review | HTML + screenshots |
| 5 | RFQ / Lead Generation Forms | HTML + screenshots |
| 6 | Content & Downloads (brochures) | HTML + screenshots |
| 7 | SEO Basics | HTML meta tags, headings |
| 8 | Mobile Experience | PageSpeed score + mobile screenshot |
| 9 | Competitor Benchmarks | Web research |
| 10 | Quick Wins | Claude synthesis |
| 11 | Next Steps & Call Invitation | Template |

---

## What We Analyze (No Admin Access Needed)

**Visual / UX (from screenshots):**
- Above-the-fold clarity: is the value proposition immediately obvious?
- Visual hierarchy: do important elements stand out?
- Trust signals: certifications, client logos, case studies
- CTA placement and clarity
- Whitespace, readability, image quality

**Content (from scraped HTML):**
- Heading structure (H1–H3)
- Copy clarity and tone (too technical? too generic?)
- Product catalog: number of products, filtering, descriptions
- RFQ forms: field count, friction, placement
- Brochures and downloadable assets

**SEO Basics (from HTML — no admin needed):**
- Page title (present? descriptive? length)
- Meta description (present? compelling?)
- H1 (one per page? keyword-relevant?)
- Image alt text (missing?)
- Basic URL structure

**Technical (public data only):**
- PageSpeed score (desktop + mobile)
- Core Web Vitals: LCP, CLS, FID
- Mobile usability issues flagged by Google

---

## Out of Scope

- WordPress plugin configuration
- Analytics data (Google Analytics, heatmaps)
- Conversion tracking setup
- Backend / server configuration
- CRM integrations
- Anything requiring login or admin access

---

## Output

- **Format:** `.docx` file
- **Length:** ~8–12 pages
- **Tone:** Expert, helpful, not salesy. Shows problems AND hints at solutions.
- **Branding:** Agency name/logo in header (configurable)
- **Delivery:** Consultant uploads to Google Drive and shares with client

---

## Success Criteria

- Audit takes < 30 min to produce per client
- Prospect responds positively or books a call
- Report feels personalized, not templated
