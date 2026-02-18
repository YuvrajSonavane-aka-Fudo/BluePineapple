import collections
#* check if freq of each element is less than or equal to the element

def freq_checker(lst):
    if (lst == []):
        return "Empty List"

    dict1 = collections.defaultdict(int)
    
    for i in lst:
        dict1[i] += 1
    
    print(dict1)

    for k , v in dict1.items():
        if v>k:
            return False
    return True

print(freq_checker([1,2,3,4,6,6,6,6,6,6,6,6,6,6,6,6,6]))