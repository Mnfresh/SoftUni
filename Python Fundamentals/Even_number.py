numbers = input().split(', ')
indices = []
for index in range(len(numbers)):
    number = int(numbers[index])
    if number %2 == 0:
        indices.append(index)

print(indices)