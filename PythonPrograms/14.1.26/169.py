import math

#*calculate the nth pell number

def calculate_pell_number(n):
    '''Calculates the pell number using binets formula and returns the nth pell number . accepts n as the argument'''

    result = ((1+math.sqrt(2))^n - (1-math.sqrt(2))^n)/ (2 * math.sqrt(2))
    return result
