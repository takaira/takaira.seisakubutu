def Init(S,N,K):
    if 1 <= K and K <= N:
        for i in range(1,N+1,1):
            if i <= K:
                S[i-1] = 1
            else:
                S[i-1] = 0
            i += 1
        return 0
    else:
        return -1

def Next(S,N):
    C = 0
    j = 1
    R = -1
    while j < N and R == -1:
        if S[j-1] == 1:
            if S[j] == 0:
                S[j-1] = 0
                S[j] = 1
                Init(S,j-1,C)
                R = 0
            else:
                C +=1
        j += 1
    return R

def Dump(S,N):
    print(S,'\n')

K = 3
N = 5
S = ['','','','','']
R = Init(S,N,K)
while R == 0:
    Dump(S,N)
    R = Next(S,N)
