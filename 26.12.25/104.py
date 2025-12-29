#sort each sublist using lambda 
list1 = [["abc","zcf","hgj"] , ["kg" , "asg" ,"etw"]]
def sorter(list1):
    if list1 == []:
        return None
    
    list2 = [sorted(sublist , key = lambda x : x) for sublist in list1 ]
    print(list2)

sorter(list1)
