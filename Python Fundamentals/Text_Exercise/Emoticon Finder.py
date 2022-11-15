single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ":":   #if single_string[index] == ":" and index != len(single_string) - 1:
        print(f":{single_string[index + 1]}")
