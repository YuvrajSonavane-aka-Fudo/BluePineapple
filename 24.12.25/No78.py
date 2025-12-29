#count all odd set bits of integeres in  a list
import math
def counter(list1):
    binarystringlist = []
    for i in list1:
        binarystringlist.append(str(bin(i)))
    cnt = 0
    for i in range(len(binarystringlist)):
        if binarystringlist[i].count("1")%2!=0:   
            cnt+=1      
    print(cnt)

counter([1,2,3])
