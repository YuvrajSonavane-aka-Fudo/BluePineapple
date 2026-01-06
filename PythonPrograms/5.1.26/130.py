#fnd item with max freq in a list
import collections
def findMaxFreq(lst):
    if lst == []:
        return 0
    
    dict1 = collections.defaultdict(int)

    for i in lst:
        dict1[i] +=1 

    maxItem = None
    maxVal = 0

    for k, v in dict1.items():
        if v > maxVal:
            maxVal = v
            maxItem = k
    return (maxItem , maxVal)

    

print(findMaxFreq([1,2,3,5,5,5,5,5]))


