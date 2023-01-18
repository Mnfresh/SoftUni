n, m = input().split(' ')
set_one = set()
set_two = set()
sum_of_n_m = int(n) + int(m)

for i in range(1,int(n)+1):
    number = int(input())
    set_one.add(number)
for z in range(1,int(m)+1):
    number = int(input())
    set_two.add(number)

for i in set_one:
    if i in set_two:
        print(i)
















