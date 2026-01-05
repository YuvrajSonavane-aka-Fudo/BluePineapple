#angle of a complex number
import math

#accepting string as input
def findAng(str1):
    try:
        comp1 = complex(str1)
        realNo = comp1.real
        imagNo = comp1.imag

        return math.degrees(math.atan2(imagNo , realNo))
    except:
        return "Invalid Input . Make sure there are no spaces between + sign and use j instead of i"
    

print(findAng("1+2j"))


