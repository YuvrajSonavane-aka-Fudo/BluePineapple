
#*exponentiation of two given tuples

def exponentiation(tup1 , tup2):
    '''Accepts two tuples . Returns a result tuple of the exponentiation'''
    result = ()
    result = tuple(map(lambda x ,y : x**y , tup1 , tup2))
    return result

print(exponentiation((1,2,3) , (1,2,3)))
