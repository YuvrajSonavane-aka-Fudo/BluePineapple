
#*find all ascii values

def findAsciiVal(str):

    lst = [ord(c) for c in str]
    return lst

print(findAsciiVal("abc hello "))