from collections import defaultdict
#product of non repeated elements:
def productNonRepeated(list1):
    if list1 == []:
        return 0
    
    dict1 = defaultdict(int)
    prod = 1
    for i in list1 :
        dict1[i] += 1
    
    for k , v in dict1.items():
        if v == 1:
            prod *= k

    return prod

print(productNonRepeated([1,2,3,3]))

# nonrepeatedele = [i for i in list1 if list1.count(i) == 1]
# prod = math.prod(nonrepeatableele)