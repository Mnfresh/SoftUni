import math

Name = input()
budjet = float(input())
beers = int(input())
chips = int(input())

discount_chips = 45 / 100
price_for_beers = beers * 1.20
price_for_chips = discount_chips * price_for_beers
total_price_for_chips = math.ceil(price_for_chips * chips)
total_sum = total_price_for_chips + price_for_beers

if total_sum <= budjet:
    i = budjet - total_sum
    print(f"{Name} bought a snack and has {i:.2f} leva left.")
else:
    x = total_sum - budjet
    print(f"{Name} needs {x:.2f} more leva!")

