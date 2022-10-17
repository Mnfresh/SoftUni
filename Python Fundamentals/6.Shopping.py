budget = int(input())
comand = input()

while comand != "End":
    product_price = int(comand)
    budget -= product_price
    if budget < 0:
        print("You went in overdraft!")
        break
    comand = input()
else:
    print("You bought everything needed.")


