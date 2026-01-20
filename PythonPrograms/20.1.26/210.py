import re
#* check if string has a-z A-Z and 0-9 using regex

def string_checker(str1):
    '''accepts a string . Return true if it contains alpha numeric charcters else False'''
    result = re.search("[a-z]+[A-Z]+[0-9]+",str1)
    if(result):
        return True
    return False

print(string_checker("abcA"))