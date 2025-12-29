def duplicate(list1):
    set1 = set()
    for i in list1:
        if i in set1:
            return "Yes , contains duplicate"
        else:
            set1.add(i)
    return "No duplicates"
    
print(duplicate([1,2,3,4,2,2,3]))
    


