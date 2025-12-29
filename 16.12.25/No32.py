#largest prime factor

def isPrime(n):
    for i in range(3,n):
        if n%i==0:
            return False
    return True

def largestPrimeFactor(n):
    largest = 0
    for i in range(2,n):
        if isPrime(i) and n%i==0 and i>largest :
            largest = i
    return largest

print(largestPrimeFactor(4))
