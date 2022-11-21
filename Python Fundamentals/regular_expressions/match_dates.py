import re
dates = input()
valid_dated = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
result = re.findall(valid_dated, dates)
for match in result:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')