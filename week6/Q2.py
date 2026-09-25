# 2. Write a Python program to create a dictionary with names and phone numbers. Then ask the user for a
# name and print the corresponding phone number
user={
    "Sumaniya":4746375862,
    "Hadiya":8766375862,
    "Rashika":3986375843,
}
name=input("input name = ")
for key in user:
    if key.casefold()==name.casefold():
        print(user[key])
