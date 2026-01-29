
#* longest palindrome subsequence in given string

def is_palindrome(str1):
    if list(reversed(str1)) == list(str1):
        return True
    return False

def find_longest_palindrome(str1):
    '''
        Accepts a string and returns the longest palindrome it found. 
        Returns none if no palindrome found 
    '''
    result = []
    for i in range(len(str1)):
        for j in range(i+1 , len(str1)):
            if is_palindrome(str1[i:j+1]):
                result.append(str1[i:j+1])
    print(max(result))

find_longest_palindrome("cabad")