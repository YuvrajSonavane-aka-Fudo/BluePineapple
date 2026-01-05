#factorial last digit
import math

def findLastDigit(a,b):
    ans = math.factorial(b) //math.factorial(a)
    lastdigit = ans%10

    return lastdigit

print(findLastDigit(1,2))