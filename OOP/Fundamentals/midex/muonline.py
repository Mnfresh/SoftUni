health = 100
bitcoins = 0
dungeon_rooms = input().split('|')
best_room_count = 0

for room in dungeon_rooms:
    room = room.split(' ')
    command = room[0]
    number = int(room[1])
    best_room_count += 1

    if command == 'potion':
        amount = 0
        if health + number > 100:
            amount = 100 - health
            health = 100
        else:
            amount = number
            health += number
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room_count}")
            break

if best_room_count == len(dungeon_rooms):
    print(f"You've made it.\nBitcoins: {bitcoins}\nHealth: {health}")
