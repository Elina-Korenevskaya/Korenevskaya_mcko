import csv


with open('game.csv', encoding='utf-8') as file: #открываем файл
    reader = csv.reader(file, delimiter='$') #делаем список и разделяем все по $
    with open('game_new.csv', mode='w', encoding='utf-8') as file_new:
    # открываем новый файл для записи
        file_wr = csv.writer(file_new, delimiter="$")#в эту переменную мы будем записывать новые данные и разделять по $
        for index, row in file:
            if index != 0:
                if '55' in row[2]: #проверяем есть ли число 55 в ошибке
                    print(f'У персонажа {row[1]} в игре {row[0]} нашлась ошибка с кодом: {row[2]}')
                    # пишем отчет об ошибке
                    file_wr.writer(row[0], row[1], 'Done', '000-00-00') #записываем новые данные



