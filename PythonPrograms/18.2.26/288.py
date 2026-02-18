
#* return the count of elements that are x*x % p == 1

def modulo_inverse_function(lst , p):
    count = 0
    for i in lst:
        if (i*i)%p == 1:
            count+=1
    
    return count

