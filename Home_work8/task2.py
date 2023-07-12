# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import os
import json
import pickle


def convert_json_to_pickle(json_file_path):
    file_directory = os.path.dirname(json_file_path)
    file_name = os.path.splitext(os.path.basename(json_file_path))[0]

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    pickle_file_path = os.path.join(file_directory, f'{file_name}.pickle')

    with open(pickle_file_path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def convert_directory_jsons_to_pickles(directory_path):
    files = os.listdir(directory_path)

    for file in files:
        if file.endswith('.json'):
            json_file_path = os.path.join(directory_path, file)
            convert_json_to_pickle(json_file_path)


if __name__ == '__main__':
    convert_directory_jsons_to_pickles(os.getcwd())