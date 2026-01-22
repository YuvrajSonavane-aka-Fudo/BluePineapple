import collections
#*find majority element in sorted array

def return_majority_element(arr):
    ''' Returns the majority element i.e the element with the most occurances'''
    dict1 = collections.defaultdict(int)
    for i in arr:
        dict1[i] +=1 
    maxVal = 0
    maxK = 0
    for k,v in dict1.items():
        if v > maxVal:
            maxVal = v
            maxK = k
    return (maxK , maxVal)


print(return_majority_element([1,2,3,4,4,4,6,7,8,9,12]))

