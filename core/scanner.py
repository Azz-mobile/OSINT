import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from modules.checker import check,normalize_username
from modules.variants import variants
from modules.search import make_searches
from core.reporter import save

def scan(username,workers=12):
    u=normalize_username(username)
    cfg=Path(__file__).resolve().parent.parent/"config/platforms.json"
    platforms=json.loads(cfg.read_text(encoding="utf-8"))
    out=[]
    with ThreadPoolExecutor(max_workers=max(1,min(20,workers))) as ex:
        fs=[ex.submit(check,p,u) for p in platforms]
        for f in as_completed(fs): out.append(f.result())
    order={p["name"]:i for i,p in enumerate(platforms)}
    out.sort(key=lambda x:order[x["name"]])
    counts={k:sum(x["status"]==k for x in out) for k in ("FOUND","NOT FOUND","UNKNOWN")}
    r={"tool":"AZZ Universal Username OSINT","version":"2.0","target":u,
       "timestamp_utc":datetime.now(timezone.utc).isoformat(),
       "platforms":out,"counts":counts,"variants":variants(u),
       "searches":make_searches(u),
       "notice":"Public-source reconnaissance only. Validate leads manually; username reuse does not prove identity."}
    r.update(save(r)); return r
