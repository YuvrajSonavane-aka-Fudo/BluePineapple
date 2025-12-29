#check whether given string represents integer or not

def check(str1):
    try :
        if isinstance(int(str1) ,int):
            return True
    except:
        return False
    
print(check("3333"))