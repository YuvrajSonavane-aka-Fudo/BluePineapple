
#*function to check if all bits are unset in a given range

def are_all_bits_unset(number , start , end):
    '''
    Accepts a number and checks if all bits are unset within the given the start and end range
    '''
    binary_num = bin(number)
    if start < 0:
        return -1
    if end > len(binary_num):
        return -1
    
    for i in range(start , end):
        if binary_num[i] == "1":
            return False
    return True

print(are_all_bits_unset(5 , 0 ,3))
