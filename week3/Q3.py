# 3. Write a program to print characters from a string which are present at even index numbers.
str="Sumaniya"
for i in range(len(str)):
    if i%2==0:
        print(str[i])    