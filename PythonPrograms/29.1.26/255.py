
#* combinations of colors

def combinations_of_colors(number):
    '''
    Docstring for combinations_of_colors
    
    :param number: Number to define how many colors to choose for returning a list of combinations
    '''
    list1 = ['Red' ,'Green' ,'Blue' ]
    result = []
    if number <= 0:
        return []
    
    if number == 1:
        return list1
    
    if number == 2:
        for i in range(len(list1)):
            for j in range(len(list1)):
                result.append([list1[i] , list1[j]])
        return result


    
