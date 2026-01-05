#convert snake case to camel case string

def convert(str1):
    if str1 == "":
        return None
    
    if "_" not in str1:
        return None

    str2 = str1.split("_")
    str3 = [str2[0]]
    #print(str2)
    
    for i in range(1 , len(str2)):
        str3.append(str2[i].capitalize())
    
    return "".join(str3)

print(convert("hello_world_lol"))