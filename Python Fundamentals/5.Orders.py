number_of_orders = int(input())
total_price = 0
for i in range(number_of_orders):
    price_for_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_for_capsule < 0.01 or price_for_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_for_capsule * capsules_per_day * days
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
