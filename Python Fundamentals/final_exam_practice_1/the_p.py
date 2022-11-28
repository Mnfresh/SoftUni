n = int(input())
dictionary = {}
for number in range(1, n+1):
    pieces = input()
    pieces_themselves, composer, key = pieces.split("|")
    dictionary[pieces_themselves] = [composer, key]
while True:
    command = input()
    if command == "Stop":
        sortedDict = dict(sorted(dictionary.items(), key=lambda x: (x[0], x[1][0])))
        for k, v in sortedDict.items():
            print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")
        break

    elif "Add" in command:
        command = command.split("|")
        pieces = command[1]
        composer = command[2]
        key = command[3]
        if pieces not in dictionary:
            dictionary[pieces] = [composer, key]
            print(f"{pieces} by {composer} in {key} added to the collection!")
        else:
            print(f"{pieces} is already in the collection!")
    elif "Remove" in command:
        piece = command.split("|")[1]
        if piece in dictionary:
            del dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif "ChangeKey" in command:
        command, piece, new_key = command.split("|")
        if piece in dictionary:
            dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")




