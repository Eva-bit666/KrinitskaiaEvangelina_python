#Вариант 1
#Задание 1
f = open('books-en.csv', encoding='cp1251')
ls = [list(i.split(';')) for i in f]
#Убираем строку с заголовком
ls = ls[1:]

count = 0
for Book_title in ls:
    if len(Book_title[1]) > 30:
        count += 1

print(count)

f.close()
#Задание 2
f = open('books-en.csv', encoding='cp1251')
ls = [list(i.split(';')) for i in f]
ls = ls[1:]

#Поиск через словарь
print('Введите имя автора')
Search = input()
dct = {i[2]: [i[1], i[6]] for i in ls}

if Search in dct and float(dct[Search][1].replace(',', '.')) < 150:
    print(dct[Search][0], dct[Search][1])

elif Search in dct and float(dct[Search][1].replace(',', '.')) > 150:
    print('Книга дороже 150 рублей. Показать её нельзя!!!')
else:
    print('Автор не найден. Проверьте имя и фамилию автора!')

f.close()
#Задание 3
import random
try:
    f = open('books-en.csv', encoding='cp1251')
    ls = [list(i.split(';')) for i in f]

    random_numbers = []
    for i in range(20):
        random_numbers.append(random.randint(0, len(ls)-1))
    with open('bibliography.txt', 'w', encoding='utf-8') as file:
        for i, enter in enumerate(random_numbers, 1):
            file.write(f'{i}. {ls[enter][2]}. {ls[enter][1]}-{ls[enter][3]}\n')

    f1 = open('bibliography.txt', encoding='utf-8').read()
    print(f1)
except FileNotFoundError:
    print('Файл не найден!')
finally:
    f.close()
#Доп.задание 1
try:
    with open('books-en.csv', encoding='cp1251') as file:
        ls = [list(i.split(';')) for i in file][1:]
        #Уберём повторы
        Uniq_Publisher = set(i[4] for i in ls)
    print(Uniq_Publisher)
except FileNotFoundError:
    print('Файл не найден!')
#Доп.задание 2
try:
    with open('books-en.csv', encoding='cp1251') as file:
        ls = [list(i.split(';')) for i in file][1:]
        #Сортировка по скачиваниям
        ls_sorted = sorted(ls, key=lambda x: int(x[-2]) if x[-2].isdigit() else 0)[::-1]
        Popular = [Book[1] for Book in ls_sorted[:20]]
        print(Popular)
except FileNotFoundError:
    print('Файл не найден!')
#Currency.xml
import xml.dom.minidom as minidom
try:
    with open('currency.xml', encoding='utf-8') as f:
        dom = minidom.parse(f)

        Valutes = dom.getElementsByTagName('Valute')
        currency_dict = {}

        for valu in Valutes:
            name = valu.getElementsByTagName('Name')[0].firstChild.nodeValue
            value = valu.getElementsByTagName('Value')[0].firstChild.nodeValue
            #Перекодируем название валюты в правильную кодировку
            name = name.encode('latin-1').decode('cp1251')
            currency_dict[name] = float(value.replace(',', '.'))

        print(currency_dict)
except FileNotFoundError:
    print('Файл не найден!')





