
#!calculate same pair in three given lsts

lst1 = [[1,2] ,[2,3]]
lst2 = [[2,3,] , [5,6]]
lst3 = [[3,4],[4,5],[2,3]]

def findSamePair(lst1 , lst2 , lst3):
    if lst1 == [] or lst2 == [] or lst3 == []:
        return []
    
    res = []
    for i in lst1:
        if i in lst2 and i in lst3:
            res.append(i)
    return res

print(findSamePair(lst1,lst2,lst3))

        