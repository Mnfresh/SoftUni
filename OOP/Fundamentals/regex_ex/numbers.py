import re
text = input()
search_pattern = r"[0-9]+"
while text:
    matches = re.findall(search_pattern, text)
    if matches:
        print(' '.join(matches), end=' ')
    text = input()

