def sortMix(list1):
    integers = sorted(list(filter(lambda x : isinstance(x , (int , float , complex)) , list1)))
    chars = sorted(list(filter(lambda x : isinstance(x , (str)) , list1)))
    list2 = []
    list2.extend(integers+chars)
    print(list2)
    

sortMix([1,2,3,"abc", "xyz","hgj", 0])