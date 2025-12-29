list1 = [[1,2,3] ,[2,3,4]]
def findMax(list1):
    for i in list1:
        maxsum = 0
        if maxsum < sum(i):
            maxsum = sum(i)

    print(maxsum)

findMax(list1)

