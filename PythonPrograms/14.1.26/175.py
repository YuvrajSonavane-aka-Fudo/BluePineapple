
#* validity of parenthesis in a string

str1 = "()"

def check_validity_of_parenthesis(string1):
    '''Accepts a string of parenthesis and checks their validity . Returns true or false'''
    stack1 = []
    for i in string1:
        if i == "(" or i=="[" or i == "{":
            stack1.append(i)
        if i == ")":
            temp = stack1.pop()
            if temp=="(":
                continue
            else:
                return False
        if i == "]":
            temp = stack1.pop()
            if temp=="[":
                continue
            else:
                return False
        if i == "}":
            temp = stack1.pop()
            if temp=="{":
                continue
            else:
                return False
    if stack1==[]:
        return True
    return False

print(check_validity_of_parenthesis(str1))