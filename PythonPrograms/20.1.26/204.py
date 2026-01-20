
#*count the occurance of a given character in a string

def count_occurance(str , character)->int:
    '''Accepts a string and , character whose count is to be found . Return count of that character'''
    count = 0
    for i in str:
        if i == character:
            count += 1
    return count

print(count_occurance("abc","a"))