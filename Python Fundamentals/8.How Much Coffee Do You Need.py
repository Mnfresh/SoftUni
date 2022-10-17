coffie = 0
while True:
    command = str(input())
    if command == 'END':
        break
    elif command in ['coding','dog','cat','movie']:
        coffie += 1
    elif command in ['CODING','DOG','CAT','MOVIE']:
        coffie += 2
    else:
        continue
if coffie <=5:
    print(coffie)
else:
    print('You need extra sleep')
