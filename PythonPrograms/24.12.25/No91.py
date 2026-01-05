#substring in list of strings

def check(substr , list1):
    for i in list1:
        if substr in i:
            return True
    return False

print(check("abc",["abcde","gasdf"]))