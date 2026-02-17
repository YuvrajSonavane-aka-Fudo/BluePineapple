
#* write a python program to split a list a very nth element

def split_at_nth_elements(lst1 , n):
    '''
    Input - Accepts list and nth element
    Output - returns a list of lists

    This functions spilts the elements at nth elements 
    '''
    
    if n <= 0:
        return "n must be greater than 0"
    
    result = []
    # Step through the list in increments of n
    for i in range(0, len(lst1), n):
        # Slice from current index to index + n
        result.append(lst1[i : i + n])
    return result

print(split_at_nth_elements([1,2,3,4,5],2))


        