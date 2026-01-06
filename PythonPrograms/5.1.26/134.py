
#! check if last number is even or odd after given p operations
#! how those p operations affect last number or what will be the operation is unclear 

def check(lst):
    if lst[-1]%2==0:
        return "even"
    else:
        return "odd"
    
print(check([1,2,3,4]))