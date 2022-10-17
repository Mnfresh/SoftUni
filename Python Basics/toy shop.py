price_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
price_toys = number_puzzles * 2.60 + number_dolls * 3 + number_bears * 4.10 \
             + number_minions * 8.20 + number_trucks * 2
number_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
if number_toys >= 50 :
    discount = 0.25 * price_toys
elif number_toys < 50 :
    discount = 0

total_price = price_toys - discount
rent = 0.10 * total_price
profit = total_price - rent
if profit > price_excursion :
    remainging = profit - price_excursion
    print(f"Yes! {remainging:.2f} lv left.")
elif profit < price_excursion :
    lacking = price_excursion - profit
    print(f"Not enough money! {lacking:.2f} lv needed.")












