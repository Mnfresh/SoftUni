def function(data_items):
    while True:
        command_data = input()
        if command_data == 'Craft!':
            break
        command, product = command_data.split(' - ')
        if command == 'Collect':
            if product not in data_items:
                data_items.append(product)
        elif command == 'Drop':
            if product in data_items:
                data_items.remove(product)
        elif command == 'Combine Items':
            old, new = product.spit(':')
            if old in data_items:
                old_item_index = data_items.index(old)
                data_items.insert(old_item_index + 1, new)

        elif command == 'Renew':
            if product in data_items:
                data_items.remove(product)
                data_items.append(product)

    print(', '.join(data_items))


items = input().split(', ')










