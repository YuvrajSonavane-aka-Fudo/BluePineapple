def findMax(list1 , k):
    if list1 == []:
        return 0
    if k <=0 :
        return 0
    
    ultList = []
    for i in range(len(list1)):
        checkVal = list1[i]
        tempList = []
        tempList.append(list1[i])
        for j in range(i+1 , len(list1)):
            if list1[i] + k == list1[j]:
                tempList.append(list1[j])
                i=j
        ultList.append(tempList)

    return len(max(ultList , key = len))

print(findMax([1,2,4,53,3,4,2],1))