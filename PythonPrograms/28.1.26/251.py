
#*insert before each element

def inserter(element , list1):
    ''' Inserts the element before each item in the list'''
    result = []
    for i in list1:
        result.extend([element , i])
    return result

print(inserter(1, [2,4,4]))