import re
#* check if a string exists that has a "a" followed by 2 or 3 "b"

def check_string(str1):
    result = re.findall(r"ab{2,3}",str1)
    print(result)

check_string("abcabb")