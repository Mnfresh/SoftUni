n = int(input())
list1 = []
list2 = []

for i in range(n):
    numbers = int(input())
    if numbers >= 0:
        list1.append(numbers)
    else:
        list2.append(numbers)

print(list1)
print(list2)
print(f"Count of positives: {len(list1)}")
print(f"Sum of negatives: {sum(list2)}")
