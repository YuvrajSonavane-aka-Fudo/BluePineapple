string1 = "_abc a_Der der_ kdfj "

def underScore(str1):
    list1 = []
    str1 = list(str1.split(" "))
    for i in str1:
        if "_" in i and i.islower():
            list1.append(i)
    print(list1)

underScore(string1)