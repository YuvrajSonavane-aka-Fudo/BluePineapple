
#*count integral coordinates inside a square

def count_of_integral_coordinates_inside_a_square(coordinates1 , coordinates2):
    return (coordinates2[0] - coordinates1[0] -1) * (coordinates2[1] - coordinates1[1] -1)

print(count_of_integral_coordinates_inside_a_square([1,1] , [5,5]))
