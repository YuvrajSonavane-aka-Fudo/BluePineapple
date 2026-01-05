def find(list1):
    return len(min(list1 , key = len))

print(find([[1,2,3],[1]]))