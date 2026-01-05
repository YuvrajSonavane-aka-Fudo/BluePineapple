str1 = "acbder"
str2 = "acdg"

str1list = list(str1)
for i in range(len(str1)):
    if str1list[i] in str2 :
        str1list[i] = ""
str1 = "".join(str1list)
print(str1)