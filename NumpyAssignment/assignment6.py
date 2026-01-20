import numpy as np
'''
Create a length-30 zero array.
Randomly pick 8 unique positions and set them to 1.
Then set positions divisible by 5 to 9 (overwriting if needed)
'''
#*array of zeroes of size 30
arr = np.zeros(30 , dtype = int)

#*randomly select 8 places
rng = np.random.default_rng()
choices = rng.choice(30 , size = 8 , replace = False)
print(f"The selected places are => {choices}")

#*set those choices to 1
arr[choices] = 1

#* set all places divisible by 5 to 9
arr[::5] = 9

print(f"The arr after the operations is => {arr}")

