import re

number = int(input())
pattern = r"^([$|%])([A-Z][a-z]{2,})\1:\ \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"

for _ in range(number):
    message = input()
    result = re.match(pattern, message)

    if result:
        tag = result.group(2)
        decrypted_message = ''
        for num in result.groups():
            if num.isdigit():
                decrypted_message += chr(int(num))
        print(f'{tag}: {decrypted_message}')
    else:
        print('Valid message not found!')
