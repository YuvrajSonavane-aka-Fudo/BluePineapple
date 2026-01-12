
#! toggle all even bits of a number

def toggle_all_even_bits(num):
    num = abs(num)
    if num==0:
        return 1
    
    if num==1:
        return 0

    for i in range(num.bit_length()):
        if i%2==0:
            mask = 1<<i
            num = num^mask
    return bin(num)

print(toggle_all_even_bits(10))
