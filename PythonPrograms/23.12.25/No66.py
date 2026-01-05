#count of positive

def countPositive(list1):
    if list1 == []:
        return 0
    
    cnt = len(list(filter(lambda x : x>=0 , list1)))
    return (cnt)

print(countPositive([1,2,3,-4,-5]))
