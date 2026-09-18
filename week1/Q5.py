# 5. Write a program to calculate the cube of all numbers from 1 to a given number.
num=int(input("enter a number = "))
for i in range(1, num+1):
    cube=i*i*i
    print("Cube of", i, "is", cube)