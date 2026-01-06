
#! pancake sort

def pancakeSort(lst):
    k = len(lst) - 1
    while k > 0:
        maxIndex = lst.index(max(lst[:k+1]))
        
        if maxIndex != k:

            lst[:maxIndex+1] = reversed(lst[:maxIndex+1])
            

            lst[:k+1] = reversed(lst[:k+1])
            
        k -= 1
    print(lst)

pancakeSort([1, 4, 3 ,2]) 




