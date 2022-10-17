number_of_leters = int(input())
for first_number in range (number_of_leters):
    for second_number in range(number_of_leters):
        for third_number in range(number_of_leters):
            print(f"{chr(97+ first_number)}{chr(97 + second_number)}{chr(97 + third_number)}")

