n = int(input())
unique_names = set()
for i in range(1, n+1):
    name = input()
    unique_names.add(name)
for person in unique_names:
    print(person)
