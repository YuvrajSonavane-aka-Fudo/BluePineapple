
#*check whether elements is a list are same or not

def are_elements_same(lst):
    '''Accepts a list . Checks if all elements are same . Returns bool value'''
    temp = lst[0]
    for i in lst:
        if i!=temp:
            return False
    return True

print(are_elements_same([1,1,1]))

