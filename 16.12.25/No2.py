def similarElements(tup1 , tup2):
    arr1 = []
    for i in tup1:
        if i in tup2:
            arr1.append(i)
    print(arr1)


similarElements((1,2,3),(2,3))