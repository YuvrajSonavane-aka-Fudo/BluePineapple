
#*find first missing positive number

lst = [2,3,5]

def find_first_missing_number(lst):
    '''Accepts a list . Returns first missing positive number . Returns none if none found'''
    min_num = min(lst)
    max_num = max(lst)
    for i in range(min_num , max_num):
        if i not in lst:
            return i
    return None

print(find_first_missing_number(lst))