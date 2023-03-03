school = {}
command = input().split(":")
while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in school.keys():
        school[course] = []
    school[course].append(f"{name} - {id}")
    command = input().split(":")
find_course = command[0].replace("_", " ")
for student in school[find_course]:
    print(student)
