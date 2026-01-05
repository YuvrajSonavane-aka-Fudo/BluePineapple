#missing number in sorted array

list1 = [1,2,3,4,5,6,7,9]

def find(list1):
    sum1 = 0
    for i in range(list1[0],list1[-1]+1):
        sum1+=i
    return sum1-sum(list1)

print(find(list1))