
#* function to set all even bits of a number

def set_even_bits(number):
    '''Returns the number with all even bits set'''
    binary_number = list(bin(number))
    
    for i in range(2 , len(binary_number)):
        if i % 2 == 0 and binary_number[i] == "0":
            binary_number[i] = "1"
    return binary_number


print(set_even_bits(9))

