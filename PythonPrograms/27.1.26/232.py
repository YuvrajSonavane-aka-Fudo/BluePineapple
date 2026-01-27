import numpy as np
#* retrieve n max elements from a dataset
dataset = [1,2,4,5,6,7]

def retrieve_n_max_elements(dataset , n):
    '''Accepts a dataset and returns the n max elements in that dataset '''

    if n>len(dataset):
        return -1

    arr = np.array(dataset)
    max_values = np.partition(arr , -n)[-n:]
    return (max_values)

print(retrieve_n_max_elements(dataset , 6))
