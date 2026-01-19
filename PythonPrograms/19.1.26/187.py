
#*longest common subsequence among two strings

def longest_common_subsequence(str1 , str2):
    ''' Accepts two strings . Returns the longest common subsequence among the two'''
    result = []
    short_string = str1 if len(str1)<len(str2)else str2
    long_string = str2 if short_string == str1 else str1
    for i in range(len(short_string)):
        for j in range(len(long_string)):
            if (short_string[i] == long_string[j]):
                pass
        templst = []

       
    return result

print(longest_common_subsequence("ab","cabc"))
    
            

            