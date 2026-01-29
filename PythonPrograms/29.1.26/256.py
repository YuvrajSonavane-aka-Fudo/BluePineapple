
#* number of primes less than a non negative number

def  is_prime(n):
    for i in range(2 , n):
        if n%i == 0:
            return False
    return True

def number_of_primes(number):
    
    '''
    Docstring for number_of_primes
    
    :param number: Returns number of prime numbers less than non negative number
    '''
    count = 0
    for i in range(2 ,number):
        if is_prime(i):
            count+=1
    return count

print(number_of_primes(7))

