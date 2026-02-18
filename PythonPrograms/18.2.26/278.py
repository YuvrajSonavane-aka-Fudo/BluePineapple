
#* find the element count that occurs before the given record in a tuple

def element_counter(tup1 , record):
    '''
        input : accepts a tuple and record 
        output : returns the count of the elements present before that record
    '''

    if record not in tup1:
        return "Record not in tuple"

    else:
        count1 = 0
        for i in tup1:
            if i==record:
                break
            else:
                count1+=1
        return count1

print(element_counter((1,2,3,4) , 4))
