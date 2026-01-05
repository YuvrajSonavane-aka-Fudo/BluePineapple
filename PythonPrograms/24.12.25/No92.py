#undulating number are of the form "abababa"

def check(num:int):
    num = str(abs(num))
    
    for i in range(2,len(num)):
        if num[i-2]!=num[i]:
            return False
            
    return True

print(check(121))
