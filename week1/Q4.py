# 4. Write a program to check if the given number is a palindrome



# num=int(input("enter a three digit number = "))
# original=num
# rev=0
# while num>0:
#     number = num%10
#     rev=rev*10+number
#     num=num//10
    
# if original==rev:
#     print("number is palindrome ")       
# else:
#     print("number is not palindrome")

num=(input("enter a number = "))
if str(num)==str(num)[::-1]:
    print("palindrome")
else:
    print("not palindrome")

