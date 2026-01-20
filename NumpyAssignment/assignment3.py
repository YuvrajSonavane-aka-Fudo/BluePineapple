import numpy as np
#* reshaping and axis

#TODO Create an array from 1 to 60 and reshape into (5, 12)
#TODO row wise sums , column wise means , global std
#TODO find index of the maximum value in the 2d array

def create_array():
    '''creates the array from 1 to 60 and reshape into 5 rows 12 columns'''
    arr = np.arange(1,61).reshape(5,12)
    print(f"array is =>\n {arr}\n")
    return arr

def aggregate_functions(arr):
    '''performs operations on the array and prints the results'''
    row_wise_sums = np.sum(arr , axis = 1)
    column_wise_means = np.mean(arr , axis = 0)
    global_std = np.std(arr)
    flat_index = np.argmax(arr)
    twoD_index = np.unravel_index(flat_index , arr.shape)

    
    print(f"Row wise sum => {row_wise_sums}")
    print(f"Column wise mean => {column_wise_means}")
    print(f"Global standard deviation => {global_std}")
    print(f"Index of max element => {twoD_index}")

arr = create_array()
aggregate_functions(arr)

    