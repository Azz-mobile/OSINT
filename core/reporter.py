from pathlib import Path
from datetime import datetime
from html import escape
import json
BASE=Path(__file__).resolve().parent.parent/"reports"
def save(r):
    BASE.mkdir(exist_ok=True); safe="".join(c for c in r["target"] if c.isalnum() or c in "._-")[:60]
    stem=BASE/f"{safe}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    jp=stem.with_suffix(".json"); tp=stem.with_suffix(".txt"); hp=stem.with_suffix(".html")
    jp.write_text(json.dumps(r,indent=2,ensure_ascii=False),encoding="utf-8")
    lines=[f"AZZ UNIVERSAL USERNAME OSINT REPORT","="*70,f"Target: {r['target']}",f"Scanned: {len(r['platforms'])} platforms",""]
    cat=None
    for x in r["platforms"]:
        if x["category"]!=cat: cat=x["category"]; lines += ["",cat,"-"*50]
        lines.append(f"[{x['status']}] {x['name']} | {x['url']}")
    lines += ["","Search Engine Queries"]
    for x in r["searches"]: lines.append(f"{x['engine']}: {x['query']} | {x['url']}")
    tp.write_text("\n".join(lines),encoding="utf-8")
    rows=[]
    for x in r["platforms"]:
        cls=x["status"].lower().replace(" ","-")
        rows.append(f"<tr class='{cls}'><td>{escape(x['category'])}</td><td>{escape(x['name'])}</td><td><b>{escape(x['status'])}</b></td><td>{escape(str(x.get('http_status','')))}</td><td><a href='{escape(x['url'])}' target='_blank'>Open</a></td></tr>")
    search_rows="".join(f"<li><b>{escape(x['engine'])}</b> — <a href='{escape(x['url'])}' target='_blank'>{escape(x['query'])}</a></li>" for x in r["searches"])
    hp.write_text(f"""<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>AZZ OSINT - {escape(r['target'])}</title>
<style>
:root{{--bg:#0b1020;--card:#111827;--line:#263244;--txt:#e5e7eb;--muted:#94a3b8;--found:#34d399;--unknown:#fbbf24}}
*{{box-sizing:border-box}}body{{margin:0;background:radial-gradient(circle at top,#18233d,#0b1020 55%);color:var(--txt);font:15px system-ui,-apple-system,Segoe UI,sans-serif}}
.wrap{{max-width:1200px;margin:auto;padding:28px 16px}}.hero,.card{{background:rgba(17,24,39,.88);border:1px solid var(--line);border-radius:18px;box-shadow:0 15px 40px #0005}}
.hero{{padding:28px;margin-bottom:18px}}h1{{margin:0 0 8px;font-size:30px}}.muted{{color:var(--muted)}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:18px 0}}.stat{{padding:18px;background:#0f172a;border:1px solid var(--line);border-radius:14px}}.num{{font-size:26px;font-weight:800}}
.card{{padding:18px;margin:18px 0;overflow:auto}}table{{width:100%;border-collapse:collapse;min-width:760px}}th,td{{padding:11px;border-bottom:1px solid var(--line);text-align:left}}th{{color:var(--muted)}}a{{color:#7dd3fc;text-decoration:none}}.found{{background:#0c2119}}.unknown{{background:#241d08}}.not-found{{opacity:.65}}
.badge{{display:inline-block;padding:4px 9px;border-radius:999px;background:#172033}}code{{color:#a5b4fc}}@media(max-width:700px){{.grid{{grid-template-columns:repeat(2,1fr)}}h1{{font-size:24px}}}}
</style></head><body><div class='wrap'>
<div class='hero'><h1>AZZ Universal Username OSINT</h1><div class='muted'>Public-source reconnaissance report</div><p><b>Target:</b> <code>{escape(r['target'])}</code></p></div>
<div class='grid'><div class='stat'><div class='muted'>Platforms</div><div class='num'>{len(r['platforms'])}</div></div>
<div class='stat'><div class='muted'>FOUND</div><div class='num'>{r['counts']['FOUND']}</div></div>
<div class='stat'><div class='muted'>NOT FOUND</div><div class='num'>{r['counts']['NOT FOUND']}</div></div>
<div class='stat'><div class='muted'>UNKNOWN</div><div class='num'>{r['counts']['UNKNOWN']}</div></div></div>
<div class='card'><h2>Platform Results</h2><table><tr><th>Category</th><th>Platform</th><th>Status</th><th>HTTP</th><th>Link</th></tr>{''.join(rows)}</table></div>
<div class='card'><h2>Search Engine OSINT</h2><ul>{search_rows}</ul></div>
<div class='card'><h2>Username Variants</h2><p><code>{escape(", ".join(r["variants"]))}</code></p></div>
<div class='card'><h2>Methodology</h2><p class='muted'>A FOUND result means the public URL returned a successful HTTP response. NOT FOUND generally corresponds to HTTP 404. UNKNOWN covers rate limiting, authentication walls, access restrictions, network failures, or platforms that cannot be reliably classified from a simple HTTP check.</p><p class='muted'>A username match is only a lead and is not proof that accounts belong to the same person.</p></div>
</div></body></html>""",encoding="utf-8")
    return {"report_json":str(jp),"report_html":str(hp),"report_txt":str(tp)}
