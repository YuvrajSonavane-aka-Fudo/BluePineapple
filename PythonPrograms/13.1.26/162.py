
#! calculate sum of all positive integers n + (n-2) +.... (n<=0)

def calculate(n):
    accumulator = n
    i = 2
    while n-i >=0 :
        accumulator += n - i
        i = i*2
    return accumulator

print(calculate(0))


    