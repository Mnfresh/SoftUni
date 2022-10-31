import math

sum_prices = 0
taxes = 0
price_with_taxes = 0
discount = 0
while True:
    prices = input()
    if prices == 'regular':
        if price_with_taxes == 0:
            print("Invalid order!")
        else:
            print(f"Congratulations you've just bought a new computer!\n\
Price without taxes: {sum_prices}$\n\
Taxes: {taxes}$\n\
-----------\n\
Total price: {price_with_taxes:.2f}$")
        break
    elif prices == 'special':
        if price_with_taxes == 0:
            print("Invalid order!")
        else:
            discount = price_with_taxes - ((price_with_taxes * 10)/100)

            print(f"Congratulations you've just bought a new computer!\n\
Price without taxes: {sum_prices}$\n\
Taxes: {taxes}$\n\
-----------\n\
Total price: {discount:.2f}$")
        break
    elif float(prices) <= 0:
        print("Invalid price!")
        continue

    else:
        sum_prices += float(prices)
        taxes = math.floor(sum_prices * 20)/100
        round(taxes, 2)
        price_with_taxes = sum_prices + taxes







