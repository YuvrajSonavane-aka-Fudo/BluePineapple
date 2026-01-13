import collections
lst = [1,2,3,3 , 3,2,2,2,2,2]

def element_with_max_freq(lst):
    dict1 = collections.defaultdict(int)
    for i in lst:
        dict1[i] +=1
    maxk = 0
    maxval = 0
    for k,v in (dict1.items()):
        if v > maxval:
            maxk = k
            maxval = v
    return maxk

def find_number_of_operations(lst):
    num = element_with_max_freq(lst)
    count = 0
    for i in lst:
        if i != num:
            count+=1
    return count


print(find_number_of_operations(lst))
