
#* sum of squares of first n odd natural numbers

def summate_squares_of_odd(n):
    sum1 = 0
    for i in range(1,n+1):
        if i%2!=0:
            sum1 += i**2
    return sum1

print(summate_squares_of_odd(5))
