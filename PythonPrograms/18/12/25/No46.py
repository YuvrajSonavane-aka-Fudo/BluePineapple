#check if all elements are different or not

def check(list1):
    list2 = list(filter(lambda x : list1.count(x) < 2 , list1))
    if list1 == list2:
        return True
    else:
        return False
print(check([1,2,3,3]))