import math
#*convert radian to degrees

def convert_radian_to_degree(rad_value):
    pi = 22/7
    deg = rad_value*(180/pi)
    
    return round(deg , 2) 

print(convert_radian_to_degree(1))