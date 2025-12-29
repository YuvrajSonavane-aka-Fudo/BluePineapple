#first and last char are equal or not 

def check(str1):
    if str1 == "":
        return 0
    if not isinstance(str1 ,(str)):
        return False

    if str1[0] == str1[-1]:
        return True
    else:
        return False
    
print(check(0))