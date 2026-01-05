#function to find element that appears only once in the given array
import collections
lst = [1,1,2 ,2,3,3,9]

def find(lst):
    try:
        dict1 = collections.Counter(lst)
        for i ,j in dict1.items():
            if j == 1:
                  return i
    except:
         return "Invalid Input"
    
print(find(lst))