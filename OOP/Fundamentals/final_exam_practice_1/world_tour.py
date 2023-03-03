stops = input()
while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break
    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
            print(stops)
        else:
            print(stops)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if len(stops) > end_index >= start_index >= 0:
            stops = stops[:start_index:] + stops[end_index + 1:]
            print(stops)
        else:
            print(stops)

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            count = stops.count(old_string)
            stops = stops.replace(old_string, new_string, count)
            print(stops)
        else:
            print(stops)


