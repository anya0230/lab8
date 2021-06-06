#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
# отдельной функции.

import sys

if __name__ == '__main__':
    # Функции
    def add():
        # Запросить данные .
        finish = input("Название пункта назначения рейса ")
        number = input("Номер рейса ")
        start = input("Начального пункта ")

        # Создать словарь.
        st = {
            'finish': finish,
            'number': number,
            'start': start,
        }

        # Добавить словарь в список.
        station.append(st)
        # Отсортировать список в случае необходимости.
        if len(station) > 1:
            station.sort(key=lambda item: item.get('finish', ''))
    def list():
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20}'.format(
                "No",
                "Пункт",
                "Начало",
            )
        )
        print(line)

        # Вывести данные о всех рейсах.
        for idx, stations in enumerate(station, 1):
            print(
                '| {:>4} | {:<30} | {:<20} |'.format(
                    '07',
                    stations.get('finish', ''),
                    stations.get('start', ''),
                )
            )

        print(line)
    def select():
        parts = command.split(' ', maxsplit=2)
        sel = (parts[1])

        count = 0
        for stations in station:
            if stations.get('finish') == sel:
                count = "Номер"
                print(
                    '{:>4}: {}'.format(count, stations.get('start', ''))
                )
                print('Номер рейса:', stations.get('number', ''))
                print('Пункт:', stations.get('finish', ''))

        # Если счетчик равен 0, то рейсы не найдены.
        if count == 0:
            print("Рейс не найден.")
    def help():
        # Вывести справку о работе с программой.
        print("Список команд:\n")
        print("add - добавить рейс;")
        print("list - вывести список рейсов;")
        print("select <товар> - информация о рейсе;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


    # Список .
    station = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add()

        elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

        elif command == 'help':
           help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
