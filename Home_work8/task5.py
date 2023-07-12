# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
#  Для дочерних объектов указывайте родительскую директорию.
#  Для каждого объекта укажите файл это или директория.
#  Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []

    def traverse_dir_recursive(dir_path):
        files = []
        size = 0

        for entry in os.scandir(dir_path):
            if entry.is_file():
                file_size = entry.stat().st_size
                results.append({
                    'name': entry.name,
                    'path': dir_path,
                    'type': 'file',
                    'size': file_size
                })
                files.append(entry.name)
                size += file_size
            elif entry.is_dir():
                subdir_size, subdir_files = traverse_dir_recursive(entry.path)
                results.append({
                    'name': entry.name,
                    'path': dir_path,
                    'type': 'directory',
                    'size': subdir_size
                })
                files.extend(subdir_files)
                size += subdir_size

        return size, files

    total_size, _ = traverse_dir_recursive(directory)

    with open('results.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, indent=4)

    with open('results.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['name', 'path', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    with open('results.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)
    return total_size


if __name__ == '__main__':
    traverse_directory(os.getcwd())