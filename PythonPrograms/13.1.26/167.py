
#! smallest power of 2 greater than or equal to n

def calculate_smallest_power_of_2(n):
    power_of_two = 2
    while not power_of_two >= n:
        power_of_two *= 2



    return power_of_two

print(calculate_smallest_power_of_2(64))
