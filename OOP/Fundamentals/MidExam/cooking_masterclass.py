import math

budget = float(input())
students = int(input())
price_package_flour = float(input())
price_single_egg = float(input())
price_single_apron = float(input())
price_apron = price_single_apron * math.ceil(students + (students * 0.2))
price_eggs = price_single_egg * (10 * students)
free_pack_flour = 0
needed_money = 0
for student in range(1, students + 1):
    if student % 5 == 0:
        free_pack_flour += 1

needed_items_for_student = price_eggs + price_apron + price_package_flour * (students - free_pack_flour)

if budget >= needed_items_for_student:
    print(f"Items purchased for {needed_items_for_student:.2f}$.")
else:
    needed_money = needed_items_for_student - budget
    print(f"{needed_money:.2f}$ more needed.")


