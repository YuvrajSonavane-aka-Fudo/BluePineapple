
#* inversions of tuple in a list

lst = [(1,2,3) , (4,5,6)]

def inverter(lst)->lst:
    '''Accepts a list . inverts the tuples inside the list and returns a lst again'''
    result = []
    for i in lst:
        temp = tuple(reversed(i))
        result.append(temp)
    return result

print(inverter(lst))