"""
collect.py — scrapes a website and saves raw data for audit analysis.

Usage:
    python src/collect.py https://example.com
"""

import sys
import json
import re
import time
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, urljoin, quote
from dotenv import load_dotenv

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

load_dotenv()

DESKTOP_VIEWPORT = {"width": 1280, "height": 800}
MOBILE_VIEWPORT = {"width": 375, "height": 812}

# Pages to look for beyond the homepage
TARGET_PAGE_PATTERNS = {
    "products": ["/product", "/products", "/catalog", "/catalogue", "/solutions", "/portfolio"],
    "contact": ["/contact", "/rfq", "/quote", "/request", "/get-a-quote"],
    "about": ["/about", "/about-us", "/company", "/who-we-are"],
}


def get_domain(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc.lstrip("www.")


def make_output_dir(client_name: str, date_str: str) -> Path:
    base = Path(__file__).parent.parent / "output" / client_name / date_str / "raw"
    base.mkdir(parents=True, exist_ok=True)
    return base


def scrape_page(page, url: str, slug: str, output_dir: Path) -> dict:
    """Load a page, take screenshots, and return scraped data."""
    print(f"  Scraping: {url}")

    try:
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(1500)

        desktop_path = output_dir / f"{slug}_desktop.png"
        page.screenshot(path=str(desktop_path), full_page=True)

        html = page.content()
        title = page.title()

        page.set_viewport_size(MOBILE_VIEWPORT)
        page.wait_for_timeout(800)
        mobile_path = output_dir / f"{slug}_mobile.png"
        page.screenshot(path=str(mobile_path), full_page=True)

        page.set_viewport_size(DESKTOP_VIEWPORT)

    except Exception as e:
        print(f"    Warning: could not fully load {url}: {e}")
        html = ""
        title = ""

    return {
        "url": url,
        "slug": slug,
        "title": title,
        "html": html,
        "desktop_screenshot": str(desktop_path) if html else None,
        "mobile_screenshot": str(mobile_path) if html else None,
    }


def find_sub_pages(homepage_html: str, base_url: str) -> dict:
    """Find links to products, contact, and about pages from homepage HTML."""
    soup = BeautifulSoup(homepage_html, "lxml")
    found = {}

    all_links = [
        urljoin(base_url, a["href"])
        for a in soup.find_all("a", href=True)
        if urlparse(urljoin(base_url, a["href"])).netloc == urlparse(base_url).netloc
    ]

    for page_type, patterns in TARGET_PAGE_PATTERNS.items():
        for link in all_links:
            path = urlparse(link).path.lower()
            if any(pat in path for pat in patterns):
                found[page_type] = link
                break

    return found


def parse_html(html: str, url: str) -> dict:
    """Extract structured SEO and content data from HTML."""
    soup = BeautifulSoup(html, "lxml")

    meta_title = soup.title.get_text(strip=True) if soup.title else ""

    meta_desc_tag = soup.find("meta", attrs={"name": re.compile(r"description", re.I)})
    meta_description = meta_desc_tag.get("content", "").strip() if meta_desc_tag else ""

    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
    h2s = [h.get_text(strip=True) for h in soup.find_all("h2")]
    h3s = [h.get_text(strip=True) for h in soup.find_all("h3")]

    images = soup.find_all("img")
    images_missing_alt = [
        img.get("src", "")
        for img in images
        if not img.get("alt", "").strip()
    ]
    total_images = len(images)

    forms = []
    for form in soup.find_all("form"):
        fields = form.find_all(["input", "select", "textarea"])
        visible_fields = [
            f for f in fields
            if f.get("type", "").lower() not in ("hidden", "submit", "button")
        ]
        submit_btn = form.find(["button", "input"], attrs={"type": re.compile(r"submit", re.I)})
        forms.append({
            "field_count": len(visible_fields),
            "field_names": [f.get("name", f.get("placeholder", "")) for f in visible_fields],
            "submit_label": submit_btn.get_text(strip=True) if submit_btn else "",
        })

    downloads = []
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if any(href.endswith(ext) for ext in [".pdf", ".doc", ".docx", ".xls", ".xlsx"]):
            downloads.append({
                "text": a.get_text(strip=True),
                "href": a["href"],
            })

    nav = soup.find("nav")
    nav_links = []
    if nav:
        nav_links = [a.get_text(strip=True) for a in nav.find_all("a") if a.get_text(strip=True)]

    phone_pattern = re.compile(r"[\+\(]?[\d\s\-\(\)\.]{7,20}")
    body_text = soup.get_text(" ", strip=True)
    phones = phone_pattern.findall(body_text)[:3]

    cta_keywords = ["request a quote", "get a quote", "contact us", "rfq", "request quote",
                    "get in touch", "start a project", "ask for a quote"]
    ctas = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True).lower()
        if any(kw in text for kw in cta_keywords):
            ctas.append(a.get_text(strip=True))

    return {
        "url": url,
        "meta_title": meta_title,
        "meta_title_length": len(meta_title),
        "meta_description": meta_description,
        "meta_description_length": len(meta_description),
        "h1s": h1s,
        "h2s": h2s[:10],
        "h3s": h3s[:10],
        "total_images": total_images,
        "images_missing_alt_count": len(images_missing_alt),
        "forms": forms,
        "downloads": downloads,
        "nav_links": nav_links,
        "phone_numbers": phones,
        "ctas_found": ctas,
    }


