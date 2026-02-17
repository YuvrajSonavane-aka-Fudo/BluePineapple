
#* filter a dictionary based on values

def filter_based_on_value(dict1 , value):
    '''
        input : accepts a dict and value
        output : returns a dictionary with the filtered elements
    '''

    result = dict(filter(lambda item  : item[1] == value , dict1.items()))
    print(result)

filter_based_on_value({1:"a" , 2:"b"} ,1 )