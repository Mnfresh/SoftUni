dictionary = {}
while True:
    data = input().split("||")
    if data[0] == 'Sail':
        break
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city not in dictionary:
        dictionary[city] = [population, gold]
    else:
        dictionary[city][0] += population
        dictionary[city][1] += gold

while True:
    data1 = input().split("=>")
    command = data1[0]

    if command == "End":
        if dictionary:
            print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
            for grad, value in dictionary.items():
                print(f"{grad} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")

    elif command == "Plunder":
        town = data1[1]
        people = int(data1[2])
        gold = int(data1[3])
        dictionary[town][0] = dictionary[town][0] - people
        dictionary[town][1] = dictionary[town][1] - gold
        if dictionary[town][0] > 0 and dictionary[town][1] > 0:
            print(f"{town} plundered! {gold} gold stolen, {people} "
                  f"citizens killed.")
        else:
            del dictionary[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        town = data1[1]
        gold = int(data1[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            dictionary[town][1] = dictionary[town][1] + gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town][1]} gold.")


