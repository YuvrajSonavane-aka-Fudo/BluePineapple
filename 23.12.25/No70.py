#all given tuples have equal length or not

tup1 = ((1,2,3),(2,3))

def check(tup1):
    if tup1 == ():
        return True

    for i in tup1:
        if len(i) != len(tup1[0]):
            return False
    return True

print(check(tup1))
