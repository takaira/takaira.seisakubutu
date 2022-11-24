import decimal

decimal.getcontext().prec = 7

def nyuton1(x,a3,a2,a1,a0):
    b2 = 3 * a3
    b1 = 2 * a2
    b0 = a1
    for i in range(0,100,1):
        f = ((a3 * x + a2) * x + a1) * x + a0
        d = (b2 * x + b1) * x + b0
        print(x,f,d)
        x = x - f / d
    print(x,f,d)

def nyuton2(n,x,a):
    b = [0,0,0,0]
    for k in range(n,0,-1):
        b[k-1] = k * a[k]
    print(b)
    for i in range(0,100,1):
        f = a[n] * x + a[n-1]
        d = b[n-1]
        for k in range(n-2,-1,-1):
            f = f * x + a[k]
            d = d * x + b[k]
        print(x,f,d)
        x = x - f / d

n = 4
x = 2.00001
a4 = 1
a3 = -8
a2 = 24
a1 = -32
a0 = 16
a = [a0,a1,a2,a3,a4]

nyuton2(n,x,a)
