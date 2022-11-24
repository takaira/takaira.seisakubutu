def select(x,n,k):
    top = 0
    last = n
    while top < last:
        pivot = x[k]
        i = top
        j = last
        while True:
            while x[i] < pivot:
                i += 1
            while pivot < x[j]:
                j -= 1
            if i >= j:
                break
            work = x[i]
            x[i] = x[j]
            x[j] = work
            i += 1
            j -= 1
        if i <= k:
            top = j + 1
        if k <= j:
            last = i - 1
    return x[k]

x = [1,3,2,4,2,2,2]
n = 6
k = 2

print(select(x,n,k))
