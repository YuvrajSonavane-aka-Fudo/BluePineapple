def gcd(num1 , num2):
    n = max(num1 , num2)
    gcd = 0
    for i in range(1,n+1):
        if num1%i==0 and num2%i==0 and gcd < i:
            gcd = i
    print(gcd)

gcd(40,20)
