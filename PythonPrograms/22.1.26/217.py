
#* find first repeated character in a given string

def first_repeated_character(string1):
    '''Accepts a string . Returns the first repeated character . if none found returns -1'''
    set1 = set()
    for i in string1:
        if i in set1:
            return i
        if i not in set1:
            set1.add(i)
        
    return -1

print(first_repeated_character('ab'))
