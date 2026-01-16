import re
#*stringliterals in a string using regex

def find_string_using_regex(string1 , string2):
    '''accepts two strings . One which is to be searched and the other is the string to be found. Returns a match object'''
    lst = re.search(f"{string2}",string1)
    return lst

print(find_string_using_regex("abc" , "abc"))
