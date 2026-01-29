
#* number of odd elements usin lambda

def filter_odd_elements(lst1):
    '''
        Accepts a list and filters out the odd elements using lambda returns the count of odd elements
    '''

    lst2 = list(filter(lambda x : x%2!=0 , lst1))
    return len(lst2)

print(filter_odd_elements([1,2,3,4,5]))