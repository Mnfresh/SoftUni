def rhombus_data(data):
    for x in range(data):
        space_data = data - x - 1
        stars_data = x + 1
        print_function(space_data, stars_data)
    for x in range(data-2,-1,-1):
        space_data = data - x - 1
        stars_data = x + 1
        print_function(space_data, stars_data)


def print_function(space_data, stars_data):
    print(' ' * space_data + '* ' * stars_data)


size = int(input())
rhombus_data(size)