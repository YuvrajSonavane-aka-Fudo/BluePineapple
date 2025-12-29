#check word at beginning of a string

def check(str1 , ip):
    strlist = str1.split(" ")
    if ip == strlist[0]:
        return True
    else:
        return False
print(check("Old Man" , "Man"))
