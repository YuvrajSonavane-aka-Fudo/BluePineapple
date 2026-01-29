
#* maximize two given tuples

def maximize_two_tuples(tup1 , tup2):
    '''
        Returns a tuple containing the max of each position in both the tuples

    '''

    result = tuple(map(max , zip(tup1 , tup2)))
    return result

print(maximize_two_tuples((1,2,3) , (0,4,2)))

