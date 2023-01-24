matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
new_matrix = []
for row in matrix:
    for num in row:
        new_matrix.append(num)
print(new_matrix)

