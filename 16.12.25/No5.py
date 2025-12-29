def dominoes(n):
    n = abs(n)
    if n%2 != 0:
        return 0
    a0 = 1
    a2 = 3 

    if n == 0:
        return a0
    if n == 2:
        return a2

    for i in range(4 , n+1 , 2):
        acur = 4*a2 - a0
        a0 , a2 = a2 , acur

    print(acur)

dominoes(8)