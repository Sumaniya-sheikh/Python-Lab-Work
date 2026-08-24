# 1. Write a program to extract each digit from an integer in reverse order.

num=int(input("enter number = "))
while num>0:
    digit= num%10
    print(digit)
    num=num//10