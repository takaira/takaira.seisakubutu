def bmmatch(text,textlen,pat,patlen):
    skip = []
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(0,26,1):
        skip.append(patlen)
    for i in range(0,patlen-1,1):
        skip[alpha.index(pat[i])] = patlen - i - 1
    print(skip)
    plast = patlen
    while plast <= textlen:
        ptext = plast
        ppat = patlen
        print("ptext=",ptext)
        print("ppat=",ppat)
        print("plast=",plast)
        while text[ptext - 1] == pat[ppat - 1]:
            if ppat == 1:
                return print(ptext)
            ptext -= 1
            ppat -= 1
        plast += skip[alpha.index(text[plast - 1])]
    return print(-1)

text = list("ABCXBBACABACADEC")
pat = list("ABAC")
textlen = len(text)
patlen = len(pat)

bmmatch(text,textlen,pat,patlen)
