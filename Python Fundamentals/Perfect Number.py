def perfect_number(current_number):
    sum = 0
    for divisior in range(1,current_number):
        if current_number % divisior == 0:
            sum += divisior
    if sum == current_number:
        print("We have a perfect number!" )
    else:
        print("It's not so perfect." )

number = int(input())
perfect_number(number)