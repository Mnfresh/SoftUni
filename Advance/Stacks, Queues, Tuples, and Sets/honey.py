from collections import deque

working_bees = deque(int(x) for x in input().split())
nectarines = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

honey = 0

operations = {
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y,
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
}

while working_bees and nectarines:
    bee = working_bees.popleft()
    nectar = nectarines.pop()
    
    if nectar < bee:
        working_bees.appendleft(bee)
    elif nectar > bee:
        honey += abs(operations[symbols.popleft()](bee, nectar))

print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectarines:
    print(f"Nectar left: {', '.join(str(x) for x in nectarines)}")




