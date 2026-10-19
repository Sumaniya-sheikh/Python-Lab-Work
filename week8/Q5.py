
alpha_numeric= "abcde1f2g4h5i6j7k8l9m1n2o3p4q0rstuvwxyz"

l1=[i for i in alpha_numeric if i.isdigit()]
l2=[i for i in alpha_numeric if i.isalpha()]

# for i in alpha_numeric:
#     if i.isdigit():
#         l1.append(i)
#     else:
#         if i.isalpha():
#             l2.append(i)

print("All the digits are :", l1)
print("All the alphabets are:", l2) 