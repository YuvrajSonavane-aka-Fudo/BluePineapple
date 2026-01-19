
#* Octal to decimal

def octal_to_decimal(number):
    '''Accepts an octal number . returns decimal equivalent'''
    result = 0
    i = 0
    while number > 0 :
        temp = number%10
        result+= (temp)*(8**i)
        number = number//10
        i+=1
    return result

print(octal_to_decimal(54)) 