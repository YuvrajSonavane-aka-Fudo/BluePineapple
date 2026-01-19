
#* remove duplicates

def remove_duplicates(tup1):
    '''Accepts a tuple. Returns a tuple without duplicates'''
    return tuple(set(tup1))

print(remove_duplicates((1,2,2,3,4)))