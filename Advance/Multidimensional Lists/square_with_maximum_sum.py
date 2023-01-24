import sys

rows, columns = tuple([int(x) for x in input().split(', ')])

matrix = [[int(x) for x in input().split(', ')] for line in range(rows)]

max_sum = -sys.maxsize
max_matrix = [[0 for x in range(2)] for _ in range(2)]


# 3 3 3 9
# 1 2 3 3
# 1 4 6 5


for r in range(rows-1):
    for c in range(columns-1):
        current_matrix_sum = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1]

        if current_matrix_sum > max_sum:
            max_sum = current_matrix_sum
            max_matrix[0][0] = matrix[r][c]
            max_matrix[0][1] = matrix[r][c+1]
            max_matrix[1][0] = matrix[r+1][c]
            max_matrix[1][1] = matrix[r+1][c+1]

[print(' '.join([str(x) for x in line])) for line in max_matrix]

print(max_sum)






