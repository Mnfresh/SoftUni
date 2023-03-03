dictionary = {}
count = 0
while True:
    data = input().split("-")
    if data[0] == "Stop":
        if dictionary:
            for key, value in dictionary.items():
                print(f"{key}: {', '.join(value)}")
        print(f"Unliked meals: {count}")

        break
    elif data[0] == "Like":
        guest = data[1]
        meal = data[2]
        if guest not in dictionary:
            dictionary[guest] = [meal]
        if meal not in dictionary[guest]:
            dictionary[guest].append(meal)
    elif data[0] == "Dislike":
        guest = data[1]
        meal = data[2]
        if guest in dictionary and meal in dictionary[guest]:
            dictionary[guest].remove(meal)
            count += 1
            print(f"{guest} doesn't like the {meal}.")
        elif guest in dictionary and meal not in dictionary[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif guest not in dictionary:
            print(f"{guest} is not at the party.")




