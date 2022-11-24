list1 = list("_.,?abcdefghijklmnopqrstuvwxyz")
def getvalue(x):
    return list1.index(x)

def getchar(x):
    return list1[x]

def calccheckcharacter(input1,len1):
    n = 30
    sum1 = 0
    is_even = False
    for i in range(len1,-1,-1):
        value = getvalue(input1[i])
        if is_even == True:
            sum1 = sum1 + value
        else:
            sum1 = sum1 + (value * 2) // n + (value * 2) % n
        is_even = not is_even
    check_value = (n - sum1 % n) % n
    return print(getchar(check_value))

def validatacheckcharacter(input1,len1):
    n = 30
    sum1 = 0
    is_odd = True
    ret_value = True
    for i in range(len1,-1,-1):
        value = getvalue(input1[i])
        if is_odd == True:
            sum1 = sum1 + value
        else:
            sum1 = sum1 + (value * 2) // n +(value * 2) % n
        is_odd = not is_odd
    if not sum1 % n == 0:
        ret_value = False
    return print(ret_value)

input1 = list("ipa__f")

validatacheckcharacter(input1,len(input1)-1)

