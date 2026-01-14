
#*find freq of number in given array

def element_with_max_freq(lst):
    '''Accepts a list and returns the element with max frequency '''
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

element_with_max_freq([1,2,2,3])
