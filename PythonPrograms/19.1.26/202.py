
#*remove even characters in a string

def remove_even_characters(str1):
    '''accepts a string . Removes characters occuring at even index . Returns a string'''
    str2 = ""
    for i in range(0, len(str1),2):
        str2 += str1[i]

    return str2
        
        

print(remove_even_characters("abc"))
