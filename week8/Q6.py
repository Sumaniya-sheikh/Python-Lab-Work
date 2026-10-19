# import csv
file = open("data.csv", "r")
data = file.read()
file.close()

vowels = "aeiouAEIOU"
count = {}

for vow in vowels:
    count[vow] = data.count(vow)

max_count = max(count.values())

print("Vowel Count:")
for vowel, cnt in count.items():
    print(f"{vowel}: {cnt}")


for vowel, cnt in count.items():
    if cnt == max_count:
        print("maximum number of instances of ", vowel, "= ", cnt)







# with open("data.csv", "w", newline="") as f:
#     w = csv.writer(f)

#     w.writerow(["ID", "Text"])
#     w.writerow([1, "Hello World 123"])
#     w.writerow([2, "Python Programming 456"])
#     w.writerow([3, "Education 789"])
#     w.writerow([4, "Artificial Intelligence 2026"])
#     w.writerow([5, "Beautiful Flowers 12345"])

# print("CSV file created successfully!")

