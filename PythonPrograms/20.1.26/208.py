import re
#*exactly two decimal places using regex

def has_exactly_two_decimal_places(int1):
    str1 = str(int1)
    result = re.search("^\\d*\\.\\d{2}$" , str1)
    if result:
        return True
    return False

print(has_exactly_two_decimal_places(2.1))


