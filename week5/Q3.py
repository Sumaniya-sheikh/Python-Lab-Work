# 3. Write a program to generate a random password that meets the following conditions:
# a. Password length must be 10 characters long.
# b. It must contain at least 2 uppercase letters, 1 digit, and 1 special symbol.
import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*"

password = [
    random.choice(uppercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special)
]


all_characters = uppercase + lowercase + digits + special

for i in range(6):
    password.append(random.choice(all_characters))


random.shuffle(password)

password = ''.join(password)

print("Random Password:", password)