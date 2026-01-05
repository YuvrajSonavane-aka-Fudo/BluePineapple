#nth smart number 
# a smart no is a number with atleast three distinct prime factors

def isPrime(n):
    for i in range(2 ,n):
        if n%i==0:
            return False
    return True


def calSmart(n):
    numlst = []
    for i in range(2 , 1000):
        Factorlst = []
        
        for j in range(2 ,10000):
            if i%j==0 and isPrime(j):
                Factorlst.append(j)
            if len(Factorlst) == 3:
                numlst.append(i)
                break
    return numlst[n]
    

print(calSmart(0))

    
    


