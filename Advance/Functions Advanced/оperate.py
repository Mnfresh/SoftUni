from functools import reduce

def operate(*args):
    operation, *numbers = args

    if operation == "+":
        return reduce(lambda x, y: x + y, numbers)
    elif operation == "-":
        return reduce(lambda x, y: x - y, numbers)

    elif operation == "*":
        return reduce(lambda x, y: x * y, numbers)
    elif operation == "/":
        return reduce(lambda x, y: x / y, numbers)
