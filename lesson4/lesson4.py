# try:
#     with open ('emails.txt') as file_read, open ('emails_gmail.txt', mode='w') as file_write:
#         for line in file_read:
#             if line.endswith('@gmail.com\n'):
#                 file_write.write(line)
# except Exception as err:
#     print(err)

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

from typing import TypedDict
import json

from pip._internal.utils import models

Purchase = TypedDict('Purchase', {'id': str, 'name': str, 'price': str})

g = (i for i in range(5000000000))


def notes():
    data = []

    def add_purchase(purchase: Purchase):
        nonlocal data
        data.append(purchase)

        try:
            with open('purchases.json', 'w') as file:
                json.dump(data, file)
        except (Exception,):
            pass
        return add_purchase

    def all_purchases():
        try:
            with open('purchases.json', 'r') as file:
                purchase: Purchase = json.load(file)
                for i in range(len(data)):
                    print(f'{data[i]["id"]} {data[i]["name"]} {data[i]["price"]}')
        except (Exception,):
            pass

    def most_expensive():
        for i in range(len(data)):
            m=data[i]["price"]
            if data[i]["price"]>m:
                m = data[i]["price"]
        print(f'{data[i]["id"]} {data[i]["name"]} {data[i]["price"]}')


    return [add_purchase, all_purchases, most_expensive]


add, all, expensive = notes()

while True:
    print('1. Добавить в список ')
    print('2. Посмотреть все ')
    print('3. Поиск покупки ')
    print('4. Самая дорогая покупка ')
    print('5. Удалить покупку по номеру ')
    print('6. Вихід')
    choice = input('Сделайте выбор: ')

    match choice:
        case '1':
            id = str(next(g))
            name = input('Введите название ')
            price = int(input('Введите цену '))
            purchase: Purchase = {'id': id, 'name': name, 'price': price}
            add(purchase)

    match choice:
        case '2':
            all()

    match choice:
        case '4':
            expensive()

    match choice:
        case '6':
            break
