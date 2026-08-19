# num=int(input("enter a number = "))
# fact=1
# for i in range(1, num+1):
#     fact=fact*i 
# print(fact)


def fact(num):
    if num<=1:
        return 1
    return num * fact(num-1)
num=int(input("enter a number = "))
print("factorial",fact(num))