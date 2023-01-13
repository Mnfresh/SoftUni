huge_box_of_clothes = input().split(" ")
capacity_for_one_rack = int(input())
start_capacity = capacity_for_one_rack
stack = []
count = 1
for clothes in huge_box_of_clothes:
    stack.append(int(clothes))
while stack:
    clothes_out = stack.pop()
    if clothes_out <= capacity_for_one_rack:
        capacity_for_one_rack -= clothes_out
    else:
        capacity_for_one_rack = start_capacity - clothes_out
        count += 1
print(count)


