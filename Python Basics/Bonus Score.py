people = int(input())
price_enter = float(input())
price_chaise_longue = float(input())
price_umbrella = float(input())

price_enter_for_all_people = people * price_enter
price_for_umbrella_for_people = (people * 0.5) * price_umbrella
price_for_chaise_longue = (people * 0.75) * price_chaise_longue

total = price_for_chaise_longue + price_enter_for_all_people + price_for_umbrella_for_people
print(f"{total:.2f} lv." )