n = int(input())
parking_info = [input() for _ in range(n)]
unique_numbers = set()
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for record in parking_info:
    command, number = record.split(', ')

    if command == COMMAND_IN:
        unique_numbers.add(number)
    elif command == COMMAND_OUT:
        unique_numbers.remove(number)
if unique_numbers:
    for plate_number in unique_numbers:
        print(plate_number)
else:
    print("Parking Lot is Empty")



