
def pathSum(lst):
    templst = []
    for i in lst:
        templst.append(max(i))

    print(f"path = {templst}")

    return sum(templst)

print(pathSum([[1,0,0] , [0,2,7] , [5,4,5] , [8,4,4,2]]))
