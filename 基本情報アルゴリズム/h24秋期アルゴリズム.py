def calcdist(n,dist):
    print("初期値")
    for i in range(0,n,1):
            print(dist[i])
    for via in range(0,n,1):
        for From in range(0,n,1):
            for to in range(0,n,1):
                if dist[From][to] > dist[From][via] + dist[via][to]:
                    dist[From][to] = dist[From][via] + dist[via][to]
        print("via=",via)
        for i in range(0,n,1):
            print(dist[i])
dist = [[0,18,999,14,999],[18,0,17,999,16],[999,17,0,13,999],
        [14,999,13,0,12],[999,16,999,12,0]]
n = 5

calcdist(n,dist)
