#len of the longest word and word

str1 = "hello i am under the water"

def find(str1):
    list1 = str1.split(" ")
    return len(max(list1 , key = len)) , max(list1, key = len) 

print(find(str1))