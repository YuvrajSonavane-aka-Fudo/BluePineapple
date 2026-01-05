#nth octagonal number

def find(n):
    if n <= 0:
        return 0
    
    return (3*(n**2)) - 2*(n)

print(find(2))