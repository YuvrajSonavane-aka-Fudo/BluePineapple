
#* sequential search

def sequential_search(lst ,element):
    '''Returns index of the element in the list'''
    for i in range(len(lst)):
        if lst[i] == element:
            return i
