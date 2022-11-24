pattern = list("*008.00#")
value = list("00012+")
fill = pattern[0]
signif = "off"
v = 0
for p in range(0,len(pattern),1):
    if pattern[p] == "0" or pattern[p] == "8":
        if signif == "off":
            if pattern[p] == "0" and value[v] == "0":
                pass
            else:
                if not value[v+1] =="+":
                    signif = "on"
            if value[v] == "0":
                pattern[p] = fill
            else:
                pattern[p] = value[v]
        else:
            if value[v+1] == "+":
                signif = "off"
            pattern[p] = value[v]
        v += 1
    else:
        if signif == "off":
            pattern[p] = fill
    print(pattern)
