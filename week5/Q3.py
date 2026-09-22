import random
import string

uppercase = random.choices(string.ascii_uppercase, k=2)
digit = random.choice(string.digits)
special = random.choice("!@#$%^&*")

remaining = random.choices(
    string.ascii_letters + string.digits + "!@#$%^&*",
    k=6
)
password_list = uppercase + [digit] + [special] + remaining

random.shuffle(password_list)

password = ''.join(password_list)

print("Random Password:", password)

