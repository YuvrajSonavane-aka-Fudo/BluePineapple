
#* remove all characters at odd index

def remove_all_characters_at_odd_index(str1):
    '''
     remove all characters at odd index and returns a copy
    '''
    str2 = ""
    for i in range(0,len(str1),2):
        str2 += str1[i]
    return str2
print(remove_all_characters_at_odd_index("hello"))
