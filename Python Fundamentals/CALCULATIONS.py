def calculation(number_a,number_b,operation):
    result = 0
    if operation == 'multiply':
        result = number_a * number_b
        return result
    elif operation == "divide":
        result = number_a // number_b
        return result
    elif operation == "add":
        result = number_a + number_b
        return result
    elif operation == "subtract":
        result = number_a - number_b
        return result
operation = input()
number_a = int(input())
number_b = int(input())
print(calculation(number_a,number_b,operation))