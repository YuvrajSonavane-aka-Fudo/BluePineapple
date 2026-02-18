
#* python function to check if list contains unique elements

def is_unique(lst):
    '''Returns true if elements in a list are unique . Else returns false'''
    set1 = set()
    for i in lst:
        if i not in set1:
            set1.add(i)
        else:
            return False
    return True

print(is_unique([1,2,3,4]))