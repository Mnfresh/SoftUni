input_words = input()
new_words = []
for char in input_words:
    new_char = ord(char) + 3
    new_char_total = chr(new_char)
    new_words.append(new_char_total)
print(''.join(new_words))
