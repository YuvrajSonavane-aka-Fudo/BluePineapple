
#* check if all items in a list are equal to a given string

def string_checker(lst , str1):
    for i in lst:
        if i!=str1:
            return False
    return True

print(string_checker(["a",1] , "a"))