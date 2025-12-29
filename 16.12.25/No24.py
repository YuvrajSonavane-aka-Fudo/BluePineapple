#binar to decimal
binString = "1101"

def bintodecimal(str1):

    #simple built in functino
    #dec = int(str1 , 2)
    str1 = "".join(reversed(str1))
    sum1 = 0
    for i in range(len(str1)):
        sum1 += int(str1[i]) * 2**i 
    print(sum1)

bintodecimal(binString)