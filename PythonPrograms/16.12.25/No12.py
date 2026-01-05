matrix = [[1,2,3] , [0,0,0] , [4,5,6]]
sumArray = []


def swapRows(matrix , sumArray):
    if matrix == []:
        return 0

    
    i , k = 0,0
    sumArray = calculateSums(matrix , sumArray)
    for i in range(len(sumArray)-1):
        if sumArray[i] > sumArray[i+1]:
            sumArray[i] , sumArray[i+1] = sumArray[i+1] , sumArray[i]
            for k in range(len(matrix[0])):
                matrix[i][k] , matrix[i+1][k] = matrix[i+1][k] , matrix[i][k] 
    print(matrix)

def calculateSums(matrix , sumArray):
    sum1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum1+= matrix[i][j]
        sumArray.append(sum1)
        sum1 = 0
    print(sumArray)
    
    return sumArray
    

swapRows(matrix , sumArray)