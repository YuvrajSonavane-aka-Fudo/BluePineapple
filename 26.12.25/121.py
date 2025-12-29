#triplet sum
lst = [1,2,-3,4]
k = 8

def tripletSum(lst , k):
    first_ele = 0
    second_ele = 0
    third_ele = 0
    lst2 = []
    for i in range(len(lst)):
        sum1 = 0
        for j in range(i+1 , len(lst)):
            sum1 = lst[i] + lst[j]
            if k-sum1 in lst:
                third_ele = k-sum1
                first_ele = lst[i]
                second_ele = lst[j]
                lst2.append(first_ele)
                lst2.append(second_ele)
                lst2.append(third_ele)
                return lst2
                
    return None
print(tripletSum(lst , k)) 


