#equilateral triangle

def equi(a , b , c):
    if a<0 or b<0 or c<0:
        return False
    if a==b==c:
        return True
    else:
        return False
print(equi(4,4,-14))