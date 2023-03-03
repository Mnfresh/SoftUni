travel_route = input().split('||')
starting_fuel_amount = int(input())
starting_ammunition_amount = int(input())

for command in travel_route:
    command = command.split(' ')

    if 'Travel' in command:
        number = int(command[1])
        starting_fuel_amount -= number
        if starting_fuel_amount >= 0:
            print(f"The spaceship travelled {number} light-years.")
        else:
            print("Mission failed.")
            break
    elif 'Enemy' in command:
        number = int(command[1])
        if starting_ammunition_amount >= number:
            starting_ammunition_amount -= number
            print(f"An enemy with {number} armour is defeated.")
        elif starting_fuel_amount - number * 2 >= 0:
            starting_fuel_amount -= number * 2
            print(f"An enemy with {number} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif 'Repair' in command:
        number = int(command[1])
        starting_fuel_amount += number
        starting_ammunition_amount += number * 2
        print(f"Ammunitions added: {number*2}.")
        print(f"Fuel added: {number}.")
    elif 'Titan' in command:
        print(f"You have reached Titan, all passengers are safe.")
        break