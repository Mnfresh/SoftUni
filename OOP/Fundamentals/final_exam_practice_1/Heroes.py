n = int(input())
dictionary = {}
for number in range(1, n+1):
    info = input().split(" ")
    hero_name, HP, MP = info[0], int(info[1]), int(info[2])
    if 0 < HP <= 100 and 0 < MP <= 200:
        dictionary[hero_name] = [HP, MP]
while True:
    command = input().split(" - ")
    if command[0] == 'End':
        for name, list1 in dictionary.items():
            if list1[0] > 0:
                print(f"{name}")
                print(f" HP: {list1[0]}")
                print(f" MP: {list1[1]}")
        break

    elif command[0] == 'CastSpell':
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if dictionary[hero_name][1] >= mp_needed:
            new_mp = dictionary[hero_name][1] - mp_needed
            dictionary[hero_name][1] = new_mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {dictionary[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        dictionary[hero_name][0] = dictionary[hero_name][0] - damage
        if dictionary[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == 'Recharge':
        hero_name = command[1]
        amount = int(command[2])
        dictionary[hero_name][1] = dictionary[hero_name][1] + amount
        if dictionary[hero_name][1] > 200:
            mana_needed = 200 - (dictionary[hero_name][1] - amount)
            dictionary[hero_name][1] = 200
            print(f"{hero_name} recharged for {mana_needed} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        hero_name = command[1]
        amount = int(command[2])
        dictionary[hero_name][0] = dictionary[hero_name][0] + amount
        if dictionary[hero_name][0] > 100:
            heal_needed = 100 - (dictionary[hero_name][0] - amount)
            dictionary[hero_name][0] = 100
            print(f"{hero_name} healed for {heal_needed} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")


