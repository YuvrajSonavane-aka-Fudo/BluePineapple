from collections import defaultdict
def isValid(i , j, n):
    if 0<i and i<=n and 0<j and j<=n:
        return True
    else:
        return False
    

def calculatePath(i , j , n , curcost , m , k , costmat):
    costdict = defaultdict()
    while(i!=m and j!=k):
        if isValid(i+1 , j , n):
            curcost += costmat[i+1][j]
            costdict[curcost] = [i+1 , j]
        if isValid(i , j+1,n):
            curcost += costmat[i][j+1]
            costdict[curcost] = [i , j+1]
        if isValid(i+1 , j+1,n):
            curcost += costmat[i+1][j+1]
            costdict[curcost] = [i+1 , j+1]
        if isValid(i-1 , j , n):
            curcost += costmat[i-1][j]
            costdict[curcost] = [i-1 , j]
        if isValid(i , j-1 , n):
            curcost += costmat[i][j-1]
            costdict[curcost] = [i , j-1]
        if isValid(i-1 , j-1 , n):
            curcost += costmat[i-1][j-1]
            costdict[curcost] = [i-1 , j-1]

        mincost = min(costdict.keys())
        i = costdict[mincost][0]
        j = costdict[mincost][1] 

        print(i,j)

costmat = [[0,1,2] , [3,4,5], [6,7,8]]
m , k = 2,2
i,j = 0,0
curcost = 0

calculatePath(i , j , len(costmat),curcost , m , k , costmat)




