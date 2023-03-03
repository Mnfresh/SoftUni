company = {}
while True:
    command = input()
    if command == "End":
        break
    name , id = command.split(" -> ")
    if name not in company:
        company[name] = []
    if id not in company[name]:
        company[name].append(id)

for key, value in company.items():
    print(key)
    for i in value:
        print(f"-- {i}")

