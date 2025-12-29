#min list using lambda

list1 = [[1,2,3],[1,2,4] , [2,3]]

def minList(list1):
    minlist1 = min(list1 , key = lambda x : len(x))
    print(minlist1)

minList(list1) 
