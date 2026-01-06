
#!count elements that occur singly
import collections
def singly(tup):
    countOfsinglyElement = 0
    count = collections.Counter(tup)
    for k , v in count.items():
        if v == 1:
            countOfsinglyElement +=1
    return countOfsinglyElement


print(singly((1,2,2,3)))