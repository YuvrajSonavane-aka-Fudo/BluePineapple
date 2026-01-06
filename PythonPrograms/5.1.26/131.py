
#!function to only reverse vowels of given string

def reverseVowels(str1):
    if str1 == "" or not (isinstance(str1 , str)):
        return -1
    list1 = list(str1.lower().replace(" " , ""))


    i = 0
    j = len(list1)-1

    vowels = ["a","e","i","o","u"]

    while i < j :
        if list1[i] not in vowels:
            i+= 1
            continue
        if list1[j] not in vowels:
            j-=1
            continue
        
        list1[i],list1[j] = list1[j],list1[i]

        i+=1
        j-=1
    return "".join(list1)


print(reverseVowels("Hello i am "))


