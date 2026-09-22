#  Write a program to create a numpy array and return an array of odd rows and even columns from the
# numpy array.
import numpy as np

arr = np.array([
    [30, 20, 10],
    [3,  1,  2],
    [9,  7,  8],
    [4, 5,   6],
    [1, 2,   3],
    [7, 0,   1]
])

print("Original Array")
print(arr)
result= arr[::2][1::2]
print("resul")
print(result)