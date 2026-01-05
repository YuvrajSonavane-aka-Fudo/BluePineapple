#check if all dictionaries are empty or not 
lst = []

def check(lst):
    try:
        for i in lst:
            if isinstance(i , dict):
                if i!={}:
                    return False
        return True
    except:
        return None

print(check(lst))