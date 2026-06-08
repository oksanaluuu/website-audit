# Decision 003 — Analysis Scope

## Decision
Audit focuses on visual/UX, content quality, and observable technical metrics. Every finding must be backed by something we actually collected — no speculation.

## Evaluation Criteria by Section

### First Impressions & Visual Design
- Is the value proposition visible above the fold?
- Does the homepage look modern and trustworthy?
- Are images high quality and relevant to manufacturing?
- Is there visual clutter or too much text?
- Are trust signals present? (certifications, client logos, years in business)

### Navigation & User Flow
- Can a visitor find the product catalog in < 2 clicks?
- Is there a clear path from product → RFQ?
- Is the navigation logical for a manufacturing buyer?
- Is there a search bar?

### Product Catalog
- Are products organized by category or industry?
- Do product pages include: specs, part numbers, downloadable datasheets?
- Is filtering available (by material, size, application)?
- Are product images adequate? Multiple angles?
- Is there a comparison feature?

### RFQ / Lead Generation Forms
- Is there an RFQ form? Is it easy to find?
- How many fields does it have? (> 10 fields = high friction)
- Is there a phone number visible without scrolling?
- Are there multiple conversion paths? (form, phone, chat)
- Is the CTA clear? ("Request a Quote" vs "Submit")

### Content & Downloads
- Are brochures / datasheets available?
- Are they gated (email required) or free?
- Is the content up to date? (check for date signals in text)
- Is there a blog or resources section?

### SEO Basics (observable only)
- Page title: present, under 60 chars, descriptive?
- Meta description: present, under 155 chars, compelling?
- H1: exactly one per page, contains primary keyword?
- Images: do they have alt text?

### Mobile Experience
- PageSpeed mobile score (0–100)
- Are buttons large enough to tap?
- Is text readable without zooming?
- Does the RFQ form work on mobile?

### Competitor Benchmarks
- 2–3 competitors identified via web search
- Compare: catalog structure, RFQ prominence, trust signals, mobile experience
- Highlight 1–2 specific things competitors do better

## Finding Format
Each finding follows this structure:
```
Issue: [what is wrong or missing]
Impact: [why this matters to a manufacturing buyer]
Suggestion: [high-level fix, not a full spec]
```

## Quick Wins Criteria
A finding qualifies as a Quick Win if:
- It can likely be fixed without a full redesign
- It has direct impact on conversions (RFQ submissions, calls)
- Examples: missing phone number in header, no alt text, form has 15 fields, no CTA above fold
