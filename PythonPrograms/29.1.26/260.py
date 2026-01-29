
#*newman shanks williams prime number

def calculate_nth_newman_shanks_williams_number(n):

    if n == 0:
        return 1
    
    if n == 1 :
        return 1
    
    return (2* calculate_nth_newman_shanks_williams_number(n-1)) + (calculate_nth_newman_shanks_williams_number(n-2))

print(calculate_nth_newman_shanks_williams_number(7))