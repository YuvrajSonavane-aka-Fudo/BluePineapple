
#* rearrange elements so that negative numbers appear before positive numbers

def rearrange_lst(lst):
    '''
    returns a list where negative numbers appear before positive numbers
    '''
    return sorted(lst)

print(rearrange_lst([8,-2,5,6,-9]))