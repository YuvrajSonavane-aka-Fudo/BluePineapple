def nonPrime(n):
    if n==0 :
        return "Neither Prime Nor Composite"
    n = abs(n)
    for i in range(2,n):
        if n%i== 0:
            return "Not Prime"
    return "Prime"

print(nonPrime(-5))




