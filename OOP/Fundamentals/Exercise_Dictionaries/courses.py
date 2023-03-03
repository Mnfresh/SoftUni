school = {}
while True:
    command = input()
    if command == 'end':
        break
    course, name = command.split(" : ")
    if course not in school:
        school[course] = []
    school[course].append(name)

for key, value in school.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")


