# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# doctest:
import doctest
import csv
import pickle
import os
from task0 import PickleToCsvConverter


def test_pickle_to_csv():
    """
    >>> # Создание файла
    >>> data = {'name': 'John', 'age': 25}
    >>> with open('data1.pickle', 'wb') as f:
    ...     pickle.dump(data, f)

    >>> # Запуск конрертера
    >>> converter = PickleToCsvConverter()
    >>> converter.pickle_file = 'data1.pickle'
    >>> converter.csv_file = 'data1.csv'
    >>> converter.pickle_to_csv()

    >>> # Проверка файла
    >>> with open('data1.csv', 'r') as f:
    ...     reader = csv.DictReader(f)
    ...     rows = list(reader)
    >>> rows == [{'name': 'John', 'age': '25'}]
    True
    >>> # Очистка
    >>> os.remove('data1.pickle')
    >>> os.remove('data1.csv')
    """


def test_pickle_to_csv_invalid_data():
    """
    >>> converter = PickleToCsvConverter()
    >>> converter.pickle_file = 'invalid_data.pickle'
    >>> converter.csv_file = 'data.csv'
    >>> converter.pickle_to_csv()
    Traceback (most recent call last):
    ...
    ValueError: Данные в pickle файле должны быть словарем.
    """


def test_pickle_to_csv_no_pickle_file():
    """
    >>> converter = PickleToCsvConverter()
    >>> converter.csv_file = 'data.csv'
    >>> converter.pickle_to_csv()
    Traceback (most recent call last):
    ...
    FileNotFoundError: Файл отсутствует
    """


if __name__ == '__main__':
    doctest.testmod(verbose=True)
