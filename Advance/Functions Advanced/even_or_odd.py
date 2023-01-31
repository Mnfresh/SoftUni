def even_odd(*args):
    even_numbers = []
    odd_numbers = []
    if args[-1] == 'even':
        for el in args:
            if type(el) == int:
                if el % 2 == 0:
                    even_numbers.append(el)
        return even_numbers
    elif args[-1] == 'odd':
        for el in args:
            if type(el) == int:
                if el % 2 != 0:
                    odd_numbers.append(el)
        return odd_numbers








