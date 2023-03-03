import re
text_string = input()
mirror_words = []
total = 0
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern,text_string)
for data in result:
    if data[1] == data[3][::-1]:
        mirror_words.append(f"{data[1]} <=> {data[3]}")

    total += 1

if total > 0:
    print(f"{total} word pairs found!")
    if not mirror_words:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(mirror_words))
else:
    print("No word pairs found!")
    print("No mirror words!")


