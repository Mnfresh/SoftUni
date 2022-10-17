n = int(input())
for num in range(1, n + 1):
    sum_of_degits = 0
    digits = num
    while digits > 0:
        sum_of_degits += digits % 10
        digits = int(digits /10)
    if (sum_of_degits == 5) or (sum_of_degits == 7) or (sum_of_degits == 11):
       print(f"{num} -> True")
    else:
       print(f"{num} -> False")

