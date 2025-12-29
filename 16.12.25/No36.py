#nth digite of proper fraction

def nthdigit(a,b , n):
    a = abs(a)
    b = abs(b)
    pf = a/b if a < b else b/a
    strpf = str(pf)
    n = n+2
    if n>=len(strpf):
        return 0
    else:
        return strpf[n]
print(nthdigit(1,2,0))