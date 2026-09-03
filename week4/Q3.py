# 3. Given a list of numbers, write a program to turn every item of the list into its square.


li= list(map(int,input("enter a list of integer = ").split()))
print(list(map(lambda x:x**2,li)))


def square(x):
    return x**2

num= list(map(int,input("enter list = ").split()))
result =list(map(square,num))
print(result)
