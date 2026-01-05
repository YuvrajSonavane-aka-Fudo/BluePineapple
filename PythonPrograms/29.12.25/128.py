
#TODO shortlist words that are longer than n in list of words

def shortlist(lst ,n):

    if lst==[]:
        return None
    res = []
    try:
        for i in lst:
            if len(i) > n:
                res.append(i)

        return res
    except:
        return "Please provide list with strings only"

shortlist(["abcd" , "3253423" , 123] , 3)
