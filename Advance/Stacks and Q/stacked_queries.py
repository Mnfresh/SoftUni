stack = []
list = []
integer = int(input())
for number in range(1, integer + 1):
    command = input()
    if command.startswith("1"):
        command_data = command.split(" ")
        current_number = int(command_data[1])
        stack.append(current_number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

while stack:
    list.append(str(stack.pop()))

print(", ".join(list))

