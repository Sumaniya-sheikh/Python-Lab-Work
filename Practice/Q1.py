def is_special_number(n):
    if n%5==0:
        return False
    if str(n)!=str(n)[::-1]:
        return False

    digit_sum=0
    temp=n
    while temp>0:
       digit_sum= digit_sum+temp%10
       temp=temp//10

  
       if digit_sum%2==0:
           return True
       return False

    for n in range(100, 1000):
        if is_special_number(n):
            print(n)