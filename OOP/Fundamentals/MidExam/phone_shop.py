phones = input().split(', ')
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        print(', '.join(phones))
        break
    if command[0] == 'Add':
        if command[1] not in phones:
            phones.append(command[1])
        else:
            continue
    elif command[0] == 'Remove':
        if command[1] in phones:
            phones.remove(command[1])
        else:
            continue

    elif command[0] == 'Bonus phone':
        comand = command[1].split(':')
        old = comand[0]
        new = comand[1]
        if old in phones:
            idx = phones.index(old)
            phones.insert(idx+1, new)

    elif command[0] == 'Last':
        if command[1] in phones:
            phones.remove(command[1])
            phones.append(command[1])



