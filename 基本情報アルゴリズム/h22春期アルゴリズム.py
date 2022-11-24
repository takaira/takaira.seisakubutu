def merge(slist1,num1,slist2,num2,list1):
    i = 0
    j = 0
    while i < num1 and j < num2:
        if slist1[i] < slist2[j]:
            list1[i + j] = slist1[i]
            i += 1
        else:
            list1[j + i] = slist2[j]
            j += 1
    while i < num1 or j < num2:
        if i < num1:
            list1[i + j] = slist1[i]
            i += 1
        else:
            list1[i + j] = slist2[j]
            j += 1

def sort(list1,num):
    slist1 = []
    slist2 = []
    if num > 1:
        num1 = num // 2
        num2 = num - num1
        for i in range(0,num1,1):
            slist1.append(list1[i])
        for i in range(0,num2,1):
            slist2.append(list1[num1 + i])
        sort(slist1,num1)
        sort(slist2,num2)
        merge(slist1,num1,slist2,num2,list1)

list1 = [5,7,4,2,3,8,1]
sort(list1,len(list1))
print(list1)
