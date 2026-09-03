# 1. Write a program to create a function cal_sum_sub() that accepts two variables and calculates addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def cal_sum_sub(a,b):
    return a+b, a-b

a,b = map(int,input("enter first number = ").split())

print(cal_sum_sub(a,b))
