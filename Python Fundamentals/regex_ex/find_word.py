import re
text = input()
word = input()
search = fr"\b{word}\b"
matches = re.findall(search, text, re.IGNORECASE)
print(len(matches))