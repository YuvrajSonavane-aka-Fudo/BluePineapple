#next smallest palindrome of a specified number
def isPalindrome(n):

    if list(str(n)) == list(reversed(list(str(n)))):
        return True
    else:
        return False

def find(n):
    while n-1 > 0:
        if isPalindrome(n-1):
            return n-1
        n -=1
    return None

print(find(10)) 


