string = input().split(" ")
result = ""
for word in string:
    n = len(word)
    result += word * n
print(result)
