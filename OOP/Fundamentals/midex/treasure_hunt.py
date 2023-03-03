loots = input().split('|')
sum_items = 0
while True:
        command = input().split(' ')

        if command[0] == 'Yohoho!':
            break

        if command[0] == 'Loot':
            for i in range(len(command)):
                if i == 0:
                    continue
                item = command[i]
                if item not in loots:
                    loots.insert(0, item)

        elif command[0] == 'Drop':
            idx = int(command[1])
            if 0 <= idx < len(loots):
                x = loots.pop(idx)
                loots.append(x)
            else:
                continue

        elif command[0] == 'Steal':
            n = int(command[1])
            if n >= len(loots):
                removed = loots
                print(', '.join(removed))
                print('Failed treasure hunt.')
                exit()
            else:
                removed = loots[-n:]
                del loots[-n:]
                print(', '.join(removed))

if len(loots) > 0:
            for i in range(len(loots)):
                sum_items += len(loots[i])

            avg = f'{sum_items / len(loots):.2f}'
            print(f'Average treasure gain: {avg} pirate credits.')



