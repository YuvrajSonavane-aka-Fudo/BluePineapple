#diff between sum of even and odd digits
list1 = [1,2,3]

def diffFinder(list1):
    evens  = sum(list(filter(lambda x : x%2 == 0 , list1)))
    odds = sum(list(filter(lambda x : x%2!=0 , list1)))

    return evens-odds

print(diffFinder(list1))
