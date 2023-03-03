import re

phone_numbers = input()

real_numbers = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

result = re.findall(real_numbers, phone_numbers)
print(', '.join(result))