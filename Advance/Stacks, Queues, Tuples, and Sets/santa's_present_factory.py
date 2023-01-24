from _collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())
dictionary = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

while materials and magic_levels:

    material = materials.pop()
    magic = magic_levels.popleft()

    if material * magic == 150:
         dictionary["Doll"] += 1
    elif material * magic == 250:
        dictionary["Wooden train"] += 1
    elif material * magic == 300:
        dictionary["Teddy bear"] += 1
    elif material * magic == 400:
        dictionary["Bicycle"] += 1
    else:
        if material * magic < 0:
            result = material + magic
            materials.append(result)
        elif material * magic > 0:
            new_material = material + 15
            materials.append(new_material)
        elif material == 0:
            magic_levels.appendleft(magic)
        elif magic == 0:
            materials.append(material)


if dictionary["Doll"] and dictionary["Wooden train"] or dictionary["Teddy bear"] and dictionary["Bicycle"]:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:

    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")


myKeys = list(dictionary.keys())
myKeys.sort()
sorted_dict = {i: dictionary[i] for i in myKeys}


for k, v in sorted_dict.items():
    if v > 0:
        print(f"{k}: {v}")















