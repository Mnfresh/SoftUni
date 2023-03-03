text = input()
count = 0
while True:
    command = input().split(" ")
    if command[0] == 'Finish':
        break
    elif command[0] == 'Replace':
        currentChar = command[1]
        newChar = command[2]
        if currentChar in text:
            text = text.replace(currentChar, newChar)
        print(text)
    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])
        if len(text) > end_index >= start_index >= 0:
            text = text[:start_index:] + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")
    elif command[0] == 'Make':
        if command[1] == 'Upper':
            text = text.upper()
            print(text)
        elif command[1] == 'Lower':
            text = text.lower()
            print(text)
    elif command[0] == 'Check':
        string = command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command[0] == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])
        if len(text) > end_index >= start_index >= 0:
            substring = text[start_index:end_index+1]
            result = 0
            for ch in substring:
                result += ord(ch)
            print(result)

        else:
            print("Invalid indices!")





