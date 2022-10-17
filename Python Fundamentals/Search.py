n = int(input())
name = input()
my_list = []
for i in range(n):
    strings = input()
    my_list.append(strings)
print(my_list)
for i in range(len(my_list) -1,-1,-1):
    if name not in my_list[i]:
        my_list.pop(i)

print(my_list)





