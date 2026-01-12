
#!vertex of parabola

def vertex_of_parabola(a,b,c):
    if a == 0:
        return -1
    
    h = -b/(2*a)

    k = a*(h**2) + b*(h) + c

    return (h,k)

print(vertex_of_parabola(2,3,4))

