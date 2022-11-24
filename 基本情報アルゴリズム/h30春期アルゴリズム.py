def lchild(i):
    return 2*i+1

def rchild(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def swap(heap,i,j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp

def makeheep(data,heap,hnum):
    for i in range(0,hnum,1):
        heap[i] = data[i]
        k = i
        while k > 0:
            if heap[k] > heap[parent(k)]:
                swap(heap,k,parent(k))
                k = parent(k)
            else:
                break
    print(heap)

def downheap(heap,hlast):
    n = 0
    while lchild(n) <= hlast:
        tmp = lchild(n)
        if rchild(n) <= hlast:
            if heap[tmp] <= heap[rchild(n)]:
                tmp = rchild(n)
        if heap[tmp] > heap[n]:
            swap(heap,n,tmp)
        else:
            return
        n = tmp

def heapsort(data,heap,hnum):
    makeheep(data,heap,hnum)
    for last in range(hnum-1,0,-1):
        swap(heap,0,last)
        downheap(heap,last-1)
    print(heap)

data = [1,5,6,7,8,9,2]
heap = [0,0,0,0,0,0,0]
hnum = len(data)

heapsort(data,heap,hnum)
