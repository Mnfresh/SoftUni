name = input()
quantity = int(input())
result = 0
price = 0
if name == 'coffee':
    price = 1.50
elif name == 'coke':
    price = 1.40
elif name == 'water':
    price = 1.00
elif name == 'snacks':
    price = 2.00
result = lambda price , quantity: price * quantity
print(f"{result(price,quantity):.2f}")