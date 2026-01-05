#given numer is one less than twice its reverse

def check(num):
    
    if num == 0:
        return 0
    
    num = abs(num)

    ognum = num
    a = str(num)
    a = list(reversed(a))
    a = "".join(a)
    a = int(a)

    if ognum == a-1:
        return True
    else:
        return False


check(2223)