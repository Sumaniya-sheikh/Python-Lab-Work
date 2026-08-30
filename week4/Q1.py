# 1. Write a program to create a function cal_sum_sub() that accepts two variables and calculates addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def cal_sum_sub(a,b):
   add=  a+b
   sub= a-b
   return add, sub

a = int(input("enter first number = "))
b = int(input("enter second number = "))

add,sub =cal_sum_sub(a,b)
print(add, sub)
