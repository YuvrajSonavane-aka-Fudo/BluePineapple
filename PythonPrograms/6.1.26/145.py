
#!find max difference between two elements 

def findMaxDiff(lst):
    min1 = min(lst)
    max1 = max(lst)

    return max1-min1

print(findMaxDiff([1,2,3,7]))