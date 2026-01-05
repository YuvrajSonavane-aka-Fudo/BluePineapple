num = int(input("Enter the number"))

def checkWooBall(num):
    num = abs(num)
    n = 1
    while True:
        wooballnum = (n * (2**n)) -1
        if wooballnum==num:
            return True
        if wooballnum > num:
            return False
        n+=1
    
print(checkWooBall(num))