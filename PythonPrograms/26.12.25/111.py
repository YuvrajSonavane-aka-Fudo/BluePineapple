#most common elements from nestedlists
import collections
list1 = [1,2,[2,3,[4,5]] ,7]

def flatten(list1):
    res = []
    for i in list1:
        if isinstance(i , list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

def countMostCommon(res):
    cnt = collections.Counter(res)

    return cnt.most_common()

res = flatten(list1)
print(countMostCommon(res))