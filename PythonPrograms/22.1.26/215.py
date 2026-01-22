
#*decode a runlength encoded list

lst = [4,'a',2,'b']
def decode_runlengthencoded_list(lst):
    '''Accepts a run length encoded list . Returns the decoded value as a string'''
    try :
        result = []
        for i in range(0,len(lst) , 2):
            temp = []
            for j in range(lst[i]):
                temp.append(lst[i+1])
            result.extend(temp)
        return "".join(result)
    except:
        print("Unexpected Exception . Perhaps the list you gave is incorrect")

print(decode_runlengthencoded_list(lst))