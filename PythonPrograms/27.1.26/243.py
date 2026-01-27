from collections import Counter
#*sort tuples based on the frequency of the first element
list1 = [("a",100) , ("b" ,200) , ("c",400) , ("c" , 200)]

def sort_by_freq(list1):
    ''' Returns the sorted list based on the freq of the first elements of tuples'''
    counts = Counter(i[0] for i in list1)
    return sorted(list1 , key =  lambda x : counts[x[0]] , reverse=True)

print(sort_by_freq(list1))