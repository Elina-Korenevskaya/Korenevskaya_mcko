import csv


name = input() #пользователь вводит имя персонажа
k = [] #в этот список мы будем добавлять игры
with open('game.csv', encoding='utf-8') as file: #открываем файл
    reader = csv.reader(file, delimiter='$') #делаем список и разделяем все по $
    for index, row in file:
        if index != 0:
            if row[1] == name: #проверяем подходит ли нам эта игры(есть ли в ней заданный персонаж)
                k.append(row[0]) #добавляем название игр
if k:
    k = sorted(k) #сортируем
    if len(k) > 5:
        for j in range(5):
            print(k[j])
        print('и др.')
    else:
        for j in range(len(k)):
            print(k[j])
else:
    print('Такого персонажа не существует')


