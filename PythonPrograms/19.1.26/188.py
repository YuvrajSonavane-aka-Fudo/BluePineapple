
#* check if a number can be represented as sum of two squares

def sum_of_squares(num):
    '''Accepts a number . Returns a list of two square numbers if num can be represented as sum of two squares else returns False'''
    if num < 0:
        return False
    for i in range(1000):
        for j in range(1000):
            if ((i**2) + (j**2)) == num:
                return [i,j]
    return False

print(sum_of_squares(13))
