#add list to tuples

tup1 = ((1,2,3),(235,65))

def adder(list1 , tup1):
    if list1 == []:
        return 0

    tup1 = tup1 + tuple(list1)
    return tup1

print(adder([[123] ,1,23],tup1))