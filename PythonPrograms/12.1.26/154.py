
#!extract every specified element in a two dimensional list
#! assuming every specified element as like the first element or third element etc

lst = [[1,2,3] ,[2,3,4] ,[4,5,6]]

def extract_specified_elements(lst , element_index):


    if element_index > len(min(lst , key = len))-1:
        return "index out of range "
    result = []
    for i in lst:
        result.append(i[element_index])
    return result

print(extract_specified_elements(lst , 3))



