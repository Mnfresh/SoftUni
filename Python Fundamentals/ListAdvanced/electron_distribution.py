number = int(input())
new_list = []
total = 0
i = 0

while 0 <= number:
    i += 1
    shell = 2*i**2
    total += shell
    new_list.append(shell)
    number -= shell
    if number < 18:
        if number > 0:
            new_list.append(number)
        break

    if number == 0:
        new_list.append(number)
        break
    if i % 3 == 0:
        i = 0


print(new_list)