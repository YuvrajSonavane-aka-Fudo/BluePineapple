
#TODO multiply two numbers without * operator

def multi(a,b):
    if a == 0 or b == 0:
        return 0
    
    ans = 0
    for i in range(b):
        ans += a
    
    return ans

print(multi(2,8))