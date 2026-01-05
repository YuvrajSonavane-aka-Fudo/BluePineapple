def firstDiv(list1):
    if list1 == []:
        return 0
    
    firstEven = 2
    firstOdd = 1
    for i in list1:
        if i%2==0 and i!=0:
            firstEven = i
            break
    for i in list1:
        if i%2!=0 and i!=0:
            firstOdd = i
            break

    print(firstEven,firstOdd)

    return firstEven/firstOdd

print(firstDiv([4,4,5]))