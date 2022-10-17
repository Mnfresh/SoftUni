cats = int(input())
from100to200 = 0
from200to300 = 0
from300to400 = 0
total_price = 0
for i in range(cats):
    gr_food = float(input())
    if 100 <= gr_food < 200:
        from100to200 += 1
    elif 200 <= gr_food < 300:
        from200to300 += 1
    elif 300 <= gr_food < 400:
        from300to400 += 1
    total_price += gr_food
print(f"Group 1: {from100to200} cats.")
print(f"Group 2: {from200to300} cats.")
print(f"Group 3: {from300to400} cats.")
print(f"Price for food per day: {total_price / 1000 * 12.45:.2f} lv.")



