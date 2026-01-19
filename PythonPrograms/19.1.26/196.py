
#* remove all tuples with k length

def remove_tuples_of_specified_length(lst ,k):
    ''' Accepts a list of tuples and value k . Removes all those that have lenght k'''
    for i in range(len(lst)):
        if len(lst[i])==k:
            lst.pop(i)
    return lst

print(remove_tuples_of_specified_length([(1,2,3) , (3,2)] , 2))