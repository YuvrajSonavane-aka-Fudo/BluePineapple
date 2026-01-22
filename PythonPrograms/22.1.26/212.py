
#* function to return sum of the fourth power of n natural numbers

def sum_of_fourthpower_of_n_natural_numbers(n):
    '''Accepts a natural number n . Returns sum of the fourth power of those n natural numbers'''
    if n<0:
        return -1

    result = 0
    for i in range(1,n+1):
        result += i**4
    return result

print(sum_of_fourthpower_of_n_natural_numbers(2))