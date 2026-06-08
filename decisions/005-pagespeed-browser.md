# Decision 005 — PageSpeed via Browser (not API)

## Decision
Use Playwright to open pagespeed.web.dev directly instead of calling the PageSpeed Insights REST API.

## Why we switched away from the API
- The public API (no key) hits a 429 rate limit after 1–2 calls per hour
- Adding an API key requires a Google Cloud project — unnecessary setup for a local tool
- The API returns raw JSON; the browser returns a full visual report

## Why the browser approach is better
- Zero rate limiting — no API key, no quota
- Screenshots of the actual Google report go directly into the .docx, which is more credible to clients than raw numbers
- Real CrUX data (28-day real user data) is visible, not just Lighthouse synthetic scores
- Captures both Mobile and Desktop tabs with separate screenshots

## Implementation details
- Navigate to `https://pagespeed.web.dev/report?url=<encoded_url>`
- Google's Trusted Types CSP blocks `eval()` — so `wait_for_function` and `evaluate` do not work
- Solution: Python-side polling loop using `query_selector` + `inner_text()` via CDP (bypasses Trusted Types)
- Poll every 2 seconds up to 120 seconds for `.lh-gauge__percentage` to return a numeric value
- Switch to Desktop tab by clicking `button:has-text('Desktop')`
- Screenshots saved as `pagespeed_mobile.png` and `pagespeed_desktop.png` in `/raw/`

## Known limitation
- Adds ~2–3 minutes to collection time (Lighthouse runs twice — mobile + desktop)
- If pagespeed.web.dev changes its DOM structure, selectors may need updating
