import re
data = input()
regex = r'(=|\/)[A-Z][A-Za-z]{2,}\1'
all_destination = []
points = 0
valid_data = re.finditer(regex,data)
for destination in valid_data:
    current_destination = re.split('\/|=',destination.group())[1]
    all_destination.append(current_destination)
    points+= len(current_destination)
print(f"Destinations: {', '.join(all_destination)}")
print(f"Travel Points: {points}")

