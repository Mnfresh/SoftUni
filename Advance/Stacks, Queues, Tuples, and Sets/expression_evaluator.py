from functools import reduce

expression = input().split(" ")
idx = 0

function = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i])
}
while idx < len(expression):
    el = expression[idx]

    if el in "*/+-":
        result = function[el](idx)
        [expression.pop(1) for i in range(idx)]
        expression[0] = result
        idx = 0

    idx += 1

print(int(expression[0]))

