
#! sum of negative numbers in a list using lambda

def sumOfNeg(lst):
    if lst == []:
        return 0
    
    return sum(filter(lambda x : x<0 , lst))

print(sumOfNeg([1,2,-4,-5]))