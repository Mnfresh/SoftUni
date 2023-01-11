from _collections import deque
queue = deque()
command_end = "End"
command_paid = "Paid"
while True:
    command = input()
    if command == command_end:
        print(f"{len(queue)} people remaining.")
        break
    elif command == command_paid:
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)