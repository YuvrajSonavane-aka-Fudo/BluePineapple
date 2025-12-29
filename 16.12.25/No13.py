from collections import defaultdict
list1 = ["apple" , "ball" , "cat", "cat" , "cat" , "apple"]

def commonWords(list1):
    commonwords = []
    dict1 = {}
    for i in list1:
        dict1[i] = 0

    for i in list1:
        dict1[i] += 1

    for k , v in dict1.items():
        if v > 1 :
            commonwords.append(k)
    return commonwords

print(commonWords(list1))

            



