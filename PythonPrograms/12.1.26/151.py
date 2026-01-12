
#! find if the numbers are co prime or not

def factor_finder(num):
    if num == 0:
        return 0
    
    if num == 1:
        return 1
    
    num = abs(num)

    res = []
    for i in range(1,num):
        if num%i==0:
            res.append(i)
    return res


def co_prime_finder(num1 , num2):
    lst1 = factor_finder(num1)
    lst2 = factor_finder(num2)

    for i in lst1:
        if i in lst2 and i!=1:
            return False
    return True

print(co_prime_finder(15, -8))