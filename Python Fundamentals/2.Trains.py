number = int(input())
wagons = [0 for wag in range(number)]
while True:
    command = input()
    if command == 'End':
        break

    command = command.split(' ')
    if command[0] == 'add':
        people = int(command[1])
        wagons[-1] += people
    elif command[0] == 'insert':
        index = int(command[1])
        people = int(command[-1])
        wagons[index] += people
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[-1])
        wagons[index] -= people
print(wagons)



