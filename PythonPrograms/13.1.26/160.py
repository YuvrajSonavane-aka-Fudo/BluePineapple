
#! function to find x and y such that ax+by = n

def find_x_y(a , b, n):
    x = a/n
    y = ((n) - (a * x))/b
    return [x,y]

print(find_x_y(1 , 1 , 5))