
#* replace blanks with any character in a string

def replace_blanks_with_char(str1):
    ''' replaces all spaces with "a" and returns a copy of the string'''
    str2 = ""
    for i in range(len(str1)):
        if str1[i] == " ":
            str2 += "a"
            continue
        str2 += str1[i]
    return str2

print(replace_blanks_with_char("hello i am under the water"))        