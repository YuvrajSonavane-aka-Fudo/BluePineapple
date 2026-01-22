
#*find minimum of three numbers

def min_of_three_numbers(num1 , num2 , num3):
    '''Returns minimum of three numbers '''
    if num1 < num2 and num1<num3:
        return num1
    if num2 < num3:
        return num2
    return num3

print(min_of_three_numbers(4,-16,3))