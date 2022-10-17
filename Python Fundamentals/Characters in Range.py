def collect_characters(fisrt,second):
    characters = []
    for current_character in range(ord(fisrt) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters

fist_character = input()
second_character = input()
print(' '.join(collect_characters(fist_character,second_character)))