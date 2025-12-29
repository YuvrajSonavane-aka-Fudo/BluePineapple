def nsmallestItems(list1 , n):
    if n==0:
        return None
    n = abs(n)

    list1 = (sorted(list1))
    for i in range(n):
        print(list1[i])

list1 = [1,2,3,4,45,2,34,23,2,321,1]

nsmallestItems(list1 , -3)