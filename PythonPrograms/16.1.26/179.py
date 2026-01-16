
#* identify if a number is a keith number or not

def isKeith(number):
    '''Returns True if the number passed is keith , else returns false'''
    list1 = list(str(number))
    list2 = []
    for i in list1:
        list2.append(int(i))

    if len(list2) < 3:
        return False
    
    for i in range(1000):
        list2.append(sum(list2[i:i+3]))
        #print(list2)
        if list2[-1] == number:
            return True
    return False
        
    

    


print(isKeith(197))