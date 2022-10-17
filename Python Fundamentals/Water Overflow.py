water_tank = 255
total_litres = 0
number_of_lines = int(input())
for i in range(number_of_lines):
    liters_water = int(input())
    if water_tank - liters_water < 0:
        print("Insufficient capacity!")
        continue
    water_tank -= liters_water
    total_litres += liters_water
print(total_litres)






