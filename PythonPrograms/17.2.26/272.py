
#* extract last element of every tuple from a list of tuples

def extract_last_element(lst):
    result = []
    for i in lst:
        result.append(i[-1])
    return result

print(extract_last_element([(1,2,3) , (4,5,6)]))