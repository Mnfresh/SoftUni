n = int(input())
unique_names = set()
for number in range(1,n+1):
    name = input()
    if name not in unique_names:
        unique_names.add(name)

for names in unique_names:
    print(names)

