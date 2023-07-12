# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import csv
import pickle


def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise ValueError("Данные в pickle файле должны быть словарем.")

    all_keys = set()
    for d in data:
        all_keys.update(d.keys())
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv('data1.pickle', 'data1.csv')
