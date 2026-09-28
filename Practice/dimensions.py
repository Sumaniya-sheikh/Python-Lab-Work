import numpy as np

arr_1d= np.array([1,2,3,4,5])
arr_2d= np.array([[1,2,3], [4,5,6]])
arr_3d= np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print("1D array:", arr_1d)
print("1D array shape:", arr_1d.shape)
print("1D array size:", arr_1d.size)
print("1D array dimensions:", arr_1d.ndim)

print("2D array:", arr_2d)
print("2D array shape:", arr_2d.shape)
print("2D array size:", arr_2d.size)
print("2D array dimensions:", arr_2d.ndim)  


print("3D array:", arr_3d)
print("3D array shape:", arr_3d.shape)
print("3D array size:", arr_3d.size)
print("3D array dimensions:", arr_3d.ndim)
