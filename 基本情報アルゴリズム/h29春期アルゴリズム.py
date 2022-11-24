def shortestpath(distance,npoint,sp,dp,sroute,sdist):
    sdist = []
    pdist = []
    pfixed = []
    proute = [0,0,0,0,0,0,0]
    for i in range(0,npoint,1):
        sroute.append(-1)
        pdist.append(float('inf'))
        pfixed.append(False)
    pdist[sp] = 0
    while True:
        i = 0
        while i < npoint:
            if not(pfixed[i]):
                break
            i += 1
        if i == npoint:
            break
        for j in range(i+1,npoint,1):
            if not(pfixed[j]) and pdist[j] < pdist[i]:
                i = j
        spoint = i
        print(i)
        pfixed[spoint] = True
        for j in range(0,npoint,1):
            if distance[spoint][j] > 0 and not(pfixed[j]):
                newdist = pdist[spoint] + distance[spoint][j]
                if newdist < pdist[j]:
                    pdist[j] = newdist
                    proute[j] = spoint
        print('pdist=',pdist)
        print('proute=',proute)
    sdist = pdist[dp]
    j = 0
    i = dp
    while not i == sp:
        sroute[j] = i
        i = proute[i]
        j += 1
    sroute[j] = sp
    print(sdist)
    print(sroute)

distance = [[0,2,8,4,-1,-1,-1],[2,0,-1,-1,3,-1,-1],[8,-1,0,-1,2,3,-1],
            [4,-1,-1,0,-1,8,-1],[-1,3,2,-1,0,-1,9],[-1,-1,3,8,-1,0,3],
            [-1,-1,-1,-1,9,3,0]]
npoint = 7
sp = 0
dp = 6
sroute = []
sdist = []
shortestpath(distance,npoint,sp,dp,sroute,sdist)
