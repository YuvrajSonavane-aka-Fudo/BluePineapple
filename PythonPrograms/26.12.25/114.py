import collections
#assign freq to each tuple in tuple list
tup1 = ((1,2,5,6,2,3),(4,5,6))

def freq(tup1):
    cnt = []
    for i in tup1:
        cnt.append(collections.Counter(i))
    return cnt

print(freq(tup1))