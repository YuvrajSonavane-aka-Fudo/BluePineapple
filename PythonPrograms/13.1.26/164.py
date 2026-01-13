
#!calculate if sum of divisors is same or not

def calculate(a,b):

    if a==b:
        return True

    divisors_of_a = []
    divisors_of_b = []

    for i in range(2,a):
        if a%i == 0:
            divisors_of_a.append(i)
    for i in range(2,b):
        if b%i == 0:
            divisors_of_b.append(i)
    
    if sum(divisors_of_a) == sum(divisors_of_b):
        return True
    else:
        return False

print(calculate(8,8))
    