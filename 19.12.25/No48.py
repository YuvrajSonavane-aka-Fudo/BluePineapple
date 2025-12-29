def setAllOddBits(num):
    for i in range(1, num.bit_length() , 2):
        num = num | (1<<i)
    return num

print(setAllOddBits(4))
