# 4. Given two Python lists, write a program to iterate both lists simultaneously and display items from list
# 1 in original order and items from list 2 in reverse order.


from itertools import zip_longest
l1= [1,2,3,4,5]
l2=[1,2,3,4,5,6,7]

for a,b in zip_longest(l1,reversed(l2),fillvalue=0):
    print(a,b)
    
# l3= [1,2,3,4,5]
# l4=[1,2,3,4,5,6,7]
# # l3,l4=list(map(int,input("enter the list 1 and list 2 = ").split(",")))
# for i in range(max(len(l3), len(l4))):
#     x=l3[i] if i<len(l3) else 0
#     y=l4[i+1] if i<len(l4) else 0
#     print(x,y)