
#*adjacent element concatenation in the given tuples

lst = [(1,2,3),(2,5,6)]

def concatenate(lst):
    '''Accepts a list of elements and returns a concatenated list'''
    result = []
    for i in lst:
        result.extend(i)
    return result

print(concatenate(lst))