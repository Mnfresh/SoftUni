rows = int(input())
matrix = []
for row in range(rows):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)


def sum_of_diagonal_primary(matrix):
    sum_of_diagonal_primary = [matrix[i][i] for i in range(len(matrix))]

    return sum_of_diagonal_primary


all_elements = []
for el in sum_of_diagonal_primary(matrix):
    all_elements.append(str(el))


def sum_of_secondary_diagonal(matrix, rows):
    sum_of_secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]

    return sum_of_secondary_diagonal


difference_of_diagonals = sum(sum_of_diagonal_primary(matrix)) - sum(sum_of_secondary_diagonal(matrix, rows))

if difference_of_diagonals < 0:
    difference_of_diagonals = sum(sum_of_secondary_diagonal(matrix, rows)) - sum(sum_of_diagonal_primary(matrix))

print(difference_of_diagonals)
