
#*list of all numbers having value greater than specified number

def return_greater_values(lst , k):
    '''Accepts a list and specified value k , returns all values greater than k in a list'''
    result = []
    for i in lst:
        if i>k:
            result.append(i)
    return result

print(return_greater_values([1,2,3,4,5], 2))
