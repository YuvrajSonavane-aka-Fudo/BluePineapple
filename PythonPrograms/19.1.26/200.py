
#*find all indexes of max values in a list

def find_indexes_of_max_values(lst):
    '''Accepts a list of values . Returns a list of indexes '''
    if lst == []:
        return None
    max_value = max(lst)
    result = []
    for i in range(len(lst)):
        if lst[i]==max_value:
            result.append(i)
    return result

    