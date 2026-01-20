import numpy as np
'''
Create a 1D float array of size 40.
Randomly turn 20% positions into np.nan.
Compute mean ignoring NaNs.
Replace NaNs with the median of non-NaN values

'''

arr = np.random.rand(40)
print(f"the arr -> {arr}")

rng = np.random.default_rng()

choices = rng.choice(40 , size = int(0.2 * 40), replace = False)
arr[choices] = np.nan
print(f"the arr after replacing some values with nan -> {arr}")

arr_mean = np.nanmean(arr)
print(f"the arr mean without taking into consideration nan is -> {arr_mean}")

arr_median = np.nanmedian(arr)
print(f"the meadian is ->{arr_median}")

arr[np.isnan(arr)] = arr_median
print(f"the arr after replacing nan values is -> {arr}")



