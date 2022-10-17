n = int(input())
my_list = []
filter_list = []
for i in range(n):
    numbers = int(input())
    my_list.append(numbers)
comand = input()
for i in range(len(my_list)):
    if comand == 'even' and my_list[i] %2 == 0:
        filter_list.append(my_list[i])
    elif comand == 'odd'and my_list[i] %2 != 0:
        filter_list.append(my_list[i])
    elif comand == 'negative'and my_list[i] < 0:
        filter_list.append(my_list[i])
    elif comand == 'positive'and my_list[i] >= 0:
        filter_list.append(my_list[i])
print(filter_list)