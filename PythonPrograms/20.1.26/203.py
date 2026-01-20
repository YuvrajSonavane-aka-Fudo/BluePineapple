
#* calculate hamming distance between two integers

def calculate_hamming_distance(int1 , int2):
    '''Accepts two integers . returns hamming distance between them'''
    binary_int1 = bin(int1)
    binary_int2 = bin(int2)

    exor = int1^int2
    count = 0
    for i in bin(exor):
        if i == "1":
            count += 1
    return count
    
print(calculate_hamming_distance(-5 , -0))