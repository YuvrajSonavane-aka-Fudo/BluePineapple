#[1,2,6] ,[1,2,3,4,5,6]

def extract(list1,start , end):

    list2 = [i for i in range(start , end+1)]
    print(list2 , "This list without missing values")
    missing = []
    for i in list2:
        if i not in list1:
            missing.append(i)

    return missing

print(extract([1,2,3,6] , 0 , 6))


