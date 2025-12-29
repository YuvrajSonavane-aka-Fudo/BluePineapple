#i will find the index of the tuple with the least len

def find(tup1):
    min1 = min(tup1  , key = len)
    return tup1.index(min1)

print(find(((1,2,3) , (2,4))))
