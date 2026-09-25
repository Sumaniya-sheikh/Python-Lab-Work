# #  Write a program to create a numpy array and return an array of odd rows and even columns from the
# # numpy array.
# import numpy as np

# arr = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])

# print("Original Array")
# #  Write a program to create a numpy array and return an array of odd rows and even columns from the
# # numpy array.
# import numpy as np

# arr = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])

# print("Original Array")
# print(arr)
# result= arr[::2][1::2]
# print("result : ", result)

# result= arr[::2, 1::2]
# print("result : ", result)
# #  Write a program to create a numpy array and return an array of odd rows and even columns from the
# # numpy array.
# import numpy as np

# arr = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])

# print("Original Array")
# print(arr)
# result= arr[::2][1::2]
# print("result : ", result)
#  Write a program to create a numpy array and return an array of odd rows and even columns from the
# numpy array.
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [0, 19, 17, 18],
    [13, 14, 15, 16]
])

print("Original Array")
print(arr)
result= arr[::2, 1::2]
print("result : ")
print(result)
