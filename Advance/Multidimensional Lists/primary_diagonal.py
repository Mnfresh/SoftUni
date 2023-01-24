rows = int(input())
matrix = []
for row in range(rows):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)


def sum_of_diagonal_primary(matrix):
    sum_of_diagonal_primary = [matrix[i][i] for i in range(len(matrix))]

    return sum(sum_of_diagonal_primary)

print(sum_of_diagonal_primary(matrix))

