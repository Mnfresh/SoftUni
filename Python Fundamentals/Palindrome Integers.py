def palindrome_numbers(numbers):
    for i in numbers:
        reversed_number_list = list(i)
        reversed_number_list.reverse()
        reversed_number_list = ''.join(reversed_number_list)

        if i == reversed_number_list:
            print('True')
        else:
            print('False')

int_numbers = input().split(', ')
palindrome_numbers(int_numbers)