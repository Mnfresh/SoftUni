secret_mess = input().split(' ')
listttt  = []
for word in secret_mess:
    word = list(word)
    number = []
    list_m = []
    for element in word:
        if element.isdigit():
            number.append(element)
        else:
            list_m.append(element)
    integer_number = ''.join(number)
    char_of_number = chr(int(integer_number))
    list_m.insert(0, char_of_number)

    second = list_m[1]
    last = list_m[-1]
    list_m[1] = last
    list_m[-1] = second
    listttt.append(''.join(list_m))

print(' '.join(listttt))
