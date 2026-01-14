
#* occurance of 'std' in given string

def find_occurance_of_substring(string1 , substring):
    '''Accepts a string and substring which is to be found . Returns index of the first occurance'''
    index = 0
    length_of_substring = len(substring)
    for i in range(len(string1)):
        if i+length_of_substring > len(string1):
            return "Substring Not found"
        if string1[i:i+length_of_substring] == substring:
            return i
        
        return "Substring not Found"
        

print(find_occurance_of_substring("abcstd" , "f"))

        
            