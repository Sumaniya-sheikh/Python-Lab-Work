import numpy as np

arr = np.array([
    [30, 20, 10],
    [3,  1,  2],
    [9,  7,  8]
])

print("Original Array:")
print(arr)
# a.	Case 1: Sort the array by the second row.
index = np.argsort(arr[1])

result = arr[:,  index]

print("Sorted by second row:")
print(result)

# b.	Case 2: Sort the array by the second column.
index = np.argsort(arr[:, 1])

result = arr[index]

print("Sorted by second column:")
print(result)