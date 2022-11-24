def bittest(data,mask):
    if bin(data & mask) == bin(mask):
        rc = 2
    else:
        if bin(data & mask) == bin(0):
            rc = 0
        else:
            rc = 1
    return print(rc)

def bittest1(data,mask):
    if bin(data & mask) == bin(0):
        rc = 0
    else:
        if bin(data & mask) == bin(mask):
            rc = 2
        else:
            rc = 1
    return print(rc)

def bittest2(data,mask):
    rc = 1
    if bin(data & mask) == bin(0):
        rc = 0
    if bin(data & mask) == bin(mask):
        rc = 2
    else:
        rc = 1
    return print(rc)

def bitcount1(data):
    work = data
    count = 0
    worst = 1
    for loop in range(0,8,1):
        if bin(work & worst) == bin(1):
            count += 1
        work = work >> 1
    return print(count)

def bitcount2(data):
    work = data
    count = 0
    comparison = 0b11111111
    while  not bin(work & comparison) == bin(0):
        count += 1
        work = work & (work -1)
    return print(count)

data = 0b11111111
mask = 0b11111111

bitcount2(data)
