#geometric series

def geoSeries(a,r,n):
    if a == 0:
        return 0
    
    if r==0:
        return 0

    if n==0 or n<1:
        return 0 
    
    nthterm = (a)*(r**(n-1))
    return nthterm

n = int(input("Enter the n"))
a = int(input("Enter the first term"))
r = int(input("Enter the const factor"))
print(geoSeries(a,r,n))
