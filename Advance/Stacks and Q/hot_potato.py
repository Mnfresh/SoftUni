from _collections import deque


kids_names = input().split(' ')
step_of_hot_patato = int(input())
kids_deque = deque(kids_names)
counter = 0

while len(kids_deque) > 1:
    counter += 1
    current_name_of_player = kids_deque.popleft()
    if counter == step_of_hot_patato:
        print(f'Removed {current_name_of_player}')
        counter = 0
    else:
        kids_deque.append(current_name_of_player)

print(f'Last is {kids_deque[0]}')