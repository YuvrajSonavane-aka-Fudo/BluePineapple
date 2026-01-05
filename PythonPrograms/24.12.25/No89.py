#closest number smaller than n

def find(list1, n):
    while n >= 0:
        if n-1 in list1:
            return n-1
        else:
            n-=1
    return None

print(find([1,2,3,4] , -1))

    