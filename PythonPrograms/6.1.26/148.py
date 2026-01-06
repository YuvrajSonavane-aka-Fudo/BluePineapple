
#!divide a number such that the sum of them is max

def findMaxSum(n):
    strNum = str(n)
    maxSum = 0
    tempsum = 0

    for i in range(1 , len(strNum)):
        first = int(strNum[:i])
        second = int(strNum[i:])

        tempsum = first+second

        if tempsum>maxSum:
            maxSum = tempsum

    return maxSum

print(findMaxSum(4554))





