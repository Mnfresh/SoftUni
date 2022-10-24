sequences1 = input().split(', ')
sequences2 = input().split(', ')
list_result = []

for x in sequences1:
    for i in sequences2:
        if x in i:
            list_result.append(x)
            break
print(list_result)

