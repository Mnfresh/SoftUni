characters = input().split(", ")
ascii_table = {}
for character in characters:
    key = character
    ascii_table[key] = ord(character)
print(ascii_table)
