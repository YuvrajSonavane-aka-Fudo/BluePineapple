#count all rotations first , then find the ones with odd values

def counter(binString):
    list1 = [ binString[i:]+binString[:i] for i in range(len(binString))]
    list2 = list(filter(lambda x : x[-1]=="1" , list1))
    print(len(list2),list2)

counter("1011")
