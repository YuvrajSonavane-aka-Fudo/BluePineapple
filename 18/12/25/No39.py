from collections import defaultdict

def possibility(str1):
    dict1 = defaultdict(int)
    for i in str1:
        dict1[i] += 1
    
    maxDictValue = max(dict1.values())
    maxDictKey = max(dict1 , key = dict1.get)
    remainingCount = abs(maxDictValue - sum(dict1.values()))
    
    if remainingCount - maxDictValue >= 1:
        return True
    else:
        return False
    
    

print(possibility("aaaaa"))