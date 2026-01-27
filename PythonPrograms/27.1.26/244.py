
#* next perfect square greater than the given the number

def next_perfect_square(number):
    '''Accept a number . Returns the next perfect square greater than the number'''
    if number == 0:
        return 1
    
    if number == 1 or number == 2:
        return 4
    
    for i in range(1 ,number):
        if i**2 > number:
            return i**2

print(next_perfect_square(1))