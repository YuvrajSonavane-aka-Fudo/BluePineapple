import math
#*calculate harmonic sum upto n-1

def calculate_harmonic_sum(n):
    y = 0.5772 #euler macroni constant
    harmonic_sum = math.log(n-1)+y
    return harmonic_sum

print(calculate_harmonic_sum(5))
