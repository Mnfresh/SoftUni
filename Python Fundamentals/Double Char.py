while True:
    text = str(input())
    if text == "End":
        break
    elif text == "SoftUni":
        continue
    output = ''
    for i in text:
        output = output + i*2
    print(output)



