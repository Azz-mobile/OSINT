import argparse
from core.ui import banner,print_results
from core.scanner import scan
def main():
    p=argparse.ArgumentParser(description="AZZ Universal Username OSINT")
    p.add_argument("username",nargs="?")
    p.add_argument("--workers",type=int,default=12)
    a=p.parse_args(); banner()
    u=a.username or input("Username > ").strip()
    if not u: return 1
    print(f"\n[*] Checking {u} across 60+ public profile URLs...\n")
    r=scan(u,a.workers); print_results(r)
if __name__=="__main__": raise SystemExit(main())
