
#*function to check if a numbers oth and nth bits are set or not ?

def is_oth_nth_bit_set(number , n):
    '''Accepts a number and checks if 0th bit and nth bit is set or not . Returns True if yes else False'''
    if n<0 :
        return -1
    
    binary_num = bin(number)
    if binary_num[-1] == '1' and binary_num[-n-1] == "1":
        return True
    return False

print(is_oth_nth_bit_set(-3 , 1))