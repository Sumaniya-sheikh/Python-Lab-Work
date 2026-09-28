# import numpy as np

# a = np.random.randint(200, 251, size=(100, 10))

# print("Selling Price Array:")
# print(a)

# # Index of product having maximum selling price
# index = np.unravel_index(np.argmax(a), a.shape)

# print("Index of product with maximum selling price:",
#       index[0])

# # Product number 10
# product_10 = a[9]

# # Index of city having lowest price for product 10
# city_index = np.argmin(product_10)

# print("Index of city with lowest selling price for product 10:",
#       city_index)


# x, y, z = int(input("x = ")), int(input("y = ")), int(input("z = "))
x, y, z = input().split()
x,y,z=int(x), int(y), int(z)
print("x:", x, "y:", y, "z:", z)