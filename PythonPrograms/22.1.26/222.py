
#* check if all elements in tuple have the same datatype or not

def are_all_elements_same_dtype(tuple1):
    '''Accepts tuple . Returns true if all elements are same datatype . Else false'''
    set1 = set()
    set1.add(type(tuple1[0]))
    for i in tuple1:
        if type(i) not in set1:
            return False
    return True


print(are_all_elements_same_dtype((1,2,4.00)))