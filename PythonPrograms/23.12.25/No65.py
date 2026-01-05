#recursion list sum

list1 = [1,2,3]

def recSum(list1 , i , s ):
    if i==len(list1):
        return s
    else:
        return recSum(list1,i+1 , s+list1[i])

print(recSum(list1,0,0))