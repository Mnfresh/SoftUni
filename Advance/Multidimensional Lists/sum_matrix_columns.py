rows, columns = map(int, input().split(','))
matrix = []
for row in range(rows):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)

sum_of_columns = []
rows = len(matrix)
cols = len(matrix[0])
for i in range(cols):
    col_sum = 0
    for j in range(rows):
        col_sum += matrix[j][i]

    sum_of_columns.append(col_sum)

for x in sum_of_columns:
    print(x)



