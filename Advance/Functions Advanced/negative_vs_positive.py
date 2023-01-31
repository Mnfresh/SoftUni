from functools import reduce


def numbers(numbers):
    negative_numbers = []
    positive_numbers = []
    for number in numbers:
        if int(number) > 0:
            positive_numbers.append(int(number))
        elif int(number) < 0:
            negative_numbers.append(int(number))

    sum_of_positive_numbers = reduce(lambda x, y: x + y, positive_numbers)
    sum_of_negative_numbers = reduce(lambda x, y: x + y, negative_numbers)
    print(sum_of_negative_numbers)
    print(sum_of_positive_numbers)

    if sum_of_positive_numbers > abs(sum_of_negative_numbers):
        print("The positives are stronger than the negatives")
    elif abs(sum_of_negative_numbers) > sum_of_positive_numbers:
        print("The negatives are stronger than the positives")


numbers(input().split())
