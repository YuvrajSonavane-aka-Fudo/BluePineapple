
#TODO magic square
#!moving down means row[i++] 
#!moving up means row[i--] 
#!moving right means row[i][j++]
#!moving left means row[i][j--] 



def create(n):
    if n<0 or n%2==0:
        return None
    
    grid = [[0 for i in range(n)] for i in range(n)] 
    num = 1
    i = 0 
    j = n//2

    while num<=n*n:
        grid[i][j] = num
        num+=1

        newI = (i-1)%n
        newJ = (j+1)%n

        if grid[newI][newJ] != 0:
            i = (i+1)%n
        else:
            i , j = newI, newJ
    
    return grid

    
        


    


print(create(5))