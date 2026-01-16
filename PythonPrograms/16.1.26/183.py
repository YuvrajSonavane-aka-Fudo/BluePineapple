
#* all distinct pairs having difference k in the given array

lst = [1,2,3]
k = 1

def distinct_pairs_having_differenc_k(lst , k):
    '''Accepts a list and a value k . Returns a list of pairs having difference k'''
    result = []
    for i in range(len(lst)):
        for j in range(i+1 ,len(lst)):
            if abs(lst[i] - lst[j])==k:
                result.append((lst[i],lst[j]))
    return result

print(distinct_pairs_having_differenc_k(lst,k))