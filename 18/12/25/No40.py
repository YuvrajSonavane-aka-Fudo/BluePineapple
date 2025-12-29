import collections

list1 = [[1,2,3],[2,3,4]]

def countFreq(list1):
    freq = []
    for i in list1:
        freq.extend(i)
    return collections.Counter(freq)

print(countFreq(list1))