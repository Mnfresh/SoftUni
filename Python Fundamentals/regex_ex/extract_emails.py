import re
text = input()
search = r'\s([a-z0-9\.\-\_]+@[a-z\.\\-]+)\b'
match = re.findall(search, text)
print('\n'.join(match))