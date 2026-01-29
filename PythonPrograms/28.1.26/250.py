
#*count the occurances of of element in tuple

def count_occurance(element , tuple1):
    '''Returns the count of the given element in the tuple'''
    count = 0
    for i in tuple1:
        if i == element:
            count+=1
    return count

print(count_occurance(2, (1,2,3,4,2,4,2)))