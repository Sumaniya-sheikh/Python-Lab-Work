# Swap middle line of first file with last line of second file
f1 = open("file1.txt", "r")
lines1 = f1.readlines()
f1.close()

f2 = open("file2.txt", "r")
lines2 = f2.readlines()
f2.close()

middle = len(lines1) // 2

temp = lines1[middle]
lines1[middle] = lines2[-1]
lines2[-1] = temp

f1 = open("file1.txt", "w")
f1.writelines(lines1)
f1.close()

f2 = open("file2.txt", "w")
f2.writelines(lines2)
f2.close()

print("Content swapped successfully")