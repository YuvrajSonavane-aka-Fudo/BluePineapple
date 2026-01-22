
#* count set bits in a number

def count_set_bits(number):
    ''' Returns the count of set bits in a number'''
    binary_num = bin(number)
    count = 0
    for i in binary_num:
        if i == "1":
            count+=1
    return count

print(count_set_bits(4))