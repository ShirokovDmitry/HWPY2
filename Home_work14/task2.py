# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# unittest:

import unittest
import csv
import pickle
import os
from task0 import PickleToCsvConverter


class TestPickleToCsv(unittest.TestCase):
    def setUp(self):
        # Создание файла
        self.data = {'name': 'John', 'age': 25}
        with open('data1.pickle', 'wb') as f:
            pickle.dump(self.data, f)

        self.converter = PickleToCsvConverter()
        self.converter.pickle_file = 'data1.pickle'
        self.converter.csv_file = 'data1.csv'

    def tearDown(self):
        # Очистка
        os.remove('data1.pickle')
        os.remove('data1.csv')

    def test_pickle_to_csv(self):
        # Запуск конвертера
        self.converter.pickle_to_csv()

        # Проверка файла
        with open('data1.csv', 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        self.assertEqual(rows, [{'name': 'John', 'age': '25'}])


class TestPickleToCsvConverter(unittest.TestCase):
    def test_missing_pickle_file(self):
        converter = PickleToCsvConverter()
        converter.pickle_file = 'nonexistent.pickle'
        converter.csv_file = 'nonexistent.csv'

        # Проверяем, что при попытке преобразовать отсутствующий файл возникает ошибка FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            converter.pickle_to_csv()

        # Проверяем, что CSV файл не был создан
        self.assertFalse(os.path.exists('nonexistent.csv'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
