string1 = "Old Mcdonald Had a farm"

def splitAtLowerCase(str1):
    list1 = []
    for i in str1:
        while(not(i.islower())):
            list1.append(list(i))
            break
            print(list1)
              
        
    print(list1)

splitAtLowerCase(string1)