def calceditdistance(str1,str1len,str2,str2len):
    d = [[0],[0],[0],[0],[0],[0],[0],[0]]
    for x in range(0,str1len+1,1):
        d[x][0] = x
    for y in range(1,str2len+1,1):
        d[0].append(y)
    for x in range(1,str1len+1,1):
        for y in range(1,str2len+1,1):
            if str1[x-1] == str2[y-1]:
                d[x].append(min(d[x-1][y-1],d[x][y-1] + 1,d[x-1][y] + 1))
            else:
                d[x].append(min(d[x][y-1] + 1,d[x-1][y] + 1))
    return print(d[str1len][str2len])

str1 = list("peace")
str2 = list("people")

calceditdistance(str1,len(str1),str2,len(str2))
