
string = input("Enter a string = ")
uppercase = 0
lowercase = 0
alphabets = 0
digits = 0
symbols = 0
for i in string:
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase+=1
    if i.isalpha():
        alphabets+=1
    if i.isdigit():
        digits+=1
    if not i.isalpha() and not i.isdigit():
        symbols += 1
print("Number of uppercase letters = ",uppercase)
print("Number of lowercase letters = ",lowercase)       
print("Number of alphabets = ",alphabets)
print("Number of digits = ",digits)
print("Number of symbols = ",symbols)