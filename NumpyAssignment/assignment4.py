import numpy as np
#* Broadcasting

#TODO Create a 4,5 matrix of random floats
#TODO Create a (5,) vector then add this vector to every row 
#TODO Normalize matrix to have sums of 1

def create_array():
    '''creates array '''
    arr = np.random.rand(4,5)
    return arr    

def create_vector():
    '''create vector'''
    vector = np.random.rand(5)
    return vector

def add_vector_to_arr(arr, vector):
    '''add vector to arr'''
    result = arr+vector
    return result

def normalize_to_1(result):
    '''normalize all sums to be one'''
    row_sums = np.sum(result , axis = 1 , keepdims=True)
    normalized = result/row_sums
    return normalized

arr = create_array()
vector = create_vector()
print(f"Array is => {arr}")
print(f"Vector is => {vector}")

result = add_vector_to_arr(arr , vector)
print(f"Result of the addition is => {result}")

normalized_array = normalize_to_1(result)

print(f"Normalized array is => {normalized_array}")



