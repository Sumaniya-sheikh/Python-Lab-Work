# 4. Write a program to use a loop to find the factorial of a given number

# num=int(input("enter a number = "))
# fact=1
# for i in range(1, num+1):
#     fact=fact*i 
# print(fact)


# def fact(num):
#     if num<=1:
#         return 1
#     return num * fact(num-1)
# num=int(input("enter a number = "))
# print("factorial",fact(num))
     
# n=int(input("enter a number =")); fact=lambda n: 1 if n<=1 else n*fact(n-1);
# print(fact(n))

from functools import reduce;
n=int(input("enter a number = ")); fact=(reduce(lambda x,y: x*y, range(1,n+1),1))
print(fact)