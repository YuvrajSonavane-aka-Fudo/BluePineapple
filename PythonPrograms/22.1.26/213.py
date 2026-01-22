
#*perform concatenation of string tuples
lst = [("abc") , ('bcd'), ('dfg')]
def concatenation_of_string_tuples(lst):
    '''performs concatenation of string tuples. Accepts a list of tuples . Returns a concatenated lst'''
    try:
        result = []
        for i in lst:
            result.extend(i)
        return "".join(result)
        
    except:
        print("An unexpected exception occured")
    

print(concatenation_of_string_tuples(lst))