def _poll_psi_score(page, timeout: int = 120) -> str:
    """Poll DOM via CDP until a Lighthouse gauge score appears. Avoids eval/Trusted Types issues."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            el = page.query_selector(".lh-gauge__percentage")
            if el:
                val = el.inner_text().strip()
                if val and val.isdigit():
                    return val
        except Exception:
            pass
        time.sleep(2)
    return "N/A"


def get_pagespeed_browser(context, url: str, output_dir: Path) -> dict:
    """Open PageSpeed Insights web UI via Playwright, screenshot results."""
    print("  Running PageSpeed via browser (~60s)...")

    psi_url = f"https://pagespeed.web.dev/report?url={quote(url, safe='')}"
    results = {}
    psi_page = context.new_page()

    try:
        psi_page.set_viewport_size({"width": 1280, "height": 900})

        print("    Waiting for mobile analysis (up to 2 min)...")
        psi_page.goto(psi_url, wait_until="domcontentloaded", timeout=30000)

        # Poll via Python — avoids Trusted Types CSP that blocks eval-based waits
        mobile_score = _poll_psi_score(psi_page, timeout=120)
        psi_page.wait_for_timeout(1500)

        mobile_path = output_dir / "pagespeed_mobile.png"
        psi_page.screenshot(path=str(mobile_path), full_page=False)
        results["mobile"] = {
            "performance_score": mobile_score,
            "screenshot": str(mobile_path),
        }

        # Switch to Desktop tab
        print("    Switching to desktop analysis...")
        desktop_tab = (
            psi_page.query_selector("button:has-text('Desktop')") or
            psi_page.query_selector("label:has-text('Desktop')") or
            psi_page.query_selector("[aria-label='Desktop']")
        )

        if desktop_tab:
            desktop_tab.click()
            desktop_score = _poll_psi_score(psi_page, timeout=120)
            psi_page.wait_for_timeout(1500)

            desktop_path = output_dir / "pagespeed_desktop.png"
            psi_page.screenshot(path=str(desktop_path), full_page=False)
            results["desktop"] = {
                "performance_score": desktop_score,
                "screenshot": str(desktop_path),
            }
        else:
            print("    Desktop tab not found — mobile only")
            results["desktop"] = {"performance_score": "N/A"}

    except Exception as e:
        print(f"    Warning: PageSpeed browser check failed: {e}")
        results = {
            "mobile": {"performance_score": "N/A", "error": str(e)},
            "desktop": {"performance_score": "N/A", "error": str(e)},
        }
    finally:
        psi_page.close()

    return results


def collect(url: str, client_name: str = ""):
    if not url.startswith("http"):
        url = "https://" + url

    domain = get_domain(url)
    client_name = client_name.strip() or domain
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_dir = make_output_dir(client_name, date_str)

    print(f"\nStarting audit data collection for: {url}")
    print(f"Client: {client_name}")
    print(f"Output directory: {output_dir}\n")

    pages_data = {}
    parsed_data = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/124.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Homepage
        print("[ 1 / 4 ] Homepage")
        homepage = scrape_page(page, url, "homepage", output_dir)
        pages_data["homepage"] = homepage
        parsed_data["homepage"] = parse_html(homepage["html"], url)

        # Save homepage HTML for reference
        if homepage["html"]:
            (output_dir / "homepage.html").write_text(homepage["html"], encoding="utf-8")

        # Find sub-pages
        sub_pages = find_sub_pages(homepage["html"], url)
        print(f"  Found sub-pages: {list(sub_pages.keys())}")

        step = 2
        for page_type in ["products", "contact", "about"]:
            if page_type in sub_pages:
                print(f"\n[ {step} / 4 ] {page_type.capitalize()} page")
                scraped = scrape_page(page, sub_pages[page_type], page_type, output_dir)
                pages_data[page_type] = scraped
                parsed_data[page_type] = parse_html(scraped["html"], sub_pages[page_type])
                if scraped["html"]:
                    (output_dir / f"{page_type}.html").write_text(
                        scraped["html"], encoding="utf-8"
                    )
                step += 1

        # PageSpeed — runs inside same browser session
        print(f"\n[ {step} / 4 ] PageSpeed Insights")
        pagespeed = get_pagespeed_browser(context, url, output_dir)

        browser.close()

    # Compile full data payload
    data = {
        "collected_at": datetime.now().isoformat(),
        "url": url,
        "domain": domain,
        "client_name": client_name,
        "date": date_str,
        "pages": {
            page_type: {
                "url": pages_data[page_type]["url"],
                "title": pages_data[page_type]["title"],
                "desktop_screenshot": pages_data[page_type]["desktop_screenshot"],
                "mobile_screenshot": pages_data[page_type]["mobile_screenshot"],
                **parsed_data[page_type],
            }
            for page_type in pages_data
        },
        "pagespeed": pagespeed,
    }

    output_path = output_dir / "data.json"
    output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDone. Data saved to: {output_path}")
    print("\nNext step: open Claude Code and run the audit analysis.")
    print(f"  Domain: {domain}")
    print(f"  Pages collected: {list(pages_data.keys())}")
    print(f"  PageSpeed desktop: {pagespeed.get('desktop', {}).get('performance_score', 'N/A')}/100")
    print(f"  PageSpeed mobile:  {pagespeed.get('mobile', {}).get('performance_score', 'N/A')}/100")

    return str(output_dir)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/collect.py <url> [\"Client Name\"]")
        sys.exit(1)
    client = sys.argv[2] if len(sys.argv) > 2 else ""
    collect(sys.argv[1], client)
