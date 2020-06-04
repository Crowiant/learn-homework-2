"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


list_of_dict = [
    {'name': 'Boris', 'age': 55, 'job': 'Electric engineer'},
    {'name': 'Daria', 'age': 35, 'job': 'Automation engineer'},
    {'name': 'Nastya', 'age': 25, 'job': 'Biologist'},
    {'name': 'Vasya', 'age': 18, 'job': 'Manager'},
    {'name': 'Elina', 'age': 25, 'job': 'Programmer'},
    {'name': 'Alexander', 'age': 25, 'job': 'Medician'}
]


def main(some_list: list):
    with open('csv_train.csv', 'a', encoding='utf-8') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for dictn in some_list:
            writer.writerow(dictn)


if __name__ == "__main__":
    main(list_of_dict)
