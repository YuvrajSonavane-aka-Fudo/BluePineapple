
#*operations required to make two numbers equal
#* i am assuming we are allowed to only increment of decrement by 1

def operations_required_to_make_equal(num1 , num2):
    ''' Returns the number of increments or decrements it would take to make num1 and num2 equal'''
    return abs(num1-num2)

print(operations_required_to_make_equal(8,7))
