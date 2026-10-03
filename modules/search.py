from urllib.parse import quote_plus
def make_searches(u):
    qs=[
      ("Google",f'"{u}"'),
      ("Google",f'"{u}" Instagram'),
      ("Google",f'"{u}" TikTok'),
      ("Google",f'"{u}" Facebook'),
      ("Google",f'"{u}" Twitter OR X'),
      ("Google",f'"{u}" GitHub'),
      ("Google",f'"{u}" Reddit'),
      ("Google",f'"{u}" YouTube'),
      ("Google",f'"{u}" "email"'),
      ("Google",f'"{u}" -instagram.com'),
      ("Bing",f'"{u}"'),
      ("DuckDuckGo",f'"{u}"'),
    ]
    out=[]
    for engine,q in qs:
        if engine=="Google": url="https://www.google.com/search?q="+quote_plus(q)
        elif engine=="Bing": url="https://www.bing.com/search?q="+quote_plus(q)
        else: url="https://duckduckgo.com/?q="+quote_plus(q)
        out.append({"engine":engine,"query":q,"url":url})
    return out
