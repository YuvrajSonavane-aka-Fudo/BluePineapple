#convert all possible convertible elements into float
#now i will assume only int and double can converted to float and rest will remain the same

def flatten(lst):#takes care of nested lists
    res = []
    for i in lst:
        if isinstance(i , (list,tuple , dict)):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

def covertToFloat(lst):
    lst = flatten(lst)
    for i in range(len(lst)):
        if isinstance(lst[i] , (int , complex)):
            lst[i] = float(lst[i])

    return lst

print(covertToFloat([1,2,[55] ,(1,2,3),{1:0} ,"abc"])) 