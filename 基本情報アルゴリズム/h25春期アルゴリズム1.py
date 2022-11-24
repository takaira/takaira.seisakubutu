def SearchUpdate(buy,ptr,buylen,target,spe,targetlen,sale):
    #検索部
    k = ptr
    t = 0
    while k >= 0 and t <= targetlen - 1:
        if buy[k][1] == target[t][0]:
            target[t][1] = buy[k][4]
            k = buy[k][0]
            t += 1
        else:
            if buy[k][1] < target[t][0]:
                k = buy[k][0]
            else:
                t += 1
    #計算部
    w = 0
    for t in range(0,targetlen,1):
        w = w + target[t][1]
    sale[3] = w // spe
    #更新部
    kp = 0
    k = ptr
    while k >= 0 and buy[k][1] < sale[0]:
        kp = k
        k = buy[k][0]
    if sale[3] > 0 and (k == 0 or buy[k][1] > sale[0]):
        buylen += 1
        if kp > 0:
            buy[kp][0] = buylen
        else:
            ptr = buylen
        buy[buylen][0] = k
        buy[buylen][1] = sale[0]
        buy[buylen][2] = sale[1]
        buy[buylen][3] = sale[2]
        buy[buylen][4] = sale[3]
        buy[buylen][5] = sale[2] * sale[3]
    if sale[3] > 0 and k > 0 and buy[k][1] == sale[0]:
        buy[k][4] = sale[3]
        buy[k][5] = sale[2] * sale[3]
    if sale[3] == 0 and k > 0 and buy[k][1] == sale[0]:
        if kp > 0:
            buy[kp][0] = buy[k][0]
        else:
            ptr = buy[k][0]
    print("ptr起点",ptr)
    print("購入行数",buylen)
    for i in range(0,6,1):
        print(buy[i])
    print("指定数量",spe)
    print("対象行数",targetlen)
    for i in range(0,3,1):
        print(target[i])
    print(sale)

buy = [[3,222,"B社緑茶 500ml",140,5,700],[0,111,"A社牛乳 1000ml",200,2,400],
       [-1,335,"C社めんつゆ 300g",150,1,150],[4,224,"B社麦茶 500ml",140,2,280],
       [2,333,"C社うどん2食入り",180,2,360],[0,0,0,0,0,0]]
ptr = 1
buylen = 4
target = [[222,0],[223,0],[224,0]]
spe = 3
targetlen = 3
sale = [229,"B社お茶3本100円引",-100,0]

SearchUpdate(buy,ptr,buylen,target,spe,targetlen,sale)
