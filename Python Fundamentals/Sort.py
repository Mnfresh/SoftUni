def sorted_numbers(total_numbers):
    list_numbers = []
    for i in total_numbers:
        list_numbers.append(int(i))
        list_numbers.sort()
    return list_numbers



numbers = input().split(' ')
print(sorted_numbers(numbers))