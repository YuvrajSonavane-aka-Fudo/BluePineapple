list1 = ["1","2"]

def maxNum(list1):
    list1 = sorted(list1 , reverse = True)
    print(int("".join(list1)))
    

maxNum(list1)