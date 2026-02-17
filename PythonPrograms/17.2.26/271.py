
#* sum of fifth power of n even natural numbers

def summate_fifth_power_of_even_numbers(n):
    sum1 = 0
    for i in range(0,n+1 , 2):
        sum1 += i**5
    return sum1

print(summate_fifth_power_of_even_numbers(2))