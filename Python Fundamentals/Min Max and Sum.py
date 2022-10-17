def function(numbers):
    my_list = []
    for i in numbers:
        my_list.append(int(i))
        minimum_number = min(my_list)
        max_number = max(my_list)
        sum_number = sum(my_list)
    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_number}")


int_numbers = input().split(' ')
function(int_numbers)
