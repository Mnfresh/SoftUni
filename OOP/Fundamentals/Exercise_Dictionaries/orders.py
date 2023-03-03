import math

dictionary = {}
while True:
    info = input()
    if " " not in info:
        break
    name, price, quantity = info.split(" ")

    if name not in dictionary:
        dictionary[name] = {'price': float(price), 'quantity': float(quantity)}
    else:
        dictionary[name]['quantity'] += float(quantity)
        if dictionary[name]['price'] != float(price):
            dictionary[name]['price'] = float(price)


for name in dictionary.keys():
    total_price = dictionary[name]['price'] * dictionary[name]['quantity']
    print(f"{name} -> {total_price:.2f}")












