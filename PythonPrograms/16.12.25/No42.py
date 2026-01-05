list1= [1,2,3,4,2,1,3,4]

def sumofrepeatedelements(list1):
    sum1=0
    set1 = set()
    for i in list1:
        if i in set1:
            sum1+=i
        else:
            set1.add(i)
    print(sum1)

sumofrepeatedelements(list1)