activationKey = input()
while True:
    data = input().split('>>>')
    command = data[0]
    if command == 'Generate':
        print(f"Your activation key is: {activationKey}")
        break
    elif command == 'Contains':
        substring = data[1]
        if substring in activationKey:
            print(f"{activationKey} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        start_index = int(data[2])
        end_index = int(data[3])
        old_string = activationKey[start_index:end_index]
        if data[1] == 'Upper':
            new_string = old_string.upper()
            activationKey = activationKey.replace(old_string, new_string, 1)
            print(activationKey)
        elif data[1] == 'Lower':
            new_string = old_string.lower()
            activationKey = activationKey.replace(old_string, new_string, 1)
            print(activationKey)

    elif command == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])
        if len(activationKey) > end_index >= start_index >= 0:
            activationKey = activationKey[:start_index:] + activationKey[end_index:]
            print(activationKey)




