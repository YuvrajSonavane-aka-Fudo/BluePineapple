
#* replace last element of list with another list
list1 = [1,2,3]
list2 = [4,5,6]
def replace_last_with_another_list(list1 , list2):
    '''Accepts two lists . the second list replaces the last element in the first list. Return the modified list'''
    list1[-1] = list2
    return list1

print(replace_last_with_another_list(list1 , list2))