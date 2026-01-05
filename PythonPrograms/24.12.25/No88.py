#freq of elements in a given list
from collections import defaultdict
def calFreq(list1):
    dict1 = defaultdict(int)

    for i in list1:
        dict1[i] += 1

    return dict1

print(calFreq([1,1,1,2 , -6]))