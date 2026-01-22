
#*first even number in a given list of numbers
lst = [1,3,5,7]
def first_even_number(lst):
    ''' Returns first even number and index as a tuple respectively. Returns 0 if none found'''
    for i in range(len(lst)):
        if lst[i] %2 == 0:
            return (lst[i] , i)
    return 0
    
print(first_even_number(lst))