import re
text = input()
search = r'\b_([a-zA-Z0-9]+)\b'
matches = re.findall(search, text)
print(','.join(matches))