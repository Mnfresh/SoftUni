country_names = input().split(", ")
capital_names = input().split(", ")
final_result = dict(zip(country_names, capital_names))
for key, value in final_result.items():
    print(f"{key} -> {value}")
