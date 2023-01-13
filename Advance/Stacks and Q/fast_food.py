from _collections import deque
quantity_of_the_food = int(input())
quantity_of_food_in_each_order = input().split(" ")
queue = deque()
list= []
for number in quantity_of_food_in_each_order:
    queue.append(int(number))

print(max(queue))
total_orders = len(queue)
while queue:
    client = queue.popleft()
    if client <= quantity_of_the_food:
        quantity_of_the_food -= client
        total_orders -= 1
    else:
        queue.insert(0, client)
        break
if total_orders == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in queue])}")



