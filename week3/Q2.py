# 2. Write a program to print the following star pattern using the for loop:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1, 10):
        print()
        if i<=5:
             for j in range(1, i+1):
                                     print("*", end=" ")
        else:    
           for j in range(10-i):
                                  print("*", end=" ")
   