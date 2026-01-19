
#*binary search

def binary_recursion(start , end , number , lst):
        if start > end:
            return -1 
        mid = (end + start)//2
        if lst[mid] == number:
            return mid
        
        if number < lst[mid]:
            return binary_recursion(start , mid-1 , number , lst)
        
        if number > lst[mid]:
            return binary_recursion(mid+1 , end , number , lst)
        

def binary_search(number , lst):
    '''Accepts a list and number to be found . Returns the index it is found in the list else returns -1 if not found'''
    return binary_recursion(0,len(lst)-1, number , lst)



print(binary_search(6, [1,2,3,4,5]))