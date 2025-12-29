#extract every first or specified element in a two dimensional list

list1 = [[1,2,3], [2,3,4]]

def extract(list1 , n):
    if n > len(list1):
        return -1
    if n<0 :
        return -1
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][n])
    return list2

print(extract(list1,3))