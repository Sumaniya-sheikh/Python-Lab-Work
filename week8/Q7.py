num= list(map(int, input("Enter distinct integers even count =  ").split()))

if len(num) % 2 == 0 and len(num) == len(set(num)):
    mid=len(num) // 2
    first_half=num[:mid]
    second_half=num[mid:]
    if all(a < b for a, b in zip(first_half, second_half)):
        print("First list:", first_half)
        print("Second list:", second_half)
    else:
        print("Elements in the first list must be less than corresponding elements in the second list.")
else:
    print("Enter distinct integers with an even number of elements.")