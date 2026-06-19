#!/usr/bin/env python3
"""
SpaceLink Spec Pack builder.
Converts a Markdown doc into a branded, self-contained HTML page that matches
SpaceLink's design tokens and links back to the Spec Pack hub (index.html).

Usage:
    python3 build_pack.py <input.md> <output.html> "Page Title" "Short subtitle"

This is the reusable converter behind the Spec Pack. To add a new document:
1. Drop the .md file in this folder.
2. Run this script to produce a branded .html page.
3. Add a card link to it in index.html.
4. Re-drop the whole folder onto Netlify.
"""
import sys, re, markdown

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SpaceLink · {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root{{
    --indigo:#4f46e5; --purple:#7c3aed; --indigo-dark:#3730a3;
    --grad:linear-gradient(135deg,#4f46e5,#7c3aed);
    --bg:#f8fafc; --ink:#1f2937; --muted:#6b7280; --line:#e5e7eb;
    --card:#ffffff; --radius:12px;
    --shadow:0 1px 3px rgba(16,24,40,.08),0 1px 2px rgba(16,24,40,.04);
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{scroll-behavior:smooth}}
  body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;-webkit-font-smoothing:antialiased}}
  .topbar{{position:sticky;top:0;z-index:50;background:rgba(248,250,252,.9);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
  .topbar .row{{max-width:860px;margin:0 auto;padding:0 24px;height:56px;display:flex;align-items:center;justify-content:space-between}}
  .back{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;color:var(--indigo);font-weight:600;font-size:.9rem}}
  .back:hover{{color:var(--indigo-dark)}}
  .brand{{display:flex;align-items:center;gap:8px;font-weight:800;font-size:.95rem;color:var(--ink)}}
  .logo{{width:26px;height:26px;border-radius:7px;background:var(--grad);display:grid;place-items:center;color:#fff;font-weight:800;font-size:.85rem}}
  .hero{{background:var(--grad);color:#fff;padding:48px 0 54px}}
  .hero .row{{max-width:860px;margin:0 auto;padding:0 24px}}
  .eyebrow{{display:inline-block;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;background:rgba(255,255,255,.18);padding:5px 11px;border-radius:999px;margin-bottom:14px}}
  .hero h1{{font-size:2.1rem;font-weight:800;letter-spacing:-.02em;line-height:1.15}}
  .hero .sub{{margin-top:12px;font-size:1.04rem;color:rgba(255,255,255,.92);max-width:62ch}}
  main{{max-width:860px;margin:0 auto;padding:44px 24px 10px}}
  .doc h1{{font-size:1.6rem;font-weight:800;margin:34px 0 10px;letter-spacing:-.01em}}
  .doc h1:first-child{{display:none}}  /* title already in hero */
  .doc h2{{font-size:1.32rem;font-weight:800;margin:38px 0 8px;padding-top:10px;letter-spacing:-.01em}}
  .doc h3{{font-size:1.08rem;font-weight:700;margin:26px 0 6px;color:var(--indigo-dark)}}
  .doc p{{margin:12px 0}}
  .doc ul,.doc ol{{margin:12px 0 12px 22px}}
  .doc li{{margin:5px 0}}
  .doc strong{{color:var(--ink);font-weight:700}}
  .doc em{{color:var(--muted)}}
  .doc a{{color:var(--indigo);font-weight:500}}
  .doc hr{{border:0;border-top:1px solid var(--line);margin:30px 0}}
  .doc table{{width:100%;border-collapse:collapse;margin:20px 0;background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;font-size:.92rem}}
  .doc th,.doc td{{text-align:left;padding:11px 14px;border-bottom:1px solid var(--line);vertical-align:top}}
  .doc th{{background:#f9fafb;font-size:.76rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);font-weight:700}}
  .doc tr:last-child td{{border-bottom:0}}
  .doc blockquote{{border-left:4px solid var(--purple);background:#faf5ff;border-radius:0 10px 10px 0;padding:14px 18px;margin:18px 0;color:#4b5563;font-size:.93rem}}
  .doc blockquote p{{margin:4px 0}}
  .doc code{{background:#eef2ff;color:var(--indigo-dark);padding:2px 6px;border-radius:5px;font-size:.88em;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}
  .doc pre{{background:#111827;color:#e5e7eb;padding:18px 20px;border-radius:var(--radius);overflow:auto;margin:18px 0;font-size:.86rem;line-height:1.5}}
  .doc pre code{{background:none;color:inherit;padding:0}}
  footer{{max-width:860px;margin:24px auto 0;padding:24px;border-top:1px solid var(--line);color:var(--muted);font-size:.82rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}}
  .draft{{background:#fef3c7;color:#92400e;font-size:.72rem;font-weight:600;padding:4px 11px;border-radius:999px}}
  @media(max-width:680px){{.hero h1{{font-size:1.6rem}}}}
</style>
</head>
<body>
  <div class="topbar"><div class="row">
    <a class="back" href="index.html">&larr; Spec Pack</a>
    <span class="brand"><span class="logo">S</span> SpaceLink</span>
  </div></div>
  <header class="hero"><div class="row">
    <span class="eyebrow">SpaceLink · Working Spec</span>
    <h1>{title}</h1>
    {subtitle_html}
  </div></header>
  <main>
    <div class="doc">
{body}
    </div>
    <footer>
      <span>SpaceLink · prepared for the design &amp; build team (Codeaza)</span>
      <span class="draft">DRAFT — for discussion</span>
    </footer>
  </main>
</body>
</html>
"""

def convert(md_path, out_path, title, subtitle):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # If subtitle not given, try to pull the first italic line under the H1
    if not subtitle:
        m = re.search(r"^\*(.+?)\*\s*$", text, re.MULTILINE)
        if m:
            subtitle = m.group(1).strip()
            text = text.replace(m.group(0), "", 1)
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
    subtitle_html = f'<p class="sub">{subtitle}</p>' if subtitle else ""
    html = TEMPLATE.format(title=title, subtitle_html=subtitle_html, body=body)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    md, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
    subtitle = sys.argv[4] if len(sys.argv) > 4 else ""
    convert(md, out, title, subtitle)
