from enum import unique

n = int(input())
unique_elements = set()
all_elements = []
for number in range(1,n+1):
    chemical_elements = input().split(' ')
    for chemical_element in chemical_elements:
        all_elements.append(chemical_element)

for element in all_elements:
    if element not in unique_elements:
        unique_elements.add(element)

for z in unique_elements:
    print(z)
