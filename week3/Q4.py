# 4. Write a program to accept a string from the user and display characters that are present at even index
# numbers.
str= input("enter a string = ")
for i in range(len(str)):
    if i%2==0:
        print(str[i])