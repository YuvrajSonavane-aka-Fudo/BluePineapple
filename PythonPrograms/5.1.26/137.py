
#?find ratio of zeroes

def findRatio(lst):
    count1 = 0
    for i in lst:
        print(i)
        if i == 0:
            count1+=1
            print("g")

    return (count1/len(lst))

print(findRatio([1,2,3,4,5,0]))