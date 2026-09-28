# 3. Write a Python program to calculate the sum of squares of the first two digits and the last two digits of
# a 4-digit number, e.g., for 1233, calculate 12^2 + 33^2.

num= (input("enter a 4 digit number = "))
sum_square= (lambda x,y: int(x)**2 + int(y)**2)(num[0:2], num[2:])
print(sum_square)