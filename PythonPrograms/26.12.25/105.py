#count True Booleans

def counter(list1):
    if list1 == []:
        return None
    

    cnt = len(list(filter(lambda x : x==True , list1)))
    print(cnt)

counter(["abc",1 , True , 2])
    