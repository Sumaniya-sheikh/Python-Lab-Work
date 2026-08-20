# 5. Write a program to find the sum of the digits of a supplied integer.
num=int(input("enter the number = "))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)