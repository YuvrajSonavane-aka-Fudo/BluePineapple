#squares in a rectangle

#m and n is the grid size mxn
#mathematical formula :
    #count of sqaures = m*n + (m-1)(n-1) ......until either term becomes zero

def findSq(m,n):
    if m<0 or n<0:
        return 0
    cnt = 0
    while m>0 and n>0:
        cnt += m*n
        m-=1
        n-=1
    return cnt

print(findSq(4,5))
