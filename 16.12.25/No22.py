def dupElement(arr):
    set1 = set()
    for i in arr:
        if i not in set1:
            set1.add(i)
        else:
            return i

print(dupElement([1,2,3,2,4,5,3]))