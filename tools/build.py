#!/usr/bin/env python3
"""Builds the 3 static, fully pre-rendered pages from tools/translations.json
+ tools/index.template.html:
    index.html     -> French (default)  https://ajwadateswholesale.vercel.app/
    en/index.html  -> English           https://ajwadateswholesale.vercel.app/en/
    es/index.html  -> Spanish           https://ajwadateswholesale.vercel.app/es/
and sitemap.xml. Asset paths are RELATIVE, so index.html also opens with a double-click.
Usage (from the project folder):  python3 tools/build.py
"""
import json, html, re, urllib.parse, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://ajwadateswholesale.vercel.app"   # production domain (no trailing slash)
LANGS = ["fr", "en", "es"]                        # first = default language, served at /
PATHS = {"fr": "/", "en": "/en/", "es": "/es/"}
LASTMOD = "2026-10-28"
WA_NUMBER = "212661111111"                        # WhatsApp number (digits only)
FAQ_COUNT = 8

# Indicative Ajwa calendar for Madinah (index 0 = January). Edit here if needed.
HARVEST = ["stock", "stock", "stock", "stock", "stock", "stock",
           "early", "peak", "main", "new", "stock", "stock"]

T = json.loads((ROOT / "tools/translations.json").read_text(encoding="utf-8"))

def wa(lang):
    return f"https://wa.me/{WA_NUMBER}?text=" + urllib.parse.quote(T[lang]["wa.text"])

def url(lang):
    return SITE + PATHS[lang]

def prefix(lang):
    """Relative prefix from the page to the site root."""
    depth = PATHS[lang].strip("/").count("/") + (1 if PATHS[lang] != "/" else 0)
    return "../" * depth

def rel_link(cur, target):
    """Relative link from page `cur` to page `target` (folder URL with trailing slash)."""
    if cur == target:
        return "./"
    p = prefix(cur) + PATHS[target].lstrip("/")
    return p or "./"

def faq_ld(lang):
    d = T[lang]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": url(lang) + "#faq",
        "inLanguage": lang,
        "mainEntity": [
            {"@type": "Question", "name": d[f"faq.q{i}"],
             "acceptedAnswer": {"@type": "Answer", "text": d[f"faq.a{i}"]}}
            for i in range(1, FAQ_COUNT + 1)
        ],
    }

def org_ld(lang):
    name = T["en"]["site.name"]
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": SITE + "/#organization",
                "name": name,
                "url": SITE + "/",
                "contactPoint": {
                    "@type": "ContactPoint",
                    "contactType": "sales",
                    "telephone": "+" + WA_NUMBER,
                    "url": "https://wa.me/" + WA_NUMBER,
                    "availableLanguage": ["French", "English", "Spanish"],
                },
            },
            {
                "@type": "WebSite",
                "@id": SITE + "/#website",
                "name": name,
                "alternateName": [T["fr"]["site.name"], T["es"]["site.name"]],
                "url": SITE + "/",
                "inLanguage": LANGS,
                "publisher": {"@id": SITE + "/#organization"},
            },
        ],
    }

SVG = lambda body, s=26: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>'
WA_PATH = '<path fill="currentColor" d="M16.04 3C9.4 3 4 8.33 4 14.9c0 2.1.56 4.15 1.62 5.95L4 29l8.4-1.6a12.2 12.2 0 0 0 3.64.55C22.66 27.95 28 22.62 28 16.05 28 9.48 22.66 3 16.04 3zm0 22.8c-1.13 0-2.24-.18-3.3-.53l-.6-.2-4.98.95.97-4.83-.22-.6a9.6 9.6 0 0 1-1.44-5.1c0-5.3 4.3-9.6 9.57-9.6s9.57 4.3 9.57 9.6-4.3 10.31-9.57 10.31zm5.27-7.07c-.29-.14-1.7-.83-1.96-.92-.27-.1-.46-.14-.65.14-.2.29-.75.92-.92 1.1-.17.2-.34.22-.63.08-.29-.15-1.22-.45-2.32-1.43-.86-.76-1.44-1.7-1.6-1.99-.17-.29-.02-.44.12-.58.13-.13.29-.34.43-.5.15-.18.2-.3.29-.49.1-.19.05-.36-.02-.5-.07-.15-.65-1.56-.89-2.13-.23-.56-.47-.48-.65-.49h-.55c-.19 0-.5.07-.77.36-.26.29-1 .98-1 2.4 0 1.4 1.03 2.77 1.17 2.96.15.19 2.03 3.1 4.92 4.34.69.3 1.22.47 1.64.6.69.22 1.32.19 1.81.12.55-.08 1.7-.69 1.94-1.36.24-.67.24-1.25.17-1.37-.07-.12-.26-.19-.55-.33z"/>'
ICONS = {
    "ICON_SPRITE": f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><symbol id="i-wa" viewBox="0 0 32 32">{WA_PATH}</symbol></svg>',
    "ICON_WA_LG": '<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true" focusable="false"><use href="#i-wa"/></svg>',
    "ICON_WA": '<svg class="i-wa" viewBox="0 0 32 32" width="20" height="20" aria-hidden="true" focusable="false"><use href="#i-wa"/></svg>',
    "ICON_PIN": SVG('<path d="M12 21s-6.5-6.1-6.5-11a6.5 6.5 0 0 1 13 0c0 4.9-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'),
    "ICON_BOX": SVG('<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5z"/><path d="M3.5 7.5 12 12l8.5-4.5M12 12v9"/>'),
    "ICON_SNOW": SVG('<path d="M12 2.5v19M4 7l16 10M20 7 4 17"/><path d="m9.5 4 2.5 2 2.5-2M9.5 20l2.5-2 2.5 2"/>'),
    "ICON_SHIP": SVG('<path d="M3 15h18l-2.5 5h-13z"/><path d="M6 15V8h12v7M9 8V4h6v4"/>'),
    "ICON_VAC": SVG('<rect x="4" y="5" width="16" height="14" rx="2.5"/><ellipse cx="9.5" cy="12" rx="2.3" ry="3.4"/><ellipse cx="14.5" cy="12" rx="2.3" ry="3.4"/>', 34),
    "ICON_BAG": SVG('<path d="M5 8h14l-1.2 12.5H6.2z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>', 34),
    "ICON_LABEL": SVG('<path d="M3.5 12.2 11.8 4H20v8.2L11.8 20.5z"/><circle cx="15.8" cy="8.2" r="1.5"/>', 34),
}

def faq_items(d):
    out = []
    for i in range(1, FAQ_COUNT + 1):
        q, a = html.escape(d[f"faq.q{i}"], quote=False), html.escape(d[f"faq.a{i}"], quote=False)
        out.append(
            f'          <details class="faq__item"{" open" if i == 1 else ""}>\n'
            f'            <summary><h3>{q}</h3><span class="faq__icon" aria-hidden="true"></span></summary>\n'
            f'            <p>{a}</p>\n'
            f'          </details>')
    return "\n".join(out)

def harvest_months(d):
    out = []
    for i, st in enumerate(HARVEST):
        full, short = d["months"][i], d["monthsShort"][i]
        label = d[f"harvest.st.{st}"]
        out.append(
            f'            <li class="hm hm--{st}">'
            f'<span class="hm__name"><span aria-hidden="true">{html.escape(short)}</span><span class="sr">{html.escape(full)}</span></span>'
            f'<span class="hm__bar"><span class="hm__st">{html.escape(label)}</span></span>'
            f'<span class="hm__avail" aria-hidden="true"></span></li>')
    return "\n".join(out)

HREFLANG = "\n".join(
    [f'  <link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS]
    + [f'  <link rel="alternate" hreflang="x-default" href="{url(LANGS[0])}">'])

def lang_links(cur):
    out = []
    for l in ["en", "fr", "es"]:   # display order EN / FR / ES
        attrs = ' aria-current="page"' if l == cur else ''
        out.append(f'          <a href="{rel_link(cur, l)}" hreflang="{l}" lang="{l}"{attrs}>{l.upper()}</a>')
    return "\n".join(out)

TPL = (ROOT / "tools/index.template.html").read_text(encoding="utf-8")

def render(lang):
    d = T[lang]
    s = TPL
    s = s.replace("{{LD_ORG}}", json.dumps(org_ld(lang), ensure_ascii=False, indent=2))
    s = s.replace("{{LD_FAQ}}", json.dumps(faq_ld(lang), ensure_ascii=False, indent=2))
    s = s.replace("{{FAQ_ITEMS}}", faq_items(d))
    s = s.replace("{{HARVEST_MONTHS}}", harvest_months(d))
    s = s.replace("{{WA}}", html.escape(wa(lang)))
    s = s.replace("{{LANG}}", lang)
    s = s.replace("{{SITE}}", SITE)
    s = s.replace("{{P}}", prefix(lang))
    s = s.replace("{{CANONICAL}}", url(lang))
    s = s.replace("{{HREFLANG}}", HREFLANG)
    s = s.replace("{{LANG_LINKS}}", lang_links(lang))
    s = s.replace("{{OG_ALT}}", "\n".join(
        f'  <meta property="og:locale:alternate" content="{T[l]["meta.ogLocale"]}">' for l in LANGS if l != lang))
    for k, v in ICONS.items():
        s = s.replace("{{" + k + "}}", v)
    s = re.sub(r"\{\{([a-zA-Z0-9_.]+)\}\}", lambda m: html.escape(d[m.group(1)]), s)
    assert "{{" not in s, lang
    return s

for lang in LANGS:
    out = ROOT / "index.html" if PATHS[lang] == "/" else ROOT / PATHS[lang].strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(lang), encoding="utf-8")
    print("generated", out.relative_to(ROOT))

alts = "\n".join(
    [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{url(l)}"/>' for l in LANGS]
    + [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url(LANGS[0])}"/>'])
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<!-- Generated by tools/build.py -->',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for l in LANGS:
    sm += ["  <url>", f"    <loc>{url(l)}</loc>", f"    <lastmod>{LASTMOD}</lastmod>", alts, "  </url>"]
sm.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
print("generated sitemap.xml")
