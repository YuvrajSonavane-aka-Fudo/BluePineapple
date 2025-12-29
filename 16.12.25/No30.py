def substring1(str1):
    count = 0
    list1 = list(str1.split(" "))
    for i in list1:
        if i[0] == i[-1]:
            count+=1
    print(count)
substring1("aba bbc agc adda")