
#* max number of equilateral triangles that can be formed within a given equilateral triangle

def count_max_equilateral_triangles(n):
    ''' Accepts side of the equilateral triangle . Counts the number of unit equilateral triangles that can be formed'''
    if n % 2 == 0:
        return (n*(n+2)*(2*n +1))//8 
    if n % 2 != 0:
        return ((n*(n+2)*(2*n +1))-1)//8 
    
print(count_max_equilateral_triangles(2))