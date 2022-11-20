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

Purchase = TypedDict('Purchase', {'id': str, 'name': str, 'price': float})

g = (i for i in range(1,5000000000))


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
                    print(f'{data[i]["id"]}.  {data[i]["name"]} цена - {data[i]["price"]}')
        except (Exception,):
            pass

    def find_purchase(field):
        for i in range(len(data)):
            if data[i]["id"] == field:
                res = data[i]
                print(f'{res["id"]}.   {res["name"]} цена - {res["price"]}')
            elif data[i]["name"] == field:
                res = data[i]
                print(f'{res["id"]}.   {res["name"]} цена - {res["price"]}')
            elif data[i]["price"] == float(field):
                res = data[i]
                print(f'{res["id"]}.   {res["name"]} цена - {res["price"]}')
            else:
                print('Ничего не найдено')


    def most_expensive():
        m = data[0]["price"]
        for i in range(len(data)):
            if data[i]["price"] > m:
                res = data[i]
                print('res')
        # print(f'{res["id"]}.   {res["name"]} цена - {res["price"]}')

    def delete_purchase(id):
        del data[id]
        return delete_purchase

    return [add_purchase, all_purchases, most_expensive, delete_purchase, find_purchase]


add, all, expensive, delete, find = notes()

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
            try:
                price = float(input('Введите цену '))
            except  Exception as err:
                print('Цена должна быть цифровым значением')
            purchase: Purchase = {'id': id, 'name': name, 'price': price}
            add(purchase)

        case '2':
            all()

        case '3':
            field = str(input('Введите строку для поиска '))
            find(field)

        case '4':
            expensive()

        case '5':
            id = int(input('Введите номер покупки '))
            delete(id)

        case '6':
            break
