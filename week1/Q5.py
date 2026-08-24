# 5. Write a program to calculate the cube of all numbers from 1 to a given number.
num=int(input("enter a three digit number = "))
for i in range(1, num):
    cube=i*i*i
    print(cube)