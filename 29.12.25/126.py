""" sum of common divisors """
def findDiv(a):
    lst = []
    for i in range(2,a):
        if a%i==0:
            lst.append(i)
    return lst

def findSum(a,b):
    lst1 = findDiv(a)
    lst2 = findDiv(b)
    lst1.extend(lst2)
    return sum(lst1)

    

print(findSum(4 , 8))
