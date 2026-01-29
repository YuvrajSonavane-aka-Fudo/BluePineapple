
#* split a list into two parts where length of the first list is given

def splitter(length_of_first_part , lst):
    '''
    Splits a list into two parts . based on the length . returns a list containing two nested lists
    '''
    first_part = lst[:length_of_first_part]
    second_part = lst[length_of_first_part :]
    return [first_part , second_part]

print(splitter(3 , [1,2,3,4,5]))        