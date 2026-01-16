
#*longest common prefix in a set of strings
lst = ["cat" , "car" , "an"]
def find_longest_common_prefix(lst):
    '''Accepts a list of strings . Returns longest common prefix. If no common prefix found returns empty List'''
    prefix = ""
    k = 0
    while k < len(lst[0]):
        if lst[0][k] == lst[1][k]:
            prefix+= lst[0][k]
        else:
            break
        k+=1
    for i in lst:
        if prefix in i:
            continue
        else:
            return []
    return prefix

print(find_longest_common_prefix(lst))