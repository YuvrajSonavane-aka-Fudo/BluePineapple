
#* find the largest sum of contiguous array which is formed by modifying the given array repeated k times

def find_largest_sum(lst , k):
    modifiedarr = []
    for i in range(k):
        modifiedarr.extend(lst)
    return(sum(modifiedarr))

print(find_largest_sum([1,2,3],2))
