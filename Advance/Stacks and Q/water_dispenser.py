from _collections import deque

def add_names_in_deque():
    people_data = deque()
    while True:
        name = input()
        if name == COMMAND_START:
            break
        people_data.append(name)

    return people_data

COMMAND_START = 'Start'
COMMAND_END = 'End'
COMMAND_REFILL = 'refill'
water_in_dispenser = int(input())
people_queue = add_names_in_deque()

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{water_in_dispenser} liters left")
        break
    elif command.startswith(COMMAND_REFILL):
        refill_command_data = command.split(' ')
        water_amount = int(refill_command_data[1])
        water_in_dispenser += water_amount
    else:
        person = people_queue.popleft()
        current_litres = int(command)

        if current_litres <= water_in_dispenser:
            print(f"{person} got water")
            water_in_dispenser -= current_litres
        else:
            print(f"{person} must wait")







