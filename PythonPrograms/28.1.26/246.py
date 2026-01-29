import math
#*compute square root using babylonian method

def babylonian_square_root(number , tolerance):
    '''Computes square root using babylonian method'''
    prev_guess = 0
    current_guess = number/2 or 1

    while abs(current_guess-prev_guess)>tolerance:
        prev_guess = current_guess
        current_guess = (prev_guess + number/prev_guess)/2
    return round(current_guess,3)


print(babylonian_square_root(20,0.001))