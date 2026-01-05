#sum of repeated elements

def sumOfRepeatedELements(list1):
    listofrepeated = (list(filter(lambda x : list1.count(x)>1 , list1)))
    print(sum(set(listofrepeated)))

sumOfRepeatedELements([1,1,3,4,2,3,2])