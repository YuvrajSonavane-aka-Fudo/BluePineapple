tup1 = ((1,2,3),(2,4,8) , (12,14,18))

def check(tup1,k):
    for i in tup1:
        if i%k != 0:
            return False
    return True

def biggerCheck(tup1 , k):
    tup2 = tuple(filter(lambda x : check(x , k) , tup1))
    print(tup2)

biggerCheck(tup1 , 1)