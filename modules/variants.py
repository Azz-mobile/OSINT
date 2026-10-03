def variants(u):
    b=u.strip().lstrip("@")
    raw={b,b.lower(),b.replace("_",""),b.replace(".",""),b.replace("-",""),
         b.replace("_","."),b.replace("_","-"),b.replace(".","_"),
         b+"1",b+"01",b+"_", "_"+b, b+"official",b+"real",b+"id"}
    return sorted(x for x in raw if x and len(x)<=30)
