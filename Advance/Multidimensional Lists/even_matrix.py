number_of_rows = int(input())
matrix = []

for _ in range(number_of_rows):
    current_row = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(current_row)

print(matrix)
