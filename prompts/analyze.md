# Audit Analysis Prompt

Use this prompt in Claude Code after running `collect.py`.
Replace `<domain>` with the actual domain folder name.

---

## How to Run an Audit

**Step 1 — Collect data:**
```bash
python src/collect.py https://client-website.com
```

**Step 2 — Analyze (paste this into Claude Code):**

```
I need you to analyze the website audit data I just collected and write a findings.json file.

Read these files:
- output/<domain>/raw/data.json
- output/<domain>/raw/homepage_desktop.png
- output/<domain>/raw/homepage_mobile.png
- output/<domain>/raw/products_desktop.png  (if it exists)
- output/<domain>/raw/contact_desktop.png   (if it exists)

Then produce output/<domain>/findings.json following the schema in prompts/findings-schema.json.

Context about who we are:
- We are a web design agency specializing in manufacturing industry websites
- This audit is a presale document — we want to show expertise and spark a discovery call
- Tone: expert, helpful, specific — not generic, not salesy
- Every finding must be based on what you actually see in the data or screenshots

For competitor benchmarking:
- Search the web for 2-3 competitors of this company
- Find specific things they do better on their websites
- Name the competitor and cite the specific feature or page

Generate findings.json now.
```

**Step 3 — Generate report:**
```bash
python src/report.py <domain>
```

The `.docx` file will appear in `output/<domain>/`.
