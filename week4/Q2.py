# 2. Write a function to return True if the first and last number of a given list are the same. If the numbers
# are different, return False.

def check_list(l):
    return l[0]==l[-1]
l= list(map(int,input("enter a list of integer = ").split()))
print(check_list(l))