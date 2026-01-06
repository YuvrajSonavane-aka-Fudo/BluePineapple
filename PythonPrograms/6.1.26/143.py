
#!find number of lists in given tuple

def findNumber(tup):
    count = 0
    for i in tup:
        if isinstance(i , list):
            count+=1

    return count

print(findNumber(([] , 1, [2,3])))