
#* division operation across given tuples

def perform_division_across_tuples(tup1 , tup2):
    '''
        Performs division and returns a tuple

    '''
    try :
        result = tuple(map(lambda x , y : x/y, tup1 , tup2))
        return result
    except :
        return "Please ensure the second tuple does not contain zeroes"

print(perform_division_across_tuples((6,8,9) , (2,0,3)))
