# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# pytest:

import pytest
import csv
import pickle
import os
from task0 import PickleToCsvConverter


def test_pickle_to_csv():
    # Создание файла
    data = {'name': 'John', 'age': 25}
    with open('data1.pickle', 'wb') as f:
        pickle.dump(data, f)

    # Запуск конвертера
    converter = PickleToCsvConverter()
    converter.pickle_file = 'data1.pickle'
    converter.csv_file = 'data1.csv'
    converter.pickle_to_csv()

    # Проверка файла
    with open('data1.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows == [{'name': 'John', 'age': '25'}]

    # Очистка
    os.remove('data1.pickle')
    os.remove('data1.csv')


def test_invalid_pickle_format():
    # Создаем тестовый pickle файл с некорректным форматом данных
    pickle_file = 'invalid_data.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump('invalid_data', f)

    # Вызываем метод преобразования pickle в csv и ожидаем ValueError
    converter = PickleToCsvConverter()
    converter.pickle_file = pickle_file
    converter.csv_file = 'data.csv'

    with pytest.raises(ValueError):
        converter.pickle_to_csv()


if __name__ == '__main__':
    pytest.main(['-vv'])
