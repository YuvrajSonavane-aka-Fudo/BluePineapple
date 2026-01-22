
#* function to replace max n occurances of spaces , commas or dots by colon

def replace_max_n_occurances(string1 , n):
    ''' 
        accepts a string and replaces spaces , commas or dots with colon . upto n occurances 
    '''
    count = n
    string2 = ""
    for i in range(len(string1)):
        if string1[i] == " " or string1[i] == "," or string1[i] == ".":
            string2 += ":"
            count-=1
        else:
            string2+=string1[i]
        if count==0:
            return string2 + string1[i:]
    return string2

print(replace_max_n_occurances("hello i am under the water . please help me ,",5))
    