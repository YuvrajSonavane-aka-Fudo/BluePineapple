
#!calculate sum of abs difference of every pair

def calculateSumOfAbsDifferences(lst):
    temp = []
    for i in range(len(lst)):
        for j in range(i+1):
            diff = abs(lst[i]-lst[j])
            temp.append(diff)
    return sum(temp)

print(calculateSumOfAbsDifferences([1,2 ,3]))