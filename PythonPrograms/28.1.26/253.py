
#* count integers in a given list

def count_integers(list1):
    '''Counts number of integers in a list and returns count'''
    count = 0
    for i in list1:
        if isinstance(i , int):
            count+=1
    return count

print(count_integers([1,2,3,[1,2,3]]))