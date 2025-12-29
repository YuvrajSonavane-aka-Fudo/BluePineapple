#newman conway sequence
#\(P(n)=P(P(n-1))+P(n-P(n-1))\)
import functools

@functools.lru_cache(100)
def newP(n):
    if n==1:
        return 1
    if n==2:
        return 1
    
    return(newP(newP(n-1))+newP(n-newP(n-1)))

print(newP(30))