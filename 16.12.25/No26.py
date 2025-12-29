k = [1,2,5,4  , 22/7]
tup1 = (1,2,3,4,5,6 ,22/7)

def check(k , tup1):
    if k == [] and tup1 == ():
        return True
    elif k == [] or tup1 == ():
        return False
    
    for i in k:
        if i not in tup1:
            return False
    return True

print(check(k , tup1))

