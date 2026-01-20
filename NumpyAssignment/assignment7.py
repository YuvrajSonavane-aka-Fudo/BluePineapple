import numpy as np
'''
Create 100 random numbers (floats).
Find top 10 values and their indices using an efficient approach 
(argpartition).
Print top 10 sorted descending (values + indices aligned)
'''

#*random 100 number array
arr = np.random.rand(100)
print(f"The arr is {arr}")

top_10_index = np.argpartition(arr,-10)[-10:]
print(f"The top 10 index are {top_10_index}")

top_10_values = arr[top_10_index]
print(f"the top 10 values are : {top_10_values}")

sorted_order = np.argsort(top_10_values)[::-1]

final_index = top_10_index[sorted_order]
final_value = top_10_values[sorted_order]

print(f"{'Index':<8} | {'Value':<10}")
print("-" * 22)
for idx, val in zip(final_index, final_value):
    print(f"{idx:<8} | {val:.6f}")

