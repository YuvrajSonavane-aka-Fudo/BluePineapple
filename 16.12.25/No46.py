def allDifferentNumbers(list1):
    set1 = set()
    for i in list1:
        if i in set1:
            return False
        else:
            set1.add(i)
    return True

print(allDifferentNumbers([1,2,4,3,4,5]))