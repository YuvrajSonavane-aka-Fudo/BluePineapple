#opposite sign numbers or not

def oppo(num1,num2):
    if num1<0 and num2>=0:
        return True
    if num2<0 and num1>=0:
        return True
    
    return False

print(oppo(-11,-12))