#split the string using regex at multiple places
import re

def spliter(str1):
    if str1 == "":
        return 0
    
    a = re.split(r"[,;\s]+" , str1)
    print(a)

spliter("Hello , i am under;; the: water")