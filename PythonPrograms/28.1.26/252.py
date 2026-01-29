import cmath
#*convert complex to polar 

def complex_to_polar(complex_number):
    return cmath.polar(complex_number)


print(complex_to_polar(3+2j))