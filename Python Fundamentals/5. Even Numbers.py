def even_numbers(total_numbers):
    list_numbers = []
    for i in total_numbers:
        if int(i) %2 == 0:
         list_numbers.append(int(i))
    return list_numbers



numbers =input().split(' ')
print(even_numbers(numbers))