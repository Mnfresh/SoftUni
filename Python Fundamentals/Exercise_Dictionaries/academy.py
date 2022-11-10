n = int(input())
dictionary = {}
for i in range(1, n+1):
    name = input()
    grade = input()
    if name not in dictionary:
        dictionary[name] = [grade]
    else:
        dictionary[name].append(grade)
for key, value in dictionary.items():
    total_sum = 0
    for number in value:
        total_sum += float(number)
    average_sum = total_sum/len(value)
    if average_sum >= 4.50:
        print(f"{key} -> {average_sum:.2f}")





