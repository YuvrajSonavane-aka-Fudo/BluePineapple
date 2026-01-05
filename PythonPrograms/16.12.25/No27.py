list1 = [1,2,3,"hello","gg"]

def removeDigits(list1):
    list2 = []
    for i in list1:
        if not isinstance(i , (int , float, complex)):
            list2.append(i)
    print(list2)

removeDigits(list1)
