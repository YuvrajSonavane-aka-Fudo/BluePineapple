import numpy as np
#*Slicing and Boolean Masking

#TODO create an array of 50 random integers between 1 and 100
#TODO filter values 1. All even numbers . 2. Divisible by 3 and greater than 50
#TODO replace values less than 20 with 20

def create_random_array():
    '''Returns a random array of 50 integers with values between 1 and 100'''
    arr = np.random.randint(1,101, size = 50)
    return arr

def tasks(arr):
    '''Performs all tasks of the assignments and prints the result'''
    even_nums = arr[arr%2==0]
    div_by_3greater_than_50 = arr[(arr%3==0) & (arr>50)]
    arr[arr<20] = 20
    print(f"Even Numbers => {even_nums}")
    print(f"Divisible by 3 and greater than 50 => {div_by_3greater_than_50}")
    print(f"Values less than 20 replaced with 20 => {arr}")

arr = create_random_array()
tasks(arr)
