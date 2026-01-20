import numpy as np
#*assignment 1 Numpy
#TODO 1. Create a 1D array from 1 to 20 
#TODO 2. Print shape , dtype , min , max , mean , sum
#TODO 3. Convert to float and show dtype change

def create_array(start , end):
    '''Creates a numpy array in the given start and end range'''
    arr = np.array([i for i in range(start , end+1)])
    return arr

def print_functions():
    '''simple function that just prints '''
    arr = create_array(1,20)
    print(arr.shape) #*shows dimension of matrix
    print(arr.dtype) #*shows datatype
    print(arr.min())
    print(arr.max())
    print(arr.sum())

    float_arr = arr.astype(float)
    print(float_arr.dtype)

print_functions()








