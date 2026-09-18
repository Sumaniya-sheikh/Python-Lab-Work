l1= [1,2,3,4,5,6,5,3]
l2= [2 ,3, 4,8, 7, 6, 5,12,14]

new_l=[]

for i in l1:
    if i%2!=0:
        new_l.append(i)
for i in l2:
    if i%2==0:
        new_l.append(i)
print(new_l)