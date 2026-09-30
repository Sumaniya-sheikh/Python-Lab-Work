# 5. Write a program to get roll numbers, names, and marks of students and store these details in a file called
# ”Marks.data”

f= open("marks.data", "a")
f.write("Name\t\tRoll\t\tMarks\n")
num_std =int(input("Enter number of students: "))

for i in range(num_std):
    name=input("Enter the name of student = ")
    roll_no = input("enter the roll number of student = ")
    marks = input("enter the marks of student = ")
    f.write(name+"\t\t"+roll_no+"\t\t"+marks+"\n")
f.close()

f= open("marks.data", "r")
data=f.read()
print(data)
f.close()