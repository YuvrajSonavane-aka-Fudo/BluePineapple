#sort a list of tuples using lambda

list1 = [(1,2,3) , (7,5,6), (3,4,5)]

def sorter(list1):
    if list1==[]:
        return 0
    
    list2 = sorted(list1 , key = lambda x : x )
    print(list2)

sorter(list1)