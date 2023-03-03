number_rooms = int(input())
free_chairs = 0
is_true = True
for x in range(number_rooms):
    chairs_visitors = input().split(' ')
    if len(chairs_visitors[0]) > int(chairs_visitors[-1]):
        free_chairs += len(chairs_visitors[0]) - int(chairs_visitors[-1])
    elif len(chairs_visitors[0]) < int(chairs_visitors[-1]):
        print(f'{int(chairs_visitors[-1]) - len(chairs_visitors[0])} more chairs needed in room {x+1}')
        is_true = False
if is_true:
    print(f"Game On, {free_chairs} free chairs left")