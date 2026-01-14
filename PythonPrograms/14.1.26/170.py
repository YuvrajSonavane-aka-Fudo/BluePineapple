
#* sum of numbers within a specified range

def calculate_sum_within_specified_range(lst , start , end):
    ''' Accepts a list and start and end values . Return sum of elements within specified range'''

    if start < 0:
        return "Please enter start range greater than or equal to zero"
    if end > len(lst):
        return "Please enter end range less than length of the list"
    summation = 0
    for i in range(start , end):
        summation += lst[i]
    
    return summation

print(calculate_sum_within_specified_range([1,2,3] , 0 , 4))