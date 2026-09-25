# 1. Write a Python program that inputs two tuples and creates a third that contains all elements of the first
# followed by all elements of the second.

tup1= tuple(map(int,input("enter numbers for tuple1 = ").split))
tup2=tuple(map(int,input("enter numbers for tuple2 = ").split))

tup3= tup1 + tup2
print("contains all element from tup1 to tup2 = ",tup3)