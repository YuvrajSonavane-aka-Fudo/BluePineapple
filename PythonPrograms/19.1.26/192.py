import re
#*check whether given string contains atleast one letter and one number

def contains_letter_number(str1):
    '''Accepts a string . Returns True if it contains at least one letter and one number else returns false'''
    str1 = str1.lower()
    str_lst = re.findall("[a-z]+" , str1)
    num_lst = re.findall("[0-9]+",str1)
    if str_lst==[] or num_lst==[]:
        return False
    return True

print(contains_letter_number("abc"))