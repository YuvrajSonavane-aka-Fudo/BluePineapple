#decimal to binar

def decimalToBinary(n):
    n = abs(n)
    if n==0:
        return 0
    if n==1 :
        return 1
    quo = n
    remainderArr = []

    while quo != 0:
        remainderArr.append(quo%2)
        quo = quo//2

    return list(reversed(remainderArr))

print(decimalToBinary(13))

    