# Decision 002 — Data Collection Strategy

## Decision
Collect only publicly visible data: rendered HTML, screenshots, and Google PageSpeed metrics. No login, no admin access, no guessing.

## What We Collect

| Data | Method | Why |
|---|---|---|
| Full-page HTML | Playwright | All visible content, structure, forms |
| Desktop screenshot | Playwright @ 1280px | Visual analysis by Claude |
| Mobile screenshot | Playwright @ 375px | Mobile UX analysis |
| Meta title + description | HTML parser (BeautifulSoup) | SEO basics |
| Heading structure (H1–H3) | HTML parser | Content hierarchy |
| Image alt text | HTML parser | SEO + accessibility |
| Forms + fields | HTML parser | RFQ friction analysis |
| Navigation links | HTML parser | User flow analysis |
| Downloadable files (PDFs) | HTML parser | Brochure/asset audit |
| PageSpeed scores | PageSpeed Insights API | Performance without admin |
| Core Web Vitals | PageSpeed Insights API | LCP, CLS, FID — real Google data |

## What We Do NOT Collect

- WordPress plugins or theme configuration (needs admin)
- Google Analytics data (needs account access)
- Heatmaps or session recordings (needs account access)
- Server configuration or hosting details
- CRM or form backend configuration

## Pages to Crawl
1. Homepage (always)
2. Products / Catalog page (if found)
3. Contact / RFQ page (if found)
4. About page (if found)
5. One sample product detail page (if catalog found)

## Google PageSpeed Insights API
- Free, public — no authentication required
- Endpoint: `https://www.googleapis.com/pagespeedonline/v5/runPagespeed`
- Returns: performance score, mobile score, LCP, CLS, FID, specific recommendations
- Called twice per URL: once for desktop, once for mobile
