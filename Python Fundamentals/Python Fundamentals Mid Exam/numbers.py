def top_5(numbers):
    avg = sum(numbers) / len(numbers)

    if len(numbers) >= 5:

        temp_sum = [x for x in sorted(numbers, reverse=True) if x > avg]

        return ' '.join(map(str, temp_sum[:5]))

    else:

        return 'No'


numbers = list(map(int, input().split()))

print(top_5(numbers))
