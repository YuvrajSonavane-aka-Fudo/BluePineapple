#monotonic

def monotonic(list1):
    #increasing monotonic
    if list1[0]<list1[1]:
        for i in range(1,len(list1)):
            if list1[i-1] > list1[i]:
                return False
    #decreasing monotonic
    if list1[0]>list1[1]:
        for i in range(1,len(list1)):
            if list1[i-1] < list1[i]:
                return False
    return True

print(monotonic([5,4,3,2,6]))