food_grams = float(input()) * 1000
hay_grams = float(input()) * 1000
cover_grams = float(input()) * 1000
pig_weight = float(input()) * 1000
flag = False
for day in range(1,31):
    food_grams -= 300
    if day % 2 == 0:
        hay_grams -= food_grams * 0.05
    if day % 3 == 0:
        cover_grams -= pig_weight / 3

    if food_grams <= 0 or hay_grams <= 0 or cover_grams <= 0 :
        flag = True
        break
if not flag:
    food, hay, cover = food_grams/1000, hay_grams/1000, cover_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")