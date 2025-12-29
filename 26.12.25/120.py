#max prod of tuples in a given list

lst = [(1,2),(2,3)]

def prod(tup1):
    if tup1 == ():
        return 0
    res = 1
    for i in tup1:
        res *= i
    return res

def maxProd(lst):
    try:
        max1 = []
        for i in lst:
            max1.append(prod(i))
        return max(max1)
    except:
        return "Invalid Input"



print(maxProd(lst))


