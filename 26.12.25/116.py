#convert given tuple of ints to an int

def convert(tup1):
    try:
        list1 = []
        for i in tup1:
            list1.append(str(i))
        str1 = "".join(list1)
        return int(str1)
    except:
        return "Invalid Input"

print(convert((1,2,3)))