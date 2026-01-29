
#*intersection of arrays using lambda function

arr1 = [1,2,3]
arr2 = [2]

def find_intersection_of_arrays(arr1 , arr2):
    '''Returns the intersection as a list '''
    arr3 = list(filter(lambda x : x in arr1 , arr2 ))
    print(arr3)

find_intersection_of_arrays(arr1 , arr2)