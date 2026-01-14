import collections
#* convert a sequence of key value pairs into a dictionary

lst = [[1,2] , [2,"abc"]]

def convert_to_dictionary(lst):
    '''Accepts a list of key value pairs and returns a dictionary'''
    dict1 = collections.defaultdict(int)

    for i in lst:
        dict1[i[0]] = i[1]
    
    return(dict1)

convert_to_dictionary(lst)
    
    