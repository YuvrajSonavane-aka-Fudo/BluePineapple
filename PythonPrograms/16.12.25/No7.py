import re
str1 = "Old McDonald Had A Farm"

str2 = re.findall(r"\b\w{4,}\b" , str1)

print(str2)
