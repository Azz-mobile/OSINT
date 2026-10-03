from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import re

def check(item, username):
    url=item["url"].format(username=username)
    req=Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; AZZ-OSINT/2.0)"})
    try:
        with urlopen(req,timeout=8) as r:
            code=r.status
            # Some sites return generic pages or anti-bot pages with 200.
            if code==200:
                return {**item,"url":url,"status":"FOUND","http_status":code}
            return {**item,"url":url,"status":"UNKNOWN","http_status":code}
    except HTTPError as e:
        if e.code in (401,403,429,451):
            return {**item,"url":url,"status":"UNKNOWN","http_status":e.code}
        if e.code==404:
            return {**item,"url":url,"status":"NOT FOUND","http_status":e.code}
        return {**item,"url":url,"status":"UNKNOWN","http_status":e.code}
    except (URLError,TimeoutError,ConnectionError) as e:
        return {**item,"url":url,"status":"UNKNOWN","http_status":None,"error":str(e)}

def normalize_username(u):
    return re.sub(r"[^A-Za-z0-9._-]","",u.strip().lstrip("@"))[:64]
