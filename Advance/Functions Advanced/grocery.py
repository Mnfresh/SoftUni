def grocery_store(**products):
    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return '\n'.join([f"{k}: {v}" for k, v in products])


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

