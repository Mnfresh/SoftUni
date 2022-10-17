number = int(input())
for i in range(number):
    strings = input()
    if "," in strings or  "." in strings or "_" in strings:
        print(f"{strings} is not pure!")
    else:
        print(f"{strings} is pure.")
