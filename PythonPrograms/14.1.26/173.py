

#*remove all characters that are NOT alphanumeric

def remove_all_except_alphanum(str1):
    '''accepts a string , removes all characters excepts alphanumeric and returns a duplicate string'''
    str2 = ""
    for i in str1:
        if i.isalnum():
            str2 += i
    return str2

print(remove_all_except_alphanum("!hello i am under the water &"))