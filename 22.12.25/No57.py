#largest number that can be formed

def largestNum(num):
    if num == 0:
        return 
    num = abs(num)
    
    list1 = list(str(num))
    list1 = sorted(list1 , reverse = True)
    ans = int("".join(list1))
    print(ans)

largestNum(34)