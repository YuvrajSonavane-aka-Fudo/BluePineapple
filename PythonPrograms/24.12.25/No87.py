#merger three dicts into one

def merger(dict1,dict2,dict3):
    return dict1|dict2|dict3

dict1 = {1:"a"}
dict2 = {1:"b"}
dict3 = {3:"c"}
print(merger(dict1,dict2,dict3))
