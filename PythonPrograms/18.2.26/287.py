
#* find sum of squares of the first n even natural numbers

def sum_of_squares(n):
    result = 0
    for i in range(1 , n+1):
        result += i**2
    return result

