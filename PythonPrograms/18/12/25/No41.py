#filter even numbers using lambda function

def filterEven(list1):
    list2 = list(filter(lambda x : x%2==0 , list1))
    return list2

print(filterEven([1,2,3,4]))