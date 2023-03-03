status_of_pirate_ship = [int(x) for x in input().split('>')]
status_of_the_war_ship = [int(x) for x in input().split('>')]
maximum_health = int(input())
count = 0
lose = True


while True:
    command = input().split()
    if command[0] == 'Retire':
        break

    if command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_of_the_war_ship):
            status_of_the_war_ship[index] -= damage
            if status_of_the_war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                lose = False
                break
        else:
            continue
    if command[0] == 'Defend':
        startIndex = int(command[1])
        endIndex = int(command[2])
        damage = int(command[3])
        if 0 <= startIndex and endIndex < len(status_of_pirate_ship):
            for idx in range(startIndex,endIndex+1):
                status_of_pirate_ship[idx] -= damage
                if status_of_pirate_ship[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lose = True
                    break
        else:
            continue

    if command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if 0 <= index <= len(status_of_pirate_ship):
            status_of_pirate_ship[index] += health
            if status_of_pirate_ship[index] > maximum_health:
                amount = status_of_pirate_ship[index] - maximum_health
                status_of_pirate_ship[index] -= amount
        else:
            continue

    if command[0] == 'Status':
        for section in status_of_pirate_ship:
            if section < maximum_health * 0.20:
                count += 1
        print(f"{count} sections need repair.")

if not lose:
    print(f"Pirate ship status: {sum(status_of_pirate_ship)}")
    print(f'Warship status: {sum(status_of_the_war_ship)}')








