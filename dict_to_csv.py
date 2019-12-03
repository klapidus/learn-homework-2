"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [{'name': 'Vasya', 'age': 14, 'job': 'journalist'},
              {'name': 'Masha', 'age': 27, 'job': 'writer'},
              {'name': 'Asya', 'age': 33, 'job': 'teacher'}]
    with open('people.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, people[0].keys(), delimiter=':')
        writer.writeheader()
        for person in people:
            writer.writerow(person)


if __name__ == "__main__":
    main()
