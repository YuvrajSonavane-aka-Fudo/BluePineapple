#multiply all nums of list and then divide that by len of list

def mulDiv(list1):
    len1 = len(list1)
    mul1 = 1
    for i in list1:
        mul1*=i
    return mul1/len1

print(mulDiv([1,2,3]))