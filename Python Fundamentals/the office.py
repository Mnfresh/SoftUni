employees = [int(x) for x in input().split(' ')]
factor = int(input())
happy_count = [x * factor for x in employees ]
average = sum(happy_count)/len(happy_count)
count = 0
for i in happy_count:
    if i >= average:
        count +=1
if count >= len(happy_count):
    print(f"Score: {count}/{len(happy_count)}. Employees are happy!")
else:
    print(f"Score: {count}/{len(happy_count)}. Employees are not happy!")