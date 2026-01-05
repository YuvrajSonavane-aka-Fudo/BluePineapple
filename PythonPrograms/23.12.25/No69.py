#check if a given list contains a sublist or not

def check(list1 , sublist1):

    if sublist1 in list1:
        return True
    else:
        return False
    
list1 = [[1,2,3] , [2,3,4]]
sublist1 = [2,3,5]

print(check(list1 , sublist1))