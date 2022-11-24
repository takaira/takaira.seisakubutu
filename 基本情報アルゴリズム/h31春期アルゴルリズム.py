def sort(freq,nsize):
    global node
    # zipで一つの変数"zip_lists"にまとめる
    # ソートの基準としたいリスト(ここではscores)を一番左においてzip
    zip_lists = zip(freq,node)
    # 昇順でソート
    zip_sort = sorted(zip_lists)
    # zipを解除
    freq,node = zip(*zip_sort)

def sortnode(size,parent,freq):
    global nsize,node
    nsize = 0
    j = 0
    node = []
    for i in range(0,size,1):
        if parent[i] < 0:
            node.append(i)
            nsize += 1
    sort(freq,nsize)
    
def huffman(size,parent,left,right,freq):
    sortnode(size,parent,freq)
    while nsize >= 2:
        #print(parent)
        #print(left)
        #print(right)
        #print(freq)
        #print(node)
        i = node[0]
        j = node[1]
        left[size] = i
        right[size] = j
        freq[size] = freq[i] + freq[j]
        parent[i] = size
        parent[j] = size
        size += 1
        sortnode(size,parent,freq)
    print(parent)
    print(left)
    print(right)
    print(freq)

def encode(k,parent,left):
    if parent[k] >= 0:
        encode(parent[k],parent,left)
        if left[parent[k]] == k:
            print("0")
        else:
            print("1")

size = 4
parent = [-1,-1,-1,-1,-1,-1,-1]
left = [-1,-1,-1,-1,-1,-1,-1]
right = [-1,-1,-1,-1,-1,-1,-1]
freq = [10,2,4,3,-1,-1,-1]

huffman(size,parent,left,right,freq)
encode(3,parent,left)

