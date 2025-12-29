#a given number is a difference of two numbers or not

def check(a):
    if a%2==1 or a%4==0:
        return True
    elif a%4==2:
        return False

print(check(23))