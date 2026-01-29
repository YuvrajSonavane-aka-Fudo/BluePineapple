
#*swap two numbers

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

a , b = swap(4,5)
print(a,b)