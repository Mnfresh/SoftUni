def total_number(number1):
    sum_of_odd = 0
    sum_of_even = 0
    for i in number1:
        if int(i) %2 == 0:
           sum_of_even += int(i)
        elif int(i) %2 != 0:
            sum_of_odd += int(i)
    print(f'Odd sum = {sum_of_odd}, Even sum = {sum_of_even}')

number = input()
total_number(number)
