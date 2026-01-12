
#! find the longest subsequence such that adjacent elements difference is one

lst = [1,2,4,5,6,7]

def find_longest_subsequence_difference_one(lst):
    res = []

    for i in range(len(lst)):
        tempLst = []
        tempLst.append(lst[i])
        j = i+1
        while j <len(lst):
           
            if lst[j] - lst[i] == 1:
                tempLst.append(lst[j])
                i+=1
            j+=1
           
        res.append(tempLst)

    return max(res, key = len)

print(find_longest_subsequence_difference_one(lst))

