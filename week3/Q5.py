# 5. Write a program to remove characters from a string starting from the nth position to the last and return
# a new string. Example: remove_chars(”aligarh”, 3) should output ali.
def remove_chars(str,num):return str[:num]
str= input("enter a string = ")
num=int(input("enter the position = "))
print(remove_chars(str,num))