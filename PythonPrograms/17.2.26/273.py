
#* subtract elements of tuple with corresponding tuple

def subtract_elements(tup1 , tup2):
    result = list(map(lambda x, y : x - y ,tup1, tup2))
    return result

print(subtract_elements((4,5,6) , (1,2,3)))
