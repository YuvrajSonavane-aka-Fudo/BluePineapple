
#* highest power of 2 less than or equal to n

def calculate_highest_power_of_2(n):
    '''Accepts n . Calculates highest power of two less than or equal to n'''
    temp = 0
    i = 1
    while temp < n:
        if 2**i > n:
            break
        temp = 2**i
        i+=1
    return temp

print(calculate_highest_power_of_2(65))