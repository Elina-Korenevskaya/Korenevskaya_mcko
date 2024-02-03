import csv


name = input()
k = []
with open('game.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='$')
    for index, row in file:
        if index != 0:
            k.append(row[1])
if k:
    k = sorted(k)
    if len(k) > 5:
        for j in range(5):
            print(k[j])
        print('и др.')
    else:
        for j in range(len(k)):
            print(k[j])
else:
    print('Такого персонажа не существует')


