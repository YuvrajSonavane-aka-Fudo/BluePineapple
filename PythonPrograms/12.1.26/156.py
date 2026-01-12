
#!tuple of string values to int values

tup1 = ("1","2")

def tuple_string_to_int(tup1):
    try:
        lst = list(tup1)
        for i in range(len(lst)):
            lst[i] = int(lst[i])
    
        return tuple(lst)
    except():
        raise("Some error occured")

print(tuple_string_to_int(tup1))