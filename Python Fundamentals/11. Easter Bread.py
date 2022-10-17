budget = float(input())
price_one_kg_flour = float(input())
budget_left = 0
bread_total = 0
eggs_total = 0
eggs_lose = 0
price_for_pack_eggs = 75 * price_one_kg_flour / 100
price_liter_milk = price_one_kg_flour + (price_for_pack_eggs * 25)/ 100
price_for_250ml_milk = price_liter_milk / 4
one_bread_price = price_for_250ml_milk + price_for_pack_eggs + price_one_kg_flour
one_bread_price = eggs_total * 3
eggs_lose = bread_total - 2
budget_left = budget - bread_
print(f"You made {bread_total} loaves of Easter bread! Now you have {eggs_total} eggs and {budget_left:.2f}BGN left.")