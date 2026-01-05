list1 = [1,-2,3]
def countPositive(list1):
    count = 0
    for i in list1:

        if i>0:
            count +=1
    return count

print(countPositive(list1))