
#* subtract two lists using lambda function 

def subtracter(lst1 , lst2):
    '''
        input : accepts two lists 
        output: returns a list of difference of the corresponding elements
    '''

    result = list(map(lambda x , y : (x-y) , lst1 , lst2))
    return result

print(subtracter([1,2,3] ,[5,6,7]))