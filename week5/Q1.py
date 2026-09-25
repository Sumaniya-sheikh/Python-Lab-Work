import secrets
otp= secrets.randbelow(900000)+100000
print(otp)

# import random
# num= int(input("Enter the number of digits = "))
# digit= list("0123456789")
# random.shuffle(digit)
# otp="".join(digit[:num])
# print(otp)