def getpos(s,x):
    i = 0
    while not s[i] == x :
        i += 1
    return i

def proglam1(v):
    i = 0
    next1 = 0
    priority = 10
    while not v[i] == 1:
        if priority < v[i]:
            next1 = i
            priority = v[i]
        i += 1
    return print(next1)

def proglam2(s,v):
    i = getpos(s,">") - 1
    next1 = 0
    priority = 11
    while not v[i] == 0:
        if priority <= v[i]:
            next1 = i
            priority = v[i]
        i -= 1
    return print(next1)

def proglam3(from1,move,s,v):
    to = getpos(s,">")
    if move > 0:
        for i in range(to,from1 - 1,-1):
            if i < len(s):
                s[i + move] = s[i]
                v[i + move] = v[i]
    if move < 0:
        for i in range(from1,to + 1,1):
            if i < len(s):
                s[i + move] = s[i]
                v[i + move] = v[i]
    s1 = s[getpos(s,">")+1:]
    v1 = v[getpos(s,">")+1:]
    for r in s1:
        s.remove(r)
    for r in v1:
        v.remove(r)
    print(s,"\n",v)

v = [0,2,2,2,10,2,2,2,3,11,3,3,11,2,2,2,3,1]
s = list("<Ans=wk#2+10+wk#1>")
from1 = 12
move = -3
proglam3(from1,move,s,v)
