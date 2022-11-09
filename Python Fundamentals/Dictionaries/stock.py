key_value = input().split(' ')
products = input().split(' ')
market = {}
for index in range(0,len(key_value), 2):
    key = key_value[index]
    value = int(key_value[index+1])
    market[key] = value

for product in products:
    if product not in market.keys():
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {market[product]} of {product} left")