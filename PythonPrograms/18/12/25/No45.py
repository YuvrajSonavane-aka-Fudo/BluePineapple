#gcd of array
import math
def findGCD(list1):
    list1.sort()
    for i in list1:
        if i%list1[0] == 0:
            continue
        else:
            return 1
    return list1[0]


print(findGCD([2,3,4]))