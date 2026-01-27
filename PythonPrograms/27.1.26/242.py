
#*count characters in string

def count_characters(string1):
    ''' Accepts a string and returns the count of the total number of characters'''
    if string1 == "":
        return 0
    count = 0
    for i in string1:
        if i == " ":
            continue
        count+=1
    
    return count

print(count_characters("Hello  _"))
    
    
