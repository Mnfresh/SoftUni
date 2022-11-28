concealed_message = input()
while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring not in concealed_message:
            print("error")
            continue
        concealed_message = concealed_message.replace(substring, "", 1)
        reverse_substring = substring[::-1]
        concealed_message = concealed_message + reverse_substring
        print(concealed_message)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        count = concealed_message.count(substring)
        concealed_message = concealed_message.replace(substring, replacement, count)
        print(concealed_message)






