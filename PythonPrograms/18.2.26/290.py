
#* find list with max length in a list of lists

def max_len_list(lst):
    result = max(lst , key = len)
    return result

print(max_len_list([[1,2,3] , [4,5,6,7,7]]))