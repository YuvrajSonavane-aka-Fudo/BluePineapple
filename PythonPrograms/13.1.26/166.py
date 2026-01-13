
#! count number of pairs with xor as even number

lst = [[1,2] , [2,3]]

def count_even_exor_pairs(lst):
    count = 0
    for i in lst:
        if (i[0] ^ i[1]) %2 == 0:
            count += 1

    return count

print(count_even_exor_pairs(lst))