# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

import csv
import pickle


class PickleToCsvConverter:
    def __init__(self):
        self.pickle_file = None
        self.csv_file = None

    def pickle_to_csv(self):
        with open(self.pickle_file, 'rb') as f:
            data = pickle.load(f)

        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            raise ValueError("Данные в pickle файле должны быть словарем.")

        all_keys = set()
        for d in data:
            all_keys.update(d.keys())
        with open(self.csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=all_keys)
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    converter = PickleToCsvConverter()
    converter.pickle_file = 'data1.pickle'
    converter.csv_file = 'data1.csv'
    converter.pickle_to_csv()
