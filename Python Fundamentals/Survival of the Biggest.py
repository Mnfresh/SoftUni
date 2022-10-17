list_numbers = input().split()
list_numbers_digits = []
n = int(input())
for element in list_numbers:
    list_numbers_digits.append(int(element))

for i in range(n):
    min_element = min(list_numbers_digits)
    list_numbers_digits.remove(min_element)

for idx in range(len(list_numbers_digits)):
    element = list_numbers_digits[idx]
    if idx < len(list_numbers_digits) -1:
        print(element,end=', ')
    else:
        print(element)