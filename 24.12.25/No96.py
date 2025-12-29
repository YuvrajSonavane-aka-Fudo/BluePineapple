#count of all factors of n

def find(n):
    cnt = 0
    for i in range(2,n):
        if n%i == 0:
            cnt +=1
    return cnt

print(find(4))