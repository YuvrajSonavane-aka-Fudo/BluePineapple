#sum of amicable numbers

def calDivisors(n):
    res = []
    for i in range(1,n):
        if n%i==0:
            res.append(i)
    #print(res)
    return res

def calAmicable(n):
    res = []
    for i in range(1,n):
        temp = sum(calDivisors(i))
        if sum(calDivisors(temp)) == i and temp!=i:
            if temp not in res:
                res.extend([i , temp])
    return sum(res)

print(calAmicable(1000))

