
#*extract maximum and minimum k elements
lst = [1,2,3,4,6]
def extract_max_min_k_elements(lst , k):
    '''
    returns a list of max k elements and min k elements. 

    '''
    if k<0:
        return -1
    if lst == []:
        return 0
        
    result = sorted(lst)
    max_elements = result[-1:-k-1:-1]
    min_elements = result[:k]
    return list((max_elements , min_elements))

print(extract_max_min_k_elements(lst , 2))