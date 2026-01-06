
#!find nth hexagonal number

def find_NTH_HEXA_NUMBER(n):
    if n<0 or n==0:
        return 0
    
    return n*(2*n -1)

print(find_NTH_HEXA_NUMBER(-2))