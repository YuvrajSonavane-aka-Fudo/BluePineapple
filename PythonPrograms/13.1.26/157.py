import collections
#!run length encoding

lst = ['a','a' ,'b','b','a','a']

def run_length_encoding(lst):
   
    tempChar = None
    count = 0
    output = []
    for i in lst:
        if i == tempChar:
            count+=1
        else:
            if tempChar is not None:
                output.append(count)
                output.append(tempChar)
                # pass
            
            tempChar = i
            count = 1
    output.append(count)
    output.append(tempChar)
    return output




print(run_length_encoding(lst))




