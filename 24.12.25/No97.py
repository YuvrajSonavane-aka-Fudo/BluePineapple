#freq count of list of lists
import collections
def find(list1):
    list2 = []

    for i in list1:
        dict1  =  collections.defaultdict(int)
        for j in range(len(i)):
            dict1[j] +=1
        list2.append(dict1)
    return list2

print(find([[1,2,3],[2,2,3]]))