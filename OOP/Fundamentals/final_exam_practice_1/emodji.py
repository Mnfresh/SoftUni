import re
data = input()
coolnumber = 1
qki_emodjita = []
pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
result = re.findall(pattern, data)
for number in data:
    if number.isdigit():
        coolnumber *= int(number)
for emoji in result:
    count = 0
    new_emoji = emoji[1]

    for char in new_emoji:
        count += ord(char)

    if count > coolnumber:
        qki_emodjita.append(emoji[0] + new_emoji + emoji[0])

print(f"Cool threshold: {coolnumber}")
print(f"{len(result)} emojis found in the text. The cool ones are: ")
for valid_emoji in qki_emodjita:
    print(valid_emoji)