
#* count number of non empty substring that can be formed from a string

def count_of_non_empty_substring(string1):
    ''' Returns the count of non empty substring that can be formed'''
    string2 = string1.replace(" " , "")
    print(string2)
    n = len(string2)
    return (n*(n+1))//2 

print(count_of_non_empty_substring("I am under the water"))