
#!remove all elements of a given list present in another list

lst1 = [1,2,3,4,5]
lst2 = [2,3]

def remove_elements(lst1 , lst2):
    temp = []
    for i in lst1:
        if i not in lst2:
            temp.append(i)
    return temp

print(remove_elements(lst1, lst2))