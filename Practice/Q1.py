# def is_special_number(n):
#     # Check divisible by 5
#     if n % 5 != 0:
#         return False

#     # Check palindrome
#     if str(n) != str(n)[::-1]:
#         return False

#     # Find digit sum
#     digit_sum = 0
#     temp = n

#     while temp > 0:
#         digit_sum = digit_sum + temp % 10
#         temp = temp // 10

#     # Check even digit sum
#     if digit_sum % 2 == 0:
#         return True

#     return False


# count = 0

# for n in range(100, 1000):
#     if is_special_number(n):
#         print(n)
#         count = count + 1

# print("Count =", count)


# s = input("Enter string: ")
# idx = int(input("Enter index: "))

# remaining = s[:idx]          # truncate from idx
# vowels = "aeiouAEIOU"
# v = c = 0
# for ch in remaining:
#     if ch in vowels:
#         v += 1
#     elif ch.isalpha():
#         c += 1

# if v > c:
#     result = ""
#     for ch in s:             # replace vowels with ASCII in ORIGINAL string
#         if ch in vowels:
#             result += str(ord(ch))
#         else:
#             result += ch
#     print(result)
# else:
#     print(remaining[::-1])   # reverse the remaining string

n = int(input("Enter integer: "))
factorials = []

for i in range(1, n + 1):
    for j in range(i, n + 1):        # row i prints i to n
        print(j, end=" ")
    print()

    f = 1
    for k in range(1, i + 1):        # factorial of the row's start (i)
        f *= k
    factorials.append(f)

print("Factorials:", factorials)
print("Total:", sum(factorials))
print("Maximum:", max(factorials))
print("Minimum:", min(factorials